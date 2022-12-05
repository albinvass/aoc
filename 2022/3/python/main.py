with open("../input.txt", "r") as f:
    lines = f.readlines()

def get_prio(x):
    score = 0
    if x >= "a" <= "z":
        score = ord(x) - 96
    elif x >= "A" <= "Z":
        score = ord(x) - 64 + 26
    return score

def part_one():
    total = 0
    for line in lines:
        (slot1, slot2) = (line[len(line)//2:], line[:len(line)//2])
        common = set(slot1).intersection(slot2)
        total += sum(map(get_prio, common))

    print(f"Part 1: {total}")
part_one()


def part_two():
    backpacks = list(map(str.strip, lines))
    groups = [
        [backpacks[i], backpacks[i+1], backpacks[i+2]]
        for i in range(0, len(backpacks)-1, 3)
    ]
    badges = []
    for group in groups:
        badge = set(group[0]).intersection(group[1]).intersection(group[2])
        badges.append(badge.pop())
    total = sum(map(get_prio, badges))
    print(f"Part 2: {total}")
part_two()
