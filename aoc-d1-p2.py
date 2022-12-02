#! python
listOfSnackBags = open("./inputs/aoc-d1.txt")
elvesSnackBagArray = []
elfSnackBag = 0
biggestThreeSnackBagsCombined = 0

for line in listOfSnackBags:
    if line != "\n":
        elfSnackBag += int(line)
    else:
        elvesSnackBagArray.append(elfSnackBag)
        elfSnackBag = 0

listOfSnackBags.close()

#Necessary to add last snack bag, as the file does not end in \n
elvesSnackBagArray.append(elfSnackBag)
elvesSnackBagArray.sort(reverse=True)
biggestThreeSnackBagsCombined = elvesSnackBagArray[0] + elvesSnackBagArray[1] + elvesSnackBagArray[2]

print("Biggest three bags of snacks combined = %s" % biggestThreeSnackBagsCombined)