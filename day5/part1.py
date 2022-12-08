stacks = [
    [],[],[],[],[],[],[],[],[],[]
]
operations = []

with open("day5.input.txt", "r") as f:
    lines = [l for l in f.readlines()]
    turn = False
    for l in lines:
        if l.strip() == '':
            turn = True
        elif turn:
            l = l.split(" ")
            operations.append([
                int(l[1]),int(l[3]), int(l[5])
            ])
        else:
            if not l[1] == "1":
                for i in range(9):
                    if i == 0:
                        if l[1] != " ":
                            stacks[i + 1].insert(0, l[1])
                    elif i:
                        c = l[1 + i * 4]
                        if c != " ":
                            stacks[i + 1].insert(0, c)

def solve(stacks: list[list[str]], operations: list[list[int]]):
    result = ""

    for operation in operations:
        cargos = []
        for i in range(operation[0]):
            cargos.insert(0,stacks[operation[1]].pop())
        stacks[operation[2]].extend(cargos)
    
    for stack in stacks:
        if len(stack) > 0:
            result += stack[-1]
    
    return result

print(solve(stacks, operations))
