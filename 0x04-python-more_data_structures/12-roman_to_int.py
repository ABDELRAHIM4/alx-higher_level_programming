#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_to_int_map = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    
    if roman_string is None or not isinstance(roman_string, str):
        return 0
    
    total = 0
    i = 0
    
    while i < len(roman_string):
        s1 = roman_to_int_map.get(roman_string[i], 0)
        
        if i + 1 < len(roman_string):
            s2 = roman_to_int_map.get(roman_string[i + 1], 0)
            
            if s1 >= s2:
                total += s1
                i += 1
            else:
                total += s2 - s1
                i += 2
        else:
            total += s1
            i += 1
    
    return total
