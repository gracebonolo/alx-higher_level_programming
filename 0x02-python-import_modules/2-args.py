#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    num_args = len(argv) - 1
    args = argv[1:]

    if num_args == 0:
        print("0 arguments.")
    else:
        print("{:d} argument{}:".format(num_args, 's' if num_args > 1 else ''))
        for i, arg in enumerate(args, 1):
            print("{:d}: {}".format(i, arg))
