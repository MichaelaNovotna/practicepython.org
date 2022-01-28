a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = []

for element in a:
    if element in b and element not in c:
            c.append(element)
print(c)


# anebo za pomocí sets
aa = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
bb = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]


def prunik(frst_lst, scnd_lst):
    cc = []
    for element in frst_lst:
        if element in scnd_lst:
            cc.append(element)
    cc = set(cc)
    return cc


print(prunik(aa, bb))


# a extra za pomocí list comprehension
aa = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
bb = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]


def prunik(frst_lst, scnd_lst):
    cc = [element for element in frst_lst if element in scnd_lst]
    cc = set(cc)
    return cc


print(prunik(aa, bb))