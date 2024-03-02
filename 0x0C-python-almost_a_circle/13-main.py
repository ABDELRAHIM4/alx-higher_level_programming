#!/usr/bin/python3
""" 13-main """
from models.square import Square

if __name__ == "__main__":

    s1 = Square(10, 2, 1)
    print(s1)
    s1_dictionary = s1.to_dictionary()
    print(s1_dictionary)
    print(type(s1_dictionary))

    s2 = Square(1, 1)
<<<<<<< HEAD
=======
    print(s2)
    s2.update(**s1_dictionary)
    print(s2)
    print(s1 == s2)
>>>>>>> 5770ad8c2ccb4eb2fe172ea4a86169f0c2dea12d

