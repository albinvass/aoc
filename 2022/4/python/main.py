with open("../input.txt", "r") as f:
    lines = f.readlines()

lines = list(map(str.strip, lines))


def part_one():
    results = []
    for line in lines:
        if line:
            (first, second) = list(map(lambda s: s.split("-"),
                                       line.strip().split(",")))
            r1 = range(int(first[0]), int(first[1])+1)
            r2 = range(int(second[0]), int(second[1])+1)
            result = set(r1).issubset(r2) or set(r2).issubset(r1)
            results.append(result)
    results = filter(lambda x: x, results)
    print(f"Part 1: {len(list(results))}")


part_one()


def part_two():
    results = []
    for line in lines:
        if line:
            (first, second) = list(map(lambda s: s.split("-"),
                                       line.strip().split(",")))
            r1 = range(int(first[0]), int(first[1])+1)
            r2 = range(int(second[0]), int(second[1])+1)
            result = not set(r1).isdisjoint(r2)
            results.append(result)
            print(f"{r1=},{r2=} - {not set(r1).isdisjoint(r2)}")
    results = filter(lambda x: x, results)
    print(f"Part 2: {len(list(results))}")


part_two()
