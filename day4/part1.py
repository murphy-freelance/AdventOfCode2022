input: list[list[list[int]]] = []

with open("day4.input.txt", "r") as f:
    for line in f.readlines():
        line = line.strip()
        obj: list[str] = [l for l in line.split(',')]
        res = []
        res.append([int(i) for i in obj[0].split("-")])
        res.append([int(i) for i in obj[1].split("-")])
        input.append(res)

print(input)

def solve(input: list[list[list[int]]]):
    count = 0
    for pair in input:
        range0 = range(pair[0][0], pair[0][1] + 1)
        range1 = range(pair[1][0], pair[1][1] + 1)
        for n in range0:
            if n in range1:
                count += 1
                break
    return count
        
print(f"Result: {solve(input)}")