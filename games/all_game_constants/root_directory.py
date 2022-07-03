"""
Module to specify the absolute path to the root directory. Note that this file is at depth 2
from the root, hence the parents[2].
All relative paths navigate from the ROOT_DIRECTORY
"""

# Standard library imports
from pathlib import Path

ROOT_DIRECTORY = Path(__file__).parents[2]
