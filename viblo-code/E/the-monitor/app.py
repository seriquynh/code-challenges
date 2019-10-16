#!/usr/bin/env python3
import sys
from fractions import Fraction as F

def solution(a, b, c, d):
    w = a
    h = (d * w) / c

    if h <= b:
        m = b * c - d * w
        n = b * c
    else:
        h = b
        m = a * d - c * h
        n = a * d

    print(F(m, n))

input_str = ''
input_str = '1 1 3 2'
# input_str = '4 3 2 2'
# input_str = '3 4 2 3'

a = int(input_str[0])
b = int(input_str[2])
c = int(input_str[4])
d = int(input_str[6])

solution(a, b, c, d)
