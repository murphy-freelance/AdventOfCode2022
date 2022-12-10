input: list[tuple[str, int]] = []
clocks = [i for i in range(20, 221, 40)]

with open("day10.input.txt", "r") as f:
    lines = [l.strip() for l in f.readlines()]
    for l in lines:
        l = l.split()
        input.append((l[0], int(l[1]) if len(l) > 1 else 0))

def solve(input: list[tuple[str, int]]):
    signals = 0
    clock = 0
    register = 1
    for command in input:
        match command[0]:
            case "addx":
                for i in range(2):
                    clock += 1
                    if clock in clocks:
                        signals += clock * register
                register += command[1]
            case "noop":
                clock += 1
                if clock in clocks:
                    signals += clock * register
    return signals

print(solve(input))