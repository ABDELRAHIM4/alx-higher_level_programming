#!/usr/bin/python3
class LockedClass:
    def __setattr__(self, key, value):
        if key != "first_name" and not hasattr(self, key):
            raise AttributeError("'LockedClass' object has no attribute '{}'".format(key))
        super().__setattr__(key, value)
