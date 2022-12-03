#! python
listOfRucksacks = open("./inputs/aoc-d3.txt")
elfGroup = ""
allElfGroups = []
duplicatedItems = []
numberInGroup = 0
sumOfGroupCommonItem = 0

for ruckSack in listOfRucksacks:
    elfGroup += (" " + ruckSack)
    numberInGroup += 1
    if numberInGroup == 3:
        elfGroup = elfGroup.replace("\n", "")
        elfGroup = elfGroup.strip()
        allElfGroups.append(elfGroup)
        elfGroup = ""
        numberInGroup = 0

for group in allElfGroups:
    group = group.rsplit(" ")
    firstRuckSack = group[0]
    secondRuckSack = group[1]
    thirdRuckSack = group[2]
    for ruckSack in group:
        ruckSack = [i for i in ruckSack]
        ruckSack = list(dict.fromkeys(ruckSack))
    for item in firstRuckSack:
        print(firstRuckSack)
        if secondRuckSack.count(item) != 0 and thirdRuckSack.count(item) != 0:
            duplicatedItems.append(item)


# Use ASCII values to avoid making maps for letter values
for item in duplicatedItems:
    if item.islower():
        sumOfGroupCommonItem += (ord(item)-96)
    if item.isupper():
        sumOfGroupCommonItem += (ord(item)-38)

print(duplicatedItems)
print(sumOfGroupCommonItem)