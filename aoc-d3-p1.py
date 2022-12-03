#! python
listOfRucksacks = open("./inputs/aoc-d3.txt")
duplicatedItems = []
sumOfItemValues = 0

for ruckSack in listOfRucksacks:
    # Necessary for \n
    minusLineBreak = 0
    if ruckSack.count("\n") == 1:
        minusLineBreak = 1

    compartmentDivider = int((len(ruckSack)-minusLineBreak) / 2)
    firstCompartment = ruckSack[:compartmentDivider]
    secondCompartment = ruckSack[compartmentDivider:]

    for item in firstCompartment:
        if secondCompartment.count(item) != 0:
            duplicatedItems.append(item)
            break

# Use ASCII values to avoid making maps for letter values
for item in duplicatedItems:
    if item.islower():
        sumOfItemValues += (ord(item)-96)
    if item.isupper():
        sumOfItemValues += (ord(item)-38)

print(sumOfItemValues)