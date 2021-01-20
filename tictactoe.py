def playing_field():
    print("Welcome to Tic Tac Toe")
    print("######################")
    row1 = [' ', ' ', ' ']
    row2 = [' ', ' ', ' ']
    row3 = [' ', ' ', ' ']
    moves = 0
    first = 'NO'
    display(row1, row2, row3)
    while moves < 9 and first == 'NO':
        while moves % 2 == 0 and first == 'NO':
            print("Player 1's Turn")
            player_move = user_input()
            if confirm_pos(player_move[0], player_move[1], row1, row2, row3):
                apply_move(player_move[0], player_move[1], 'X', row1, row2, row3)
            else:
                break
            first = check_match(row1, row2, row3)
            display(row1, row2, row3)
            moves += 1
        while moves % 2 != 0 and first == 'NO':
            print("Player 2's Turn")
            player_move = user_input()
            if confirm_pos(player_move[0], player_move[1], row1, row2, row3):
                apply_move(player_move[0], player_move[1], 'O', row1, row2, row3)
            else:
                break
            first = check_match(row1, row2, row3)
            display(row1, row2, row3)
            moves += 1

    if first == 'NO' and moves == 9:
        print('A winner could not be decided, regroup and re-engage')
    elif first == 'P1':
        print('Well done Player 1! You are truly worthy!')
        print('Player 2 get good!')
    elif first == 'P2':
        print('A worthy opponent has been found! Player 2!')
        print('Player 1, please re-evaluate your life choices')


def display(row1, row2, row3):
    print(*row1, sep=' | ')
    print('---------')
    print(*row2, sep=' | ')
    print('---------')
    print(*row3, sep=' | ')


def user_input():
    print("All values are between 1 and 3")
    row = int(input("Select a row: "))
    while row not in range(1, 4):
        row = int(input("Select a row: "))
    index = int(input("Select a index: "))
    while index not in range(1, 4):
        index = int(input("Select a index: "))
    move = [row, (index-1)]

    return move


def check_match(row1, row2, row3):
    first_check = perfect_match(row1, row2, row3)
    sec_check = straight_match(row1, row2, row3)
    third_check = diagonal_match(row1, row2, row3)

    if (first_check == 'O') or (sec_check == 'O') or (third_check == 'O'):
        return 'P2'
    elif (first_check == 'X') or (sec_check == 'X') or (third_check == 'X'):
        return 'P1'
    else:
        return 'NO'


def perfect_match(row1, row2, row3):
    perfect_o = ['O', 'O', 'O']
    perfect_x = ['X', 'X', 'X']
    if (row1 == perfect_o) or (row2 == perfect_o) or (row3 == perfect_o):
        return 'O'
    elif (row1 == perfect_x) or (row2 == perfect_x) or (row3 == perfect_x):
        return 'X'
    else:
        return 'NO'


def straight_match(row1, row2, row3):
    for num in range(4):
        if (row1[num] == 'O') and (row2[num] == 'O') and (row3[num] == 'O'):
            return 'O'
        elif (row1[num] == 'X') and (row2[num] == 'X') and (row3[num] == 'X'):
            return 'X'
        else:
            return 'NO'


def diagonal_match(row1, row2, row3):
    if (row1[0] == 'O') and (row2[1] == 'O') and (row3[2] == 'O'):
        return 'O'
    elif (row3[0] == 'O') and (row2[1] == 'O') and (row1[2] == 'O'):
        return 'O'
    elif (row1[0] == 'X') and (row2[1] == 'X') and (row3[2] == 'X'):
        return 'X'
    elif (row3[0] == 'X') and (row2[1] == 'X') and (row1[2] == 'X'):
        return 'X'
    else:
        return 'NO'


def apply_move(row, index, player, row1, row2, row3):
    re = confirm_pos(row, index, row1, row2, row3)
    if re:
        if row == 1:
            row1[index] = player
            return row1
        elif row == 2:
            row2[index] = player
            return row2
        elif row == 3:
            row3[index] = player
            return row3
    else:
        print("Values provided don't comply with empty spaces")


def confirm_pos(row, index, row1, row2, row3):
    if row == 1:
        if row1[index] != " ":
            return False
        else:
            return True
    elif row == 2:
        if row2[index] != " ":
            return False
        else:
            return True
    elif row == 3:
        if row3[index] != " ":
            return False
        else:
            return True


def execute():
    ask = input("Do you want to play the game Y/N ? : ")
    ask = ask.upper()
    my_options = ['Y', 'N']
    while ask not in my_options:
        ask = input("Did you even read? Y for Yes , N for No: ".upper())
    if ask == 'Y':
        playing_field()
        execute()
    elif ask == 'N':
        pass


if __name__ == "__main__":
    execute()