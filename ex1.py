import datetime
now = datetime.datetime.now()

name = input("What is your name? ")
vek = input("how old are you? ")

year = now.year - int(vek) + 100

vysledek = name + ", you will be 100 in " + str(year - 1) + " or " + str(year) + ". "
print(vysledek)

opakovani = int(input("Give me another number: "))

print(opakovani * vysledek)

for i in range(opakovani):
    print(vysledek)