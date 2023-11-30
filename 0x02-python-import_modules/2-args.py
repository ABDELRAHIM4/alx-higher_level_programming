#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    argv = sys.argv
    num_args = len(argv) - 1

    if num_args == 0:
        print("{} arguments.".format(num_args))
    elif num_args == 1:
        print("{} argument:".format(num_args))
        for i in range(1, num_args + 1):
            print("{}: {}".format(i, argv[i]))
    else:
        print("{} arguments:".format(num_args))
        for i in range(1, num_args + 1):
            print("{}: {}".format(i, argv[i]))

