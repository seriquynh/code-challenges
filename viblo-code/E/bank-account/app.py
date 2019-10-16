#!/usr/bin/env python3
import sys

def solution(n):
    length = len(n)
    a = int(n[length - 1]) # end character
    b = int(n[length - 2])
    result = n
    if n[0] == '-':
        if a > b and a != 0:
            result = n[:length - 1]
        else:
            result = n[:length - 2] + str(a)
    else:
        if a > b:
            result = n[:length - 2] + str(a)
        elif a != 0:
            result = n[:length - 1]
    if result == '-0':
        result = '0'
    print(result)

# input_str = ""

# for line in sys.stdin:
#     input_str += line

input_str = '-10'

solution(input_str)
