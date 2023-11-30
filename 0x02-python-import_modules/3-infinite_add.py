#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    def add_args(*args):
        return sum(int(arg) for arg in args)

    if __name__ == "__main__":
        print(add_args(*sys.argv[1:]))
