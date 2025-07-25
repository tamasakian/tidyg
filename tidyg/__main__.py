#!/usr/bin/env python3

import argparse
import sys

from tidyg import functions

def main():
    args = parse_args()
    function = functions[args.function]
    try:
        function(*args.args)
    except TypeError as e:
        print(e)
        sys.exit(1)

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("function", choices=functions)
    parser.add_argument("args", type=str, nargs="*")
    args = parser.parse_args()
    return args

functions = {
    "root2hog": functions.root2hog,
    "omamer2hog": functions.omamer2hog,
    "pivot_wider": functions.pivot_wider,
    "pivot_longer": functions.pivot_longer,
}

if __name__ == "__main__":
    main()