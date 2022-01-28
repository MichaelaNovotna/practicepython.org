cislo = int(input("Zadejte číslo: "))
list = []
for i in range(1, cislo+1):
    if cislo % i == 0:
        list.append(i)
print(list)

# anebo
cislo2 = int(input("Zadejte další číslo: "))
list2 = [number for number in range(1, cislo2 + 1) if cislo2 % number == 0]
print(list2)
