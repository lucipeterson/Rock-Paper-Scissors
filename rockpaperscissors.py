#rockpaperscissors.py
import random

print("~~ Rock, Paper, Scissors ~~")
weapon_list = ["rock", "paper", "scissors"]
user = input("Rock, paper, or scissors? ")
while user.lower() not in weapon_list:
    user = input("Rock, paper, or scissors? ")

computer = random.choice(weapon_list)
print("Computer chooses " + computer + ".")
if computer == "rock":
    if user.lower() == "rock":
        print("It's a tie!")
    elif user.lower() == "paper":
        print("Paper smothers rock.  You win!")
    elif user.lower() == "scissors":
        print("Rock crushes scissors.  You lose.")
if computer == "paper":
    if user.lower() == "rock":
        print("Paper smothers rock.  You lose.")
    elif user.lower() == "paper":
        print("It's a tie!")
    elif user.lower() == "scissors":
        print("Scissors cut paper.  You win!")
if computer == "scissors":
    if user.lower() == "rock":
        print("Rock crushes scissors.  You win!")
    elif user.lower() == "paper":
        print("Scissors cut paper.  You lose.")
    elif user.lower() == "scissors":
        print("It's a tie!")

again = input("Play again? ")
while again.lower() == "yes":
        user = input("Rock, paper, or scissors? ")
        while user.lower() not in weapon_list:
                user = input("Rock, paper, or scissors? ")

        computer = random.choice(weapon_list)
        print("Computer chooses " + computer + ".")
        if computer == "rock":
            if user.lower() == "rock":
                print("It's a tie!")
                again = input("Play again? ")
            elif user.lower() == "paper":
                print("Paper smothers rock.  You win!")
                again = input("Play again? ")
            elif user.lower() == "scissors":
                print("Rock crushes scissors.  You lose.")
                again = input("Play again? ")
        if computer == "paper":
            if user.lower() == "rock":
                print("Paper smothers rock.  You lose.")
                again = input("Play again? ")
            elif user.lower() == "paper":
                print("It's a tie!")
                again = input("Play again? ")
            elif user.lower() == "scissors":
                print("Scissors cut paper.  You win!")
                again = input("Play again? ")
        if computer == "scissors":
            if user.lower() == "rock":
                print("Rock crushes scissors.  You win!")
                again = input("Play again? ")
            elif user.lower() == "paper":
                print("Scissors cut paper.  You lose.")
                again = input("Play again? ")
            elif user.lower() == "scissors":
                print("It's a tie!")
                again = input("Play again? ")

if again.lower() != "yes":
    print("Game Over")
