# backup
def check():
    if board[0][0] == "X" and board[0][1] == 'X' and board[0][2] == 'X':
        print("X wins")
        return 1
    if board[1][0] == "X" and board[1][1] == 'X' and board[1][2] == 'X':
        print('X wins')
        return 1
    if board[2][0] == "X" and board[2][1] == 'X' and board[2][2] == 'X':
        print('X wins')
        return 1

    if board[0][0] == "X" and board[1][0] == 'X' and board[2][0] == 'X':
        print('X wins')
        return 1
    if board[0][1] == "X" and board[1][1] == 'X' and board[2][1] == 'X':
        print('X wins')
        return 1

    if board[0][2] == "X" and board[1][2] == 'X' and board[2][2] == 'X':
        print('X wins')
        return 1
    if board[0][0] == "X" and board[1][1] == 'X' and board[2][2] == 'X':
        print('X wins')
        return 1
    if board[2][2] == "X" and board[1][1] == 'X' and board[0][0] == 'X':
        print('X wins')
        return 1
    if board[0][2] == "X" and board[1][1] == 'X' and board[0][0] == 'X':
        print('X wins')
    if board[0][0] == "X" and board[0][1] == 'X' and board[0][2] == 'X':
        print('X wins')
        return 1
    if board[0][2] == "X" and board[1][1] == 'X' and board[2][0] == 'X':
        print('X wins')
        return 1
    #

    if board[0][0] == "O" and board[0][1] == 'O' and board[0][2] == 'O':
        print('O wins')
        return 1
    if board[1][0] == "O" and board[1][1] == 'O' and board[1][2] == 'O':
        print('O wins')
        return 1
    if board[2][0] == "O" and board[2][1] == 'O' and board[2][2] == 'O':
        print('O wins')
        return 1

    if board[0][0] == "O" and board[1][0] == 'O' and board[2][0] == 'O':
        print('O wins')
        return 1
    if board[0][1] == "O" and board[1][1] == 'O' and board[2][1] == 'O':
        print('O wins')
        return 1

    if board[0][2] == "O" and board[1][2] == 'O' and board[2][2] == 'O':
        print('O wins')
        return 1
    if board[0][0] == "O" and board[1][1] == 'O' and board[2][2] == 'O':
        print('O wins')
        return 1
    if board[2][2] == "O" and board[1][1] == 'O' and board[0][0] == 'O':
        print('O wins')
        return 1

    if board[0][2] == "O" and board[1][1] == 'O' and board[2][0] == 'O':
        print('O wins')
        return 1

        # if board[2][2] == "X" and board[1][1] == 'X' and board[0][0] == 'X':
        #     print('X wins')
        #     return 1

    # if board['7'] == 'O' and board['8'] == 'O' and board['9'] == 'O':
    #     print('Player Two Won!!')
    #     return 1  # used to end the game
    # if board['4'] == 'O' and board['5'] == 'O' and board['6'] == 'O':
    #     print('Player Two Won!!')
    #     return 1
    # if board['1'] == 'O' and board['2'] == 'O' and board['3'] == 'O':
    #     print('Player Two Won!!')
    #     return 1
    # if board['7'] == 'O' and board['5'] == 'O' and board['3'] == 'O':
    #     print('Player Two Won!!')
    #     return 1
    # if board['1'] == 'O' and board['5'] == 'O' and board['9'] == 'O':
    #     print('Player Two Won!!')
    #     return 1
    # if board['7'] == 'O' and board['4'] == 'O' and board['1'] == 'O':
    #     print('Player Two Won!!')
    #     return 1
    # if board['8'] == 'O' and board['5'] == 'O' and board['2'] == 'O':
    #     print('Player Two Won!!')
    #     return 1
    # if board['9'] == 'O' and board['6'] == 'O' and board['3'] == 'O':
    #     print('Player Two Won!!')
    #     return 1
    return 0


# user_input = input("Enter cells: ")
# l = list(user_input)
player = 1
total_moves = 0
end_check = 0

board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]


def grid():
    print("---------")
    print(f"| {board[0][0]} {board[0][1]} {board[0][2]} |")
    print(f"| {board[1][0]} {board[1][1]} {board[1][2]} |")
    print(f"| {board[2][0]} {board[2][1]} {board[2][2]} |")
    print("---------")


grid()

while True:
    if total_moves == 9:
        print("Draw")
        exit()
    coor = input("Enter the coordinates: ")
    n = [x for x in coor.split() if x.isalpha()]
    if len(n) > 0:
        print("You should enter numbers!")
    else:
        row, col = coor.split()
        row, col = int(row), int(col)
        if row > 3 or col > 3:
            print("Coordinates should be from 1 to 3!")
            continue
        # elif board[row - 1][col - 1] == " ":
        #     board[row - 1][col - 1] = "X"
        #     grid()
        #     break

        # elif (coor.split().count("O") ==3 and coor.split().count("X")==3):
        #     print("draw")
        #     exit()
        elif board[row - 1][col - 1] != " ":
            print("This cell is occupied! Choose another one!")
            continue

        # end_check = check()
        # if total_moves == 9 or end_check == 1:
        #     break
        while total_moves<10:
            if player == 1:
                # p1_input = input('PLAYER ONE :')
                # coor
                # if row > 3 or col > 3:
                #     print("Coordinates should be from 4 to 3!")
                #     break
                if board[row - 1][col - 1] == " ":
                    board[row - 1][col - 1] = "X"
                    # board[p1_input.upper()] = 'X'
                    player = 2
                    grid()
                    end_check = check()
                    if end_check == 1:
                        exit()
                    break

                else:
                    print('Invalid input, please try again')
                    continue
            else:
                # if row > 3 or col > 3:
                #     print("Coordinates should be from 1 to 3!")
                #     break
                if board[row - 1][col - 1] == " ":
                    board[row - 1][col - 1] = "O"
                    player =1
                    grid()
                    end_check = check()
                    if end_check == 1:
                        exit()
                    break
                else:
                    print('Invalid input, please try again')
                    continue
    total_moves += 1
    print(total_moves)
# exit()
