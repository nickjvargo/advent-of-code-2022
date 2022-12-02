#! python
# A, X = Rock; B, Y = Paper; C, Z = Scissors
win = ["C X", "A Y", "B Z"]
loss = ["B X", "C Y", "A Z"]
draw = ["A X", "B Y", "C Z"]
totalScore = 0

cheatSheet = open("./inputs/aoc-d2.txt")

for line in cheatSheet:
    # Necesarry as last line has no \n, all others do
    if line.endswith("\n"):
        roundOfGame = line[:-1]
    else:
        roundOfGame = line
    
    if win.count(roundOfGame) == 1:
        totalScore += 6 + (win.index(roundOfGame) + 1)
    elif loss.count(roundOfGame) == 1:
        totalScore += 0 + (loss.index(roundOfGame) + 1)
    else:
        totalScore += 3 + (draw.index(roundOfGame) + 1)

cheatSheet.close()

print("Total score = %s" % totalScore)