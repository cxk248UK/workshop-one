from random import random


def main():
    printIntro()
    probA, probB, n = getInput()
    winsA, winsB = simNGame(n, probA, probB)
    printSummary(winsA, winsB)


def printIntro():
    print("This is to simulate the racquetball game...")


def getInput():
    probA = float(input("What is the prob. Player A wins a serve: "))
    probB = float(input("What is the prob. Player B wins a serve: "))
    n = int(input("How many games to sim?: "))
    return probA, probB, n


def simNGame(n, probA, probB):
    winsA = 0
    winsB = 0

    for i in range(n):
        scoreA, scoreB = simOneGame(probA, probB)
        if scoreA > scoreB:
            winsA += 1
        else:
            winsB += 1

    return winsA, winsB


def simOneGame(probA, probB, serving="A", scoreA=0, scoreB=0):
    if not gameOver(scoreA, scoreB):
        if serving == "A":
            if random() < probA:
                scoreA += 1
            else:
                serving = "B"
        else:
            if serving == "B":
                if random() < probB:
                    scoreB += 1
                else:
                    serving = "A"
        return simOneGame(probA, probB, serving, scoreA, scoreB)
    return scoreA, scoreB


def gameOver(scoreA, scoreB):
    return scoreA == 15 or scoreB == 15


def printSummary(winsA, winsB):
    n = winsA + winsB
    print("Games simulated = ", n)
    print("Wins for A {0} ({1:0.1%}) ".format(winsA, winsA / n))
    print("Wins for B {0} ({1:0.1%}) ".format(winsB, winsB / n))


if __name__ == "__main__":
    main()
