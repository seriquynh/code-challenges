#!/usr/bin/env python3
import sys

def solution(n, a):
    check = len(a) / 2 + 1
    counter = {}
    valid = True
    for number in a:
        if number not in counter:
            counter[number] = 0
        counter[number] += 1
        if counter[number] > check:
            valid = False
            break
    if valid:
        print('YES')
    else:
        print('NO')

# input_str = ""

# for line in sys.stdin:
#     input_str += line

input_str = '3\n1 1 2'

parsed = input_str.split('\n')
n = parsed[0]
a = parsed[1].split(' ')

print(n, a)

solution(n, a)
