slovo = input("Zadejte slovo: ")
listpismen = []

for i in range(1, len(slovo) + 1):
    if slovo[i - 1] == slovo[-i]:  # pokud se písmeno z jedné strany shoduje s tím z druhé strany
        listpismen.append(slovo[i - 1])  # pridej ho do listu pismen
        palindrom = "".join(listpismen)  # a pak z nej udelej string
        if i == len(slovo):  # pokud je tohle posledni pismeno
            print("Slovo '" + palindrom + "' je palindrom.")  # vytiskni zaverecnou zpravu
    else:
        print("Slovo '" + slovo + "' není palindrom.")
        break

# NEBO

wrd = input("Please enter a word: ")
wrd = str(wrd)
rvs = wrd[::-1]
print(rvs)
if wrd == rvs:
    print("This word is a palindrome")
else:
    print("This word is not a palindrome")


# NEBO

def reverse(word):
    x = ''
    for i in range(len(word)):
        x += word[len(word) - 1 - i]
    return x


word = input('give me a word:\n')
x = reverse(word)
if x == word:
    print('This is a Palindrome')
else:
    print('This is NOT a Palindrome')
