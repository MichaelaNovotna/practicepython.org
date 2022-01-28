def dej_mi_cislo():
    return int(input("Dej mi číslo: "))


def je_prvocislo(cislo):
    if cislo > 1:
        list = []
        for delitel in range(2, cislo):
            if cislo % delitel == 0:
                list.append(delitel)
        if list == []:
            print("Je to prvočíslo!")
        else:
            print("Není to prvočíslo!")
    else:
        print("Není to prvočíslo!")


je_prvocislo(dej_mi_cislo())


# zkráceně

def dej_mi_cislo2():
    return int(input("Dej mi číslo: "))


def je_prvocislo2(cislo):
    if cislo > 1:
        if [delitel for delitel in range(2, cislo) if cislo % delitel == 0] == []:
            print("Je to prvočíslo!")
        else:
            print("Není to prvočíslo!")
    else:
        print("Není to prvočíslo!")


je_prvocislo2(dej_mi_cislo2())
