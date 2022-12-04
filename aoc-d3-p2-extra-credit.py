#! python

# This solution is more dynamic than the first one. It works by creating groups
# the size of the maxNumberPerGroup variable, eliminating repeat letters in each
# rucksack, then iterating through the rucksacks and only marking an item as duplicated
# if it is in all three rucksacks with the ues of flags.

listOfRucksacks = open("./inputs/aoc-d3.txt")
elfGroup = ""
allElfGroups = []
duplicatedItems = []
numberInGroup = 0
maxNumberPerGroup = 3
sumOfGroupCommonItem = 0

for ruckSack in listOfRucksacks:
    elfGroup += (" " + ruckSack)
    numberInGroup += 1
    if numberInGroup == maxNumberPerGroup:
        elfGroup = elfGroup.replace("\n", "")
        elfGroup = elfGroup.strip()
        allElfGroups.append(elfGroup)
        elfGroup = ""
        numberInGroup = 0

for group in allElfGroups:
    ruckSacks = group.rsplit(" ")
    trimmedRuckSacks = []
    foundInXGroups = 1
    duplicateItemFound = False
    # Remove duplicates, make a trimmed list per group
    for ruckSack in ruckSacks:
        ruckSack = [i for i in ruckSack]
        ruckSack = list(dict.fromkeys(ruckSack))
        trimmedRuckSacks.append(ruckSack)

    # Iterating through the first ruckSack, increases a flag (foundInXGroups) that indicates if
    # item is duplicated and immediately looks at next rucksack. When flag is equal to amount 
    # of rucksacks in group, that item is the confirmed duplicate and the search stops for said
    # group and we move on to the next group (back to line 26). If item is not a duplicate,
    # iteration for said item breaks, all flags reset, and we move on to next item.
    for item in trimmedRuckSacks[0]:
        if duplicateItemFound == True:
            break
        for index in range(maxNumberPerGroup-1):
            if trimmedRuckSacks[(index+1)].count(item) > 0:
                foundInXGroups += 1
                if foundInXGroups == maxNumberPerGroup:
                    duplicatedItems.append(item)
                    duplicateItemFound = True
            else:
                foundInXGroups = 1
                break

# Use ASCII values to avoid making maps for letter values
for item in duplicatedItems:
    if item.islower():
        sumOfGroupCommonItem += (ord(item)-96)
    if item.isupper():
        sumOfGroupCommonItem += (ord(item)-38)

print(duplicatedItems)
print(sumOfGroupCommonItem)