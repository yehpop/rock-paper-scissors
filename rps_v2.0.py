__author__ = "Yusa Erenci"

import random

lose = "The Computer Wins"
win = "You Win!"
lives = 5
score = 0
drew = 0
compLives = 7
passwordList = []


# I am adding functions here cause it makes it neat
def loseFunc(computer, lose):
    print("The computer chose", computer)
    print(" ")
    print(lose)
    print(" ")
    global lives
    lives = lives - 1


def winFunc(computer, win):
    print("The computer chose", computer)
    print(" ")
    print(win)
    print(" ")
    global compLives
    compLives = compLives - 1
    global lives
    lives = lives + 1
    global score
    score = score + 1


def drawFunc(computer):
    global drew
    drew = drew + 1
    print("The computer chose", computer)
    print("  \nYou Drew\n  ")


while 1 > 0:
    print("To begin fill in the below info.")
    username = input("Please enter your username: ")
    password = input("Please enter your password: ")
    searchFile = open("accounts.txt", "r")
    for line in searchFile:
        passwordList.append(line.strip())
        if username + " , " + password in passwordList:
            print("Access Granted")
            print("____________")
            print("        ROCK PAPER SCISSORS")
            print("------------------------------------")
            print("RULES")
            print(
                "You start with 5 lives\nIf you win you get an extra life\nIf you lose you lose a "
                "life\nIf you draw your lives stay the same\n'r' for rock, 'p' for paper and 's' for scissors\nDon't use capitols\n you can type exit at "
                "anytime to leave the game")
            print("--------------------------------------------")
            print("The computers also got lives\nGood Luck!")
            print("--------------------------------------------")
            while True:
                rps = input("rock, paper, scissors?  ")
                computer = ("rock", "paper", "scissors")
                computer = random.choice(computer)

                # rock if
                if rps == "r" and computer == "paper":
                    loseFunc("paper", lose)
                if rps == "r" and computer == "scissors":
                    winFunc("scissors", win)

                # paper if
                if rps == "p" and computer == "scissors":
                    loseFunc("scissors", lose)
                if rps == "p" and computer == "rock":
                    winFunc("rock", win)

                # scissors if
                if rps == "s" and computer == "rock":
                    loseFunc("rock", lose)
                if rps == "s" and computer == "paper":
                    winFunc("paper", win)

                # draw if
                if rps == "r" and computer == "rock":
                    drawFunc("rock")
                if rps == "s" and computer == "scissors":
                    drawFunc("scissors")
                if rps == "p" and computer == "paper":
                    drawFunc("paper")

                # things I used to check if codes work
                if rps == "display lives":
                    print(lives)
                if rps == "display score":
                    print("Your current score:", score)
                if rps == "display draws":
                    print("You've drawed", drew, "times")

                # lives
                if lives == 0 or rps == "test":
                    print(
                        "Thanks for playing.\nYou've ran out of lives\nYou won",
                        score, "times.\nYou've drawn", drew, "times", drew)
                    stop = input("Press any key to exit.")
                    exit()
                if compLives == 0:
                    print(
                        "Thanks for playing.\nYou've defeated the computer\nYou won",
                        score, "times.\nYou've drawn", drew, "times")
                    stop = input("Press any key to exit.")
                    exit()

                # end
                if rps == "exit":
                    break
        else:
            print("Access Denied\nYour username or password is incorrect.")
            print("Sign up if you haven't already")
