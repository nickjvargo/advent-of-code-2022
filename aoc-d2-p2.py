#! python
# A, X = Rock, Lose; B, Y = Paper, Draw; C, Z = Scissors, Win
rock = ["B X", "A Y", "C Z"]
paper = ["C X", "B Y", "A Z"]
scissors = ["A X", "C Y", "B Z"]
totalScore = 0

cheatSheet = open("./inputs/aoc-d2.txt")

def lossDrawWin(number):
    if number == 0:
        return 0
    if number == 1:
        return 3
    if number == 2:
        return 6

for line in cheatSheet:
    # Necesarry as last line has no \n, all others do
    if line.endswith("\n"):
        roundOfGame = line[:-1]
    else:
        roundOfGame = line
    

    if rock.count(roundOfGame) == 1:
        totalScore += 1 + (lossDrawWin(rock.index(roundOfGame)))
    elif paper.count(roundOfGame) == 1:
        totalScore += 2 + (lossDrawWin(paper.index(roundOfGame)))
    else:
        totalScore += 3 + (lossDrawWin(scissors.index(roundOfGame)))

cheatSheet.close()

print("Total score = %s" % totalScore)