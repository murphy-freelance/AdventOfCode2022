input: list[str]

with open("day3.input.txt", "r") as f:
    lines = f.readlines()
    input = [l.strip() for l in lines]

def solve(input: list[str]):
    commons = []
    result = 0
    for bag in input:
        half = round(len(bag) / 2)
        sacks = [bag[0:half], bag[half:]]
        for item in sacks[0]:
            if item in sacks[1]:
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