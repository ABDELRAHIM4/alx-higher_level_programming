#!/usr/bin/python3
class MyList(list):
    """ make a class from MyList that inherits from list """
    def append(self, item):
        """ append an item to the list"""
        if not isinstance(item, int):
            raise TypeError('All elements of the list must be of type int')
        super().append(item)
    def print_sorted(self):
        """ sort the list """
        sorted_list = sorted(self)
        print(sorted_list)
