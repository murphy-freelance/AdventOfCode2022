input: list[list[str]] = []

with open("day3.input.txt", "r") as f:
    lines = f.readlines()
    lines = [l.strip() for l in lines]
    for i in range(len(lines)):
        if(i % 3 == 0):
            input.append([lines[i]])
        else:
            input[-1].append(lines[i])


def solve(input: list[list[str]]):
    commons = []
    result = 0
    for group in input:
        for item in group[0]:
            if item in group[1] and item in group[2]:
                commons.append(item)
                break
    for c in commons:
        unicode = ord(c)
        priority = 0
        if unicode >= 65 and unicode <= 90:
            priority = unicode - 64 + 26
        if unicode >= 97 and unicode <= 122:
            priority = unicode - 96
        result += priority
    print(f"Result: {result}")

solve(input)