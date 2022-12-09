import numpy as np

input: list[list[int]] = []

with open("C:/Users/giuse/Documents/AdventOfCode/day8/day8.input.txt", "r") as f:
    lines = [l.strip() for l in f.readlines()]
    for line in lines:
        layer = [int(c) for c in line]
        input.append(layer)

input = np.array(input)

def getScore(x: int, y: int, map: np.array):
    if x == 0 or x == map.shape[0] - 1:
        return 0
    if y == 0 or y == map.shape[1] - 1:
        return 0
    value = map[x, y]
    res = 1

    count = 0
    for el in np.flip(map[:x, y]):
        count += 1
        if el >= value:
            break
    res *= count

    count = 0   
    for el in map[x+1:, y]:
        count += 1
        if el >= value:
            break
    res *= count

    count = 0
    for el in np.flip(map[x, :y]):
        count += 1
        if el >= value:
            break
    res *= count

    count = 0
    for el in map[x, y+1:]:
        count += 1
        if el >= value:
            break
    res *= count

    return res

def solve(input: np.array):
    res = 0
    x_dim, y_dim = input.shape
    for x in range(x_dim):
        for y in range(y_dim):
            score = getScore(x, y, input)
            if res < score:
                res = score
    return res

print(solve(input))