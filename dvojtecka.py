a = [1, 2, 3, 4, 5, 6]
# pozpátku
b = a[5:0:-1] # problém: není tam první číslo (1) na nulté pozici
print(b)

c = a[5::-1] # anebo jen a[::-1]
print(c)