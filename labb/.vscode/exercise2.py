# Write a program to accept a string from the user and display characters that are present at an even index number.

# For example, str = "pynative" so you should display ‘p’, ‘n’, ‘t’, ‘v’.

ordet = input("Skriv ett ord")
print("Orginalsträng:", ordet)

size = len(ordet)

print("Skriver bara konsonanter")
for a in range(0, size - 1, 2):
    print("index[", a, "]", ordet[a]")