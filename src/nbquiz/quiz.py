"""
YAML Representation of a quiz.

A quiz is generated from one or more test banks and a YAML file
describing the questions on the quiz. Parameterized variants can
be generated inside of the YAML.

This module is a front-end for handling the YAML. Back ends are
responsible for generating output, for example a Canvas export
package.
"""

from abc import ABC
from importlib.resources import files

import yamale

from nbquiz.question import QuestionGroup, TestQuestion
from nbquiz.testbank import bank


class Quiz(ABC):
    """
    Back end processors should override this class.
    """

    def load_file(self, filename: str):
        """Load a YAML quiz description from a file."""
        self._load(yamale.make_data(path=filename))

    def load_str(self, yaml: str):
        """Load a YAML quiz description from a string."""
        self._load(yamale.make_data(content=yaml))

    def _load(self, data):
        schema = yamale.make_schema(
            content=files("nbquiz.resources").joinpath("quiz_schema.yaml").read_text()
        )
        yamale.validate(schema, data)
        data = list(data)
        if len(data) > 1:
            raise ValueError("Quiz YAML files must only contain one document.")
        data = data[0][0]

        self.set_title(data["title"])
        self.set_description(data["description"])

        def elaborate_group(questions_data):
            for question_data in questions_data:
                match question_data:
                    case {"name": name, "params": params}:
                        question = bank.find(f"@{name}")
                        variant = question.variant(**params)
                        yield variant
                    case str() as name:
                        question = bank.find(f"@{name}")
                        if isinstance(question, QuestionGroup):
                            raise ValueError("Canvas does not allow groups in groups.")
                        yield bank.find(f"@{name}")

        for question_data in data["questions"]:
            match question_data:
                case {"group": group, "questions": questions}:
                    self.add_group(QuestionGroup(group, list(elaborate_group(questions))))

                case {"name": name, "params": params}:
                    question = bank.find(f"@{name}")
                    variant = question.variant(**params)
                    self.add_question(variant)

                case str() as name:
                    question = bank.find(f"@{name}")
                    if isinstance(question, type) and issubclass(question, TestQuestion):
                        self.add_question(question)
                    elif isinstance(question, QuestionGroup):
                        self.add_group(question)

                case _:
                    raise ValueError(f"I don't understand this: {question_data}")

    def set_title(self, title: str):
        """Set the title"""
        raise NotImplementedError()

    def set_description(self, description: str):
        """Set the description"""
        raise NotImplementedError()

    def add_file(self, filename: str):
        """Add an attached file."""
        raise NotImplementedError()

    def add_question(self, question: TestQuestion):
        """Add a test question"""
        raise NotImplementedError()

    def add_group(self, group: QuestionGroup):
        """Add a question group."""
        raise NotImplementedError()