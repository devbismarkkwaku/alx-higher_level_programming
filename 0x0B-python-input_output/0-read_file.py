#!/usr/bin/python3
"""
Contains the function: read_file
"""


def read_file(filename=""):
    """
    reads and prints to stdout, a text file
    """
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
