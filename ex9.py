import random

znova = True
while znova:
    a = random.randint(0, 9)
    pokusu = 0
    while True:
        b = int(input("Guess a number between 0 and 9: "))
        if a == b:
            print("That is correct! You tried " + str(pokusu) + " times.")
            if input("Do you want to play again? ") != "yes":
                znova = False
            break
        elif a > b:
            print("Too low!")
            pokusu += 1
        elif a < b:
            print("Too high!")
            pokusu += 1
