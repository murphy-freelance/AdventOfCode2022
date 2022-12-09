input: dict

with open("day7.input.txt", "r") as f:
    lines = [l.strip() for l in f.readlines()]
    directories = {}
    prec = []
    current = directories
    for line in lines:
        command = line.split()
        match command[0]:
            case '$':
                if command[1] == "cd":
                    if command[2] == "/":
                        current = directories
                    elif command[2] == "..":
                        if len(prec) > 0:
                            current = prec.pop()
                    else:
                        dir = command[2]
                        if not current[dir]:
                            current.update({dir: {}})
                        prec.append(current)
                        current = current[dir]
            case "dir":
                current.update({command[1]: {}})
            
            case _:
                current.update({command[1]: int(command[0])})
    input = directories


def get_sum(k, dir: dict, output: dict):
    res = 0
    for key,v in dir.items():
        if type(v) == dict:
            res += get_sum(key,v, output)
        elif type(v) == int:
            res += v
    output.append(res)
    return res

def solve(input: dict):
    res = 0
    outputs = []
    get_sum("/",input, outputs)
    delta = 70000000 - outputs[-1] - 30000000
    for v in outputs:
        if v >= abs(delta):
            return v

print(solve(input))