a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
b = []

for cislo in a:
    if cislo % 2 == 0:
        b.append(cislo)
        
print(b)

# nebo jednořádkově

c = [cislo for cislo in a if cislo % 2 == 0]
print(c)
