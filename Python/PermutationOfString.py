list = []


def swap(str, i, j):
    letter = [i for i in str]

    temp = letter[i]
    letter[i] = letter[j]
    letter[j] = temp

    word = ""
    for i in letter:
        word = word+i

    return word


def permutation(str, i):
    if i >= len(str):
        list.append(str)
        return

    for j in range(i, len(str)):
        str = swap(str, i, j)
        permutation(str, i+1)
        str = swap(str, i, j)


str = input("Enter the word ")

permutation(str, 0)

for word in list:
    print(word)
