#!/usr/bin/env python3
import sys

def solution(n, m):
    if n == m:
        result = 0
    elif n > m:
        result = n - m

    result = 0
    while n < m:
        n *= 2
        result += 1

    result += n - m

    print(result)

lines = []

for line in sys.stdin:
    lines += line

n = int(lines[0][0])
m = int(lines[0][2])

solution(n, m)
