"""
Interface for a group of test banks.
"""

from pathlib import Path
from typing import Union

import nbformat

from nbquiz.testcase import CellQuestion, FunctionQuestion, TestQuestion


class TestBank:
    """A group of test loaded from multiple files."""

    def __init__(self):
        self._tags = {}
        self._required = {}
        self._forbidden = {}
        self._questions = {}

    def load(self, *path: Union[str, Path]) -> None:
        for p in path:
            self._load(p)

    def stats(self):
        return {
            "questions": len(self._questions),
            "tags": len(self._tags),
            "required": len(self._required),
            "forbidden": len(self._forbidden),
        }

    def _load(self, filename: Union[str, Path]):
        nb = nbformat.read(filename, nbformat.NO_CONVERT)
        source = "\n\n".join(
            [
                cell["source"]
                for cell in nb["cells"]
                if cell["cell_type"] == "code"
                and "tags" in cell["metadata"]
                and "question" in cell["metadata"]["tags"]
            ]
        )
        test_ns = {}
        exec(source, test_ns)
        for attr in test_ns:
            # print("Looking at:", attr, test_ns[attr])
            if (
                isinstance(test_ns[attr], type)
                and issubclass(test_ns[attr], TestQuestion)
                and test_ns[attr] not in [TestQuestion, FunctionQuestion, CellQuestion]
            ):
                test_ns[attr].validate()
                self._questions[test_ns[attr]._celltag] = {
                    "class": test_ns[attr],
                    "source": source,
                }
        # Rebuild the caches
        self._tags = {}
        self._required = {}
        self._forbidden = {}
        for q in self._questions.values():
            for t in q["class"].tags:
                if t not in self._tags:
                    self._tags[t] = [q]
                else:
                    self._tags[t].append(q)
            for r in q["class"].tokens_required:
                if r not in self._required:
                    self._required[r] = [q]
                else:
                    self._required[r].append(q)

            for f in q["class"].tokens_forbidden:
                if f not in self._forbidden:
                    self._forbidden[f] = [q]
                else:
                    self._forbidden[f].append(q)

    @property
    def questions(self):
        return self._questions
