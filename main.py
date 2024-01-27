import random

print("Welcome to number gessing game...")
def gameCont():
    print("I'm thinking of a number btw 1 to 100")


    diff = {"easy": 10, "hard": 5}

    difficulty = diff[input("Chose difficulty easy / hard:  \n")]

    guess = random.randint(0,100)
    print(guess)

    for x in range (difficulty):
        user = int (input("make a guess: "))
        if user > guess:
            print("Too High")
            print("Guess again")

        if user < guess:
            print("Too Low")
            print("Guess again")

        if user == guess:
            print(f"Congratulation, I was thinking {guess} ")
            break
        difficulty -= 1
        print(f"You have {difficulty} attempts remaining")

    shouldplay = input("Do you want to play again, press Y say yes, press N to say no:::  ")
    if shouldplay.lower() == "y":
        gameCont()
    else:
        print("Thank You for playing number guessing, have a nice day.")


gameCont()


''' this game was developed for learning purpose
I used for loop, functions, if else, recurssion, global/local variables to build this game
game runs on console.'''