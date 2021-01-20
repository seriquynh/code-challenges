#!/usr/bin/env python3
import sys

def solution(m):
    i = 0
    valid = True
    while m != '':
        if m[i:i + 3] == '144':
            m = m[i + 3:]
        elif m[i:i + 2] == '14':
            m = m[i + 2:]
        elif m[i:i + 1] == '1':
            m = m[i + 1:]
        else:
            valid = False
            break
    if valid:
        print('YES')
    else:
        print('NO')

input_str = ""

for line in sys.stdin:
    input_str += line

solution(input_str)
