input: list[str]

win = [1, 2, 0]
lose = [2, 0, 1]

mapper = {
    'A': 0,
    'B': 1,
    'C': 2,
    'X': 0,
    'Y': 1,
    'Z': 2
}

result = 0
failed = []

with open("day2.input.txt", "r") as f:
    input = f.readlines()

for entry in input:
    score = 0
    entry = entry.strip()
    opponent = mapper[entry[0]]
    outcome = mapper[entry[2]]
    score = outcome * 3
    my = 0
    if(outcome == 1):
        my = opponent
    elif(outcome == 0):
        my = lose[opponent]
    else:
        my = win[opponent]
    score += my + 1
    result += score
    print(opponent, score, my, outcome)

print(f"Score: {result}")
    