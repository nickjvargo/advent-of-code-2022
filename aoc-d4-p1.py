#! python
import re

listOfSectionAssignments = open("./inputs/aoc-d4.txt")
redundantSections = 0

for pairOfAssignments in listOfSectionAssignments:
    numbers = re.search("(\d+)-(\d+),(\d+)-(\d+)", pairOfAssignments)
    firstRangeStart = int(numbers.group(1))
    firstRangeEnd = int(numbers.group(2))
    secondRangeStart = int(numbers.group(3))
    secondRangeEnd = int(numbers.group(4))
    
    if firstRangeStart >= secondRangeStart and firstRangeEnd <= secondRangeEnd:
        redundantSections += 1
    elif secondRangeStart >= firstRangeStart and secondRangeEnd <= firstRangeEnd:
        redundantSections += 1

    
print(redundantSections)