input: str = ""

with open("0day1.input.txt", "r") as f:
    input = f.read()

print(input)

elves = [0]
splitted = input.split("\n")

for entry in splitted:
    if(entry == ''):
        elves.append(0)
    else:
        elves[-1] += int(entry)

top = []

elves.sort(reverse=True)
result = sum(elves[0:3]) 

print(f"Result: {result}")