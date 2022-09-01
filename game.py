# 1  3  5
# 9  11 13
# 17 19 21
board = "|1|2|3|\n|4|5|6|\n|7|8|9|"
board_pos = [1, 3, 5, 9, 11, 13, 17, 19, 21]


def display_board():
    print(board)


def player1_turn():
    global board
    pos = input("Player X, choose a position: ")
    if is_valid(pos):
        board = board.replace(pos, "X")
        display_board()
    else:
        print("Position not valid!")
        player1_turn()


def player2_turn():
    global board
    pos = input("Player O, choose a position: ")
    if is_valid(pos):
        board = board.replace(pos, "O")
        display_board()
    else:
        print("Position not valid!")
        player2_turn()


def is_valid(pos):
    for i in board_pos:
        if pos == board[i]:
            return True
    return False


def game_won():
    if board[1] == board[3] == board[5] or board[9] == board[11] == board[13] or board[17] == board[19] == board[
        21] or board[1] == board[9] == board[17] or board[3] == board[11] == board[19] or board[5] == board[13] == \
            board[21] or board[1] == board[11] == board[21] or board[5] == board[11] == board[17]:
        return True
    return False


def is_draw():
    for i in board_pos:
        if board[i] != 'X' and board[i] != 'O':
            return False
    return True


display_board()
while True:
    player1_turn()
    if game_won():
        print("player X wins!")
        break
    elif is_draw():
        print("Draw!")
        break
    player2_turn()
    if game_won():
        print("Player O wins!")
        break
    elif is_draw():
        print("Draw!")
        break
