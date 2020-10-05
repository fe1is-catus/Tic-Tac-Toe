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

#stage 4/5: First move!
symbols = input("Enter cells:")


print('---------')
print('|', symbols[0], symbols[1], symbols[2], '|')
print('|', symbols[3], symbols[4], symbols[5], '|')
print('|', symbols[6], symbols[7], symbols[8], '|')
print('---------')


while True:
    coord = input('Enter the coordinates: ')

    if coord.isalpha():
        print("You should enter numbers!")
        pass

    else:
        coord_col, coord_row = coord.split()
        coord_x = int(coord_col) - 1
        coord_y = 3 - int(coord_row)
        index = (coord_y * 3) + coord_x

        if index <= 8:

            if 1 <= int(coord_col) <= 3 and 1 <= int(coord_row) <= 3:

                if symbols[index] != '_':
                    print("This cell is occupied! Choose another one!")
                    pass

                else:

                    for j in range(len(symbols)):
                        symbols = [i for i in symbols]
                        if symbols[index] == '_':
                            symbols[index] = 'X'
                            print('---------')
                            print('|', symbols[0], symbols[1], symbols[2], '|')
                            print('|', symbols[3], symbols[4], symbols[5], '|')
                            print('|', symbols[6], symbols[7], symbols[8], '|')
                            print('---------')
                            break

                    break
            else:
                print("Coordinates should be from 1 to 3!")
                pass

        else:
            print("Coordinates should be from 1 to 3!")
            pass

#stage 5/5: Fight!

def check_row(list_):
    new_list = []
    for i in range(3):
        if list_[i][0] == list_[i][1] == list_[i][2]:
            if list_[i][0] != ' ':
                new_list.append(list_[0][i])
    return new_list


def check_column(list_):
    new_list = []
    for i in range(3):
        if list_[0][i] == list_[1][i] == list_[2][i]:
            if list_[0][i] != ' ':
                new_list.append(list_[0][i])
    return new_list


def check_diagonal(list_):
    new_list = []
    if list_[0][0] == list_[1][1] == list_[2][2] or list_[2][0] == list_[1][1] == list_[0][2]:
        if list_[1][1] != ' ':
            new_list.append(list_[1][1])
    return new_list

tic_tac_toe = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
t_t_t = [[tic_tac_toe[0], tic_tac_toe[1], tic_tac_toe[2]],
         [tic_tac_toe[3], tic_tac_toe[4], tic_tac_toe[5]],
         [tic_tac_toe[6], tic_tac_toe[7], tic_tac_toe[8]]]


def t_t_t_print():
    print(f'''---------
| {t_t_t[0][0]} {t_t_t[0][1]} {t_t_t[0][2]} |
| {t_t_t[1][0]} {t_t_t[1][1]} {t_t_t[1][2]} |
| {t_t_t[2][0]} {t_t_t[2][1]} {t_t_t[2][2]} |
---------''')

winner = check_column(t_t_t) + check_row(t_t_t) + check_diagonal(t_t_t)
t_t_t_print()

while True:
    winner = check_column(t_t_t) + check_row(t_t_t) + check_diagonal(t_t_t)
    moves = 0
    coords = input('Enter the coordinates: ')
    y, x = coords.split()
    if not (x.isdigit() and y.isdigit()):
        print('You should enter numbers!')
        continue
    if int(x) not in range(1, 4) or int(y) not in range(1, 4):
        print('Coordinates should be from 1 to 3!')
        continue
    y = int(y) - 1
    x = 3 - int(x)
    if t_t_t[x][y] == ' ' and moves % 2 == 0:
        t_t_t[x][y] = 'X'
        t_t_t_print()
        if abs(tic_tac_toe.count('X') - tic_tac_toe.count('O')) > 1:
            print('Impossible')
            break
        elif len(winner) > 1:
            print('Impossible')
            break

        elif len(winner) == 0 and ' ' not in tic_tac_toe:
            print('Draw')
            break
        elif winner:
            print(f'{winner[0]} wins')
            break
    elif t_t_t[x][y] == ' ' and moves % 2 == 1:
        t_t_t[x][y] = 'O'
        t_t_t_print()
        if abs(tic_tac_toe.count('X') - tic_tac_toe.count('O')) > 1:
            print('Impossible')
            break
        elif len(winner) > 1:
            print('Impossible')
            break
        
        elif len(winner) == 0 and ' ' not in tic_tac_toe:
            print('Draw')
            break
        elif winner:
            print(f'{winner[0]} wins')
            break
    else:
        print('This cell is occupied! Choose another one!')
