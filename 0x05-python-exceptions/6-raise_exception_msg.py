#!/usr/bin/python3
def raise_exception_msg(message=""):
    if message:
        raise NameError(message)
    else:
        raise NameError("An error occurred")
