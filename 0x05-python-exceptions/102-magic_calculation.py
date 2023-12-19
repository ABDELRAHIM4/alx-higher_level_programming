#!/usr/bin/python3
result = 0

    try:
        for i in range(1, 3):
            if i > a:
                raise Exception('Too far')
            else:
                result += a ** b / i

    except Exception as e:
        print(e)
        result = a + b

    return result
