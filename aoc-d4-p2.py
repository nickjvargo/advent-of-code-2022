#! python
import re

listOfSectionAssignments = open("./inputs/aoc-d4.txt")
assignmentsWithAnyOverlap = 0

for pairOfAssignments in listOfSectionAssignments:
    numbers = re.search("(\d+)-(\d+),(\d+)-(\d+)", pairOfAssignments)
    firstRangeStart = int(numbers.group(1))
    firstRangeEnd = int(numbers.group(2))
    secondRangeStart = int(numbers.group(3))
    secondRangeEnd = int(numbers.group(4))

    if firstRangeStart >= secondRangeEnd and firstRangeStart <= secondRangeEnd:
        assignmentsWithAnyOverlap += 1
    elif firstRangeEnd >= secondRangeStart and firstRangeEnd <= secondRangeEnd:
        assignmentsWithAnyOverlap += 1
    elif secondRangeStart >= firstRangeStart and secondRangeStart <= firstRangeEnd:
        assignmentsWithAnyOverlap += 1
    elif secondRangeEnd >= firstRangeStart and secondRangeEnd <= firstRangeEnd:
        assignmentsWithAnyOverlap += 1
    
print(assignmentsWithAnyOverlap)