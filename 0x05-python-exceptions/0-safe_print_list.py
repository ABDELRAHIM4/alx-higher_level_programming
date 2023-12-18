#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    index = 0
    counter = 0
    for element in my_list:
        try:
            print(element, end = "")
            index += 1
            counter += 1
        except IndexError:
            print("ERROR")
            break
        if counter == x:
            break
    print()
    return x
