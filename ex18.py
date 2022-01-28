import random


def generator():
    generated_num = [random.randint(0, 9) for number in range(4)]
    return generated_num


def correct_place(user_num, generated_num):
    cows = 0
    for i in range(4):
        if user_num[i] == generated_num[i]:
            cows += 1
    return cows

    
def wrong_place(user_num, generated_num, cows):
    bulls = 0
    uzbylo = []
    for i in range(4):
        if user_num[i] not in uzbylo:
            if generated_num.count(user_num[i]) == user_num.count(user_num[i]):
                bulls += generated_num.count(user_num[i])
            elif user_num[i] in generated_num:
                bulls += 1
        uzbylo.append(user_num[i])
    bulls = bulls - cows
    if bulls >= 0:
        return bulls
    else:
        return 0


def vyhodnot():
    pokusu = 1
    while True:
        user_num = str(input("Guess a 4-digit number: "))
        num_of_cows = correct_place(user_num, generated_num)
        num_of_bulls = wrong_place(user_num, generated_num, num_of_cows)
        if num_of_cows == 4:
            print("Congrats! You have 4 cows. You tried " + str(pokusu) + " times." )
            break
        else:
            print("You have " + str(num_of_cows) + " cow(s) and " + str(num_of_bulls) + " bull(s).")
        pokusu += 1

# VSTUPY
generated_num = generator()
generated_num = str("".join([str(i) for i in generated_num]))
vyhodnot()


    

