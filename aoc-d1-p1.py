#! python
listOfSnackBags = open("./inputs/AOC-D1.txt")
elvesSnackBagArray = []
elfSnackBag = 0
biggestSnackBag = 0

for line in listOfSnackBags:
    if line != "\n":
        elfSnackBag += int(line)
    else:
        elvesSnackBagArray.append(elfSnackBag)
        elfSnackBag = 0

#Necessary to add last snack bag, as the file does not end in \n
elvesSnackBagArray.append(elfSnackBag)

for snackBag in elvesSnackBagArray:
    if snackBag > biggestSnackBag:
        biggestSnackBag = snackBag

print("Biggest bag of snacks - %s" % biggestSnackBag)