input: str

with open("day6.input.txt", "r") as f:
    input = f.read()

def solve(input: str):
    result = 0
    buffer = []
    for char in input:
        buffer.append(char)
        result += 1
        repetitions = 0
        for el in buffer:
            for e in buffer:
                if el == e:
                    repetitions += 1
        if repetitions == 4:
            return result
        buffer = buffer[-3:]
        

print(solve(input))