input: list[tuple[str, int]] = []

with open("C:/Users/giuse/Documents/AdventOfCode/day10/day10.input.txt", "r") as f:
    lines = [l.strip() for l in f.readlines()]
    for l in lines:
        l = l.split()
        input.append((l[0], int(l[1]) if len(l) > 1 else 0))

def solve(input: list[tuple[str, int]]):
    clock = 0
    sprite = 1
    display = ["." for i in range(240)]
    delay = 0
    count = 0
    value = 0
    for i in range(240):
        if delay == 1:
            delay -= 1
            sprite += value
            value = 0
        if abs(clock - sprite) <= 1:
            display[i] = "#"
        if delay > 1:
            delay -= 1
        elif count < len(input):
                i, v = input[count]
                match i:
                    case "addx":
                        value = v
                        delay = 2
                    case "noop":
                        delay = 1
                count += 1
        clock += 1
        if clock % 40 == 0:
            clock = 0
    return display

def display(solution: list[str]):
    line = ""
    for i,v in enumerate(solution):
        line += v
        if (i + 1) % 40 ==0:
            print(line)
            line = ""

display(solve(input))
