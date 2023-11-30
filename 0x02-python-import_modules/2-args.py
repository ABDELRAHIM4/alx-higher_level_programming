#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    num_args = len(sys.argv)

    if num_args == 0 or num_args == 1:
        print("{} argument(s).".format(num_args - 1))
    elif num_args > 1:
        print("{} argument(s):".format(num_args - 1))

        for i, arg in enumerate(sys.argv[1:], start=1):
            print(f"{i}: {arg}")
    else:
        print("Error: unexpected number of arguments.")
