a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = []

for element in a:
    if element in b and element not in c:
        c.append(element)
print(c)


# za pomoci alespoň jedné list comprehension
cc = [element for element in a if element in b] # problém: nevylučuje to opakující se čísla, takže přidám:
cc2 = []
for element in cc:
    if element not in cc2:
        cc2.append(element)
print(cc2)                          # je to řešení za pomoci alespoň jedné list comprehension, ale ve výsledku delší

#anebo za použití set(a)
result = [element for element in set(a) if element in b]
print(result)


# EXTRA
import random
 
a = random.sample(range(1,30), 16)
b = random.sample(range(1,30), 12)
result1 = [element for element in set(a) if element in b]
result2 = [element for element in result1 if result1.count(element) == 1] # ofiko řešení ale myslím, že zbytečný řádek
print(result2)

# anebo za použití set(a)
result3 = [element for element in set(a) if element in b]
print(result3)