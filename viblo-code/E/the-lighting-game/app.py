#!/usr/bin/env python3
import sys

def solution(m):
    states = [[1, 1, 1],
              [1, 1, 1],
              [1, 1, 1]]
    for i in range(0, 3):
        for j in range(0, 3):
            _change_states(states, i, j)
    for i in range(0, 3):
        for j in range(0, 3):
            print(states[i][j], end = '')
        print('')

def _valid_index(i, j):
    return 0 <= i < 3 and 0 <= j < 3

def _new_state(state):
    if state == 1:
        return 0
    else:
        return 1

def _change_states(states, i, j):
    value = int(m[i][j])
    if value % 2 == 1:
        states[i][j] = _new_state(states[i][j])
        if _valid_index(i + 1, j + 1):
            states[i + 1][j + 1] = _new_state(states[i + 1][j + 1])
        if _valid_index(i + 2, j):
            states[i + 2][j] = _new_state(states[i + 2][j])
        if _valid_index(i + 1, j - 1):
            states[i + 1][j - 1] = _new_state(states[i + 1][j - 1])
        if _valid_index(i + 1, j):
            states[i + 1][j] = _new_state(states[i + 1][j])

m = []

for line in sys.stdin:
    m.append(line.strip().split(' '))

solution(m)
