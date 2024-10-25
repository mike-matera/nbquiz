"""
Export a test bank to canvas.
"""

import logging

from nbquiz.canvas.export import CanvasExport
from nbquiz.testbank import bank

logging.basicConfig(level=logging.INFO)


def add_args(parser):
    parser.add_argument("testyaml", help="A YAML file containing a description of a test.")
    parser.add_argument("output", help="A ZIP file that will have the Canvas export package.")


def main(args):
    bank.load()
    logging.info(f"Loading test file: {args.testyaml}")
    with open(args.testyaml) as fh:
        e = CanvasExport.from_yaml(fh)
    logging.info(f"Writing {args.output}")
    e.write(args.output)
