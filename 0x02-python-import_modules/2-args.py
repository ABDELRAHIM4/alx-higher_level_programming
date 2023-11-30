#!/usr/bin/python3
import sys

def main():
    argv = sys.argv
    num_args = len(argv)

    if num_args == 1:
        print("0 arguments.")
    else:
        print(f"{num_args-1} argument(s):")
        for i in range(1, num_args):
            print(f"{i}: {argv[i]}")

if __name__ == "__main__":
    main()
