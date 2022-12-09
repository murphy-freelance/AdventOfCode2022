from math import sqrt
input: list[tuple[str, int]] = []

with open("day9.input.txt", "r") as f:
    lines = [l.strip() for l in f.readlines()]
    for l in lines:
        l = l.split()
        l[1] = int(l[1])
        input.append(tuple(l))

def isNear(a: list[int], b: list[int]):
    if sqrt(pow(a[0] - b[0], 2) + 
        pow(a[1] - b[1],2)) <= sqrt(2):
        return True
    return False

def solve(input: list[tuple[str,int]]):
    positions = []
    h = [0, 0]
    t = [0, 0]
    for d, v in input:
        for i in range(v):
            match d:
                case "L":
                    h[0] -= 1
                case "R":
                    h[0] += 1
                case "U":
                    h[1] += 1
                case "D":
                    h[1] -= 1
            while not isNear(t, h):
                dX = t[0] - h[0]
                dY = t[1] - h[1]
                if dX != 0:
                    t[0] += int(dX / abs(dX)) * -1
                if dY != 0:
                    t[1] += int(dY / abs(dY)) * -1
            if not tuple(t) in positions:
                positions.append(tuple(t))
    return len(positions)


print(solve(input))