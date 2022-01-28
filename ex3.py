a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

list = []
for cislo in a:
    if cislo < 5:
        list.append(cislo)
print(list)

# vše na jednom řádku
newlist = [element for element in a if int(element) < 5]
print(newlist)
