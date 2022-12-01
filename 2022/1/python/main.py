with open("../input.txt", "r") as f:
    lines = f.readlines()

class Elf():
    def __init__(self, number):
        self.number = number
        self.calories = 0

elves = []
elf = Elf(0)

for line in lines:
    line = line.strip()
    if not line: 
        elves.append(elf)
        elf = Elf(len(elves)-1)
    else:
         elf.calories += int(line)

elves.sort(key=lambda x: -x.calories)
top_three_elves = elves[:3]
top_three_sum = sum(map(lambda x: x.calories, top_three_elves))

print("Top three elves:")
for e in top_three_elves:
    print(f"    Elf #{e.number} has {e.calories} calories")
print(f"Together they are carrying {top_three_sum} calories")
