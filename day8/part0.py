import numpy as np

input: list[list[int]] = []

with open("C:/Users/giuse/Documents/AdventOfCode/day8/day8.input.txt", "r") as f:
    lines = [l.strip() for l in f.readlines()]
    for line in lines:
        layer = [int(c) for c in line]
        input.append(layer)

input = np.array(input)

def isVisible(x: int, y: int, map: np.array):
    if x == 0 or x == map.shape[0] - 1:
        return True
    if y == 0 or y == map.shape[1] - 1:
        return True
    value = map[x, y]

    visible = True
    for el in map[:x, y]:
        if el >= value:
            visible = False
    if visible: return True

    visible = True
    for el in map[x+1:, y]:
        if el >= value:
            visible = False
    if visible: return True

    visible = True
    for el in map[x, :y]:
        if el >= value:
            visible = False    
    if visible: return True
    
    visible = True
    for el in map[x, y+1:]:
        if el >= value:
            visible = False    
    if visible: return True

    return visible

def solve(input: np.array):
    res = 0
    x_dim, y_dim = input.shape
    for x in range(x_dim):
        for y in range(y_dim):
            its = isVisible(x,y,input)
            res += 1 if its else 0
    return res

print(solve(input))