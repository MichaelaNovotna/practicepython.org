while True: 
    hracA = input("Player A, enter your play: ").lower()
    hracB = input("Player B, enter your play: ").lower()

    if hracA == hracB:
        print("It's a draw!")
    elif (hracA == "rock" or hracB == "rock") and (hracA == "paper" or hracB == "paper"):
        print("Paper beats rock!")
    elif hracA == "rock" or hracB == "rock" and (hracA == "scissors" or hracB == "scissors"):
        print("Rock beats scissors!")
    elif (hracA == "scissors" or hracB == "scissors") and (hracA == "paper" or hracB == "paper"):
        print("Scissors beats paper!")
    else:
        print("I didn't understand!")
    if input("Do you want to play again? ").lower() != "yes":
        break
