def give_me_num():
    return int(input("How many numbers of Fibonacci? "))


def generate(celkem):
    if celkem == 0:
        list = []
    if celkem == 1:
        list = [1]
    elif celkem > 1:
        list = [1, 1]
        for i in range(1, celkem-1):
            cislo = list[-1] + list[-2]
            list.append(cislo)
    return list


print(generate(give_me_num()))

