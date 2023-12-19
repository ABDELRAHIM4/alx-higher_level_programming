#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(list_length):
        try:
            element_1 = my_list_1[i]
            element_2 = my_list_2[i]
            if isinstance(element_1, (int, float)) and isinstance(element_2, (int, float)):
                new_list.append(element_1 / element_2)
            else:
                print("wrong type")
                new_list.append(0)
        except IndexError:
            print("out of range")
            new_list.append(0)
        except ZeroDivisionError:
            print("division by 0")
            new_list.append(0)
    return new_list
