#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    index = 0
    counter = 0
    while(counter < x):
        try:
            print("{:d}".format(int(my_list[index])), end = "")
            counter += 1
            index += 1
        except ValueError:
            index += 1
        except:
            break
        if counter == x:
            break
    print()
    return counter
