#! python
import re

input = open("./samples/aoc-d5.txt")
numberOfStacks = 0
instructions = []

for line in input:
    line = line.replace("\n", "")
    print(line)
    if re.match("(\s\d+)", line):
        # Removes all whitespace to find length
        line = "".join(line.split())
        numberOfStacks = len(line)
    elif re.match("^move", line):
        instructions.insert(len(instructions), line)
    elif re.search("\[", line):
        print("stacks found")


print("found number of columns ", numberOfStacks)
print(instructions)