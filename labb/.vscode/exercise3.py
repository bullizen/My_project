word = input('Enter word ')
print("Original sträng:", word)

size = len(word)

print("Skriver bara jämna bokstäver")
for i in range(0, size - 1, 2):
    print("index[", i, "]", word[i])