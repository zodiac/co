#!/usr/bin/env python3
from __future__ import print_function

import sys
if sys.version_info[0] < 3:
    input = raw_input

n, m = input().split(' ')
n = int(n)
m = int(m)
s = input()

last_char = None
start = None

score = 0

for i, c in enumerate(s):
    if last_char == "." and c != ".":
        score += (i - start - 1)
        start = None
    if last_char != "." and c == ".": start = i
    last_char = c

if start is not None:
    score += (n - start - 1)

s = list(s)

so = []

for _ in range(m):
    i, c = input().split()
    i = int(i) - 1

    if c == "." and s[i] != ".":
        if i-1 >= 0 and s[i-1] == ".": score += 1
        if i+1 < n and s[i+1] == ".": score += 1
    if c != "." and s[i] == ".":
        if i-1 >= 0 and s[i-1] == ".": score -= 1
        if i+1 < n and s[i+1] == ".": score -= 1

    s[i] = c
    so += [str(score)]

# print('\n'.join(so))