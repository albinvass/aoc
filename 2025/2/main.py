#!/usr/bin/env python

with open("input", "r") as f_h:
    input = [ line.strip() for line in f_h.read().split(",") ]

def is_invalid(id: str) -> bool:
    l = len(id)
    if l % 2 != 0:
        return False
    b = id[:int(l/2)]
    e = id[int(l/2):]
    if b == e:
        return True

    return False

total = 0

for r in input:
    start, end = r.split("-")
    for id in range(int(start), int(end)+1):
        if is_invalid(str(id)):
            total += id
        else:
            pass

print(total)



