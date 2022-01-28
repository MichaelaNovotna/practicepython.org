def veta():
    return input("Give me a sentence. ")


def reverse_sentence(veta):
    veta = str(veta).split(" ")
    nova = [veta[-slovo] for slovo in range(1, len(veta)+1)]    # nebo níže za pomocí for cyklu
    nova = " ".join(nova)
    return nova


print(reverse_sentence(veta()))
    
# anebo za pomocí for cyklu
#   nova = []
#   for i in range(1, len(veta)+1):
#       nova.append(veta[-i])

# anebo
def reverse_sentence2(veta):
    return " ".join(str(veta).split()[::-1])


print(reverse_sentence2(veta()))