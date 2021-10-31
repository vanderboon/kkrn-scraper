#!/usr/bin/env python3

import colorama
import typer
from typer import Argument

from kkrn.lib import getMaxPages

def main() -> None:
    """Gets the maximum number of pages."""
    print(getMaxPages(0))

# Allow the script to be run standalone (useful during development).
if __name__ == "__main__":
    typer.run(main)
