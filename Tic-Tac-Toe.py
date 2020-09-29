#Stage 2/5: The user is the gamemaster
field = input("Enter cells:")
field_fringe = "---------"

print(field_fringe)
print('|', field[0], field[1], field[2], '|')
print('|', field[3], field[4], field[5], '|')
print('|', field[6], field[7], field[8], '|')
print(field_fringe)

#stage 3/5: What's up on the field?
input = input("Enter cells")
print("---------")
print("| " + input[0] + " " + input[1] + " " + input[2] + " |")
print("| " + input[3] + " " + input[4] + " " + input[5] + " |")
print("| " + input[6] + " " + input[7] + " " + input[8] + " |")
print("---------")


def isWinner(bo, le):
    return ((bo[0] == le and bo[1] == le and bo[2] == le) or  # across the top

            (bo[3] == le and bo[4] == le and bo[5] == le) or  # across the middle

            (bo[6] == le and bo[7] == le and bo[8] == le) or  # across the bottom

            (bo[0] == le and bo[3] == le and bo[6] == le) or  # down the left side

            (bo[1] == le and bo[4] == le and bo[7] == le) or  # down the middle

            (bo[2] == le and bo[5] == le and bo[8] == le) or  # down the right side

            (bo[0] == le and bo[4] == le and bo[8] == le) or  # diagonal

            (bo[2] == le and bo[4] == le and bo[6] == le))  # diagonal
o_num = 0
x_num = 0
for i in range(0, 9):
    if input[i] == "X":
        x_num += 1
    if input[i] == "O":
        o_num += 1
if isWinner(input, 'X') and isWinner(input, 'O') or not isWinner(input, 'X') and not isWinner(input, 'O') and abs(x_num - o_num) >= 2:
    print("Impossible")
elif isWinner(input, 'X') and not isWinner(input, 'O'):
    print("X wins")
elif isWinner(input, 'O') and not isWinner(input, 'X'):
    print("O wins")
elif "_" not in input:
    print("Draw")
elif not isWinner(input, 'X') or not isWinner(input, 'O'):
    if "_" in input:
        print("Game not finished")