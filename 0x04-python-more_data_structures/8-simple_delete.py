#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    if key is None:
        return(a_dictionary)
    else:
        a_dictionary.pop(key,None)
        return(a_dictionary)
