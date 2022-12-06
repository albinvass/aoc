with open("../input.txt", "r") as f:
    msg = f.read()
msg = msg.strip("\n")

def get_marker_position(msg, l):
    for i in range(l-1, len(msg)):
        s = msg[i:i+l]
        if len(s) == len(set(s)):
            return i+l

def part_one():
    print(f"Part One: {get_marker_position(msg, 4)}")


part_one()


def part_two():
    print(f"Part One: {get_marker_position(msg, 14)}")


part_two()
