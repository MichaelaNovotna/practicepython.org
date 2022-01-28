number = int(input("Give me a number: "))
divided = number % 2
if divided == 0:
    print("This number is even.")
else:
    print("This number is odd.")
    
divided4 = number % 4
if divided4 == 0:
    print("This number is multiple of 4.")
else:
    print("This number is not a multiple of 4.")
