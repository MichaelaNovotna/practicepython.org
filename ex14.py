def remove_duplicates(seznam):
    return set(seznam)


print(remove_duplicates([1, 1, 2, 3, 4, 4, 5]))


# anebo delší
def remove_duplicates2(seznam):
    seznam2 = []
    for i in seznam:
        if i not in seznam2:
            seznam2.append(i)
    return seznam2


print(remove_duplicates2([1, 1, 2, 3, 4, 4, 5]))