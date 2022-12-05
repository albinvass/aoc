with open("../input.txt", "r") as f:
    lines = f.readlines()

lines = [line.strip("\n") for line in lines]


def get_starting_state():
    ship = {}
    empty_line_index = 0
    for line in lines:
        if not line:
            break
        empty_line_index += 1

    piles = lines[empty_line_index-1].split()
    starting_state = lines[:empty_line_index+1]
    for pile in piles:
        ship[pile] = []
        for i in range(empty_line_index-2, -1, -1):
            crate = starting_state[i][1+(int(pile)-1)*4].strip()
            if crate:
                ship[pile].append(crate)
    return ship, lines[empty_line_index+1:]


def part_one():
    ship, instructions = get_starting_state()
    for ins in instructions:
        if ins:
            (cmd, n, _, fr, _, to) = ins.split()
            for i in range(0, int(n)):
                ship[to].append(ship[fr].pop())

    print("Part One:")
    for pile in ship.keys():
        print(f"{pile}: {ship[pile].pop()}")
    print("")
    print("")


part_one()


def part_two():
    ship, instructions = get_starting_state()
    for ins in instructions:
        if ins:
            (cmd, n, _, fr, _, to) = ins.split()
            buffer = []
            for i in range(0, int(n)):
                buffer.append(ship[fr].pop())

            buffer.reverse()
            for b in buffer:
                ship[to].append(b)

    print("Part Two:")
    for pile in ship.keys():
        print(f"{pile}: {ship[pile].pop()}")


part_two()
