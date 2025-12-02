#!/usr/bin/env python

with open("input", "r") as f_h:
    input = [ line.strip() for line in f_h.readlines() ]

pos = 50
count = 0

def string_to_move(line: str) -> int:
    move = 0
    if line.startswith("L"):
        move -= int(line[1:])
    else:
        move = int(line[1:])
    return move

def normalize(pos: int) -> int:
    while pos < 0 or pos >= 100:
        if pos >= 100:
            pos -= 100
        elif pos < 0:
            pos +=100
    return pos


for line in input:
    pos += string_to_move(line)
    pos = normalize(pos)

    if pos == 0:
        count += 1

print(count)
