# [
#    [], rad1
#    [], rad2
#    [], rad3
# ]

tictactoe = [[" ", " ", " "], [" ", " ", "X"], [" ", " ", " "]]

print("Fore")
for rad in tictactoe:
    print (rad)

pos = tictactoe[1][2]
tictactoe[1][2] = '0'

print('Efter')
for rad in tictactoe:
    print(rad)