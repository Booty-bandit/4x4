empty = "."
player1 = "0"
player2 = "X"

row = 5
col = 5
board = []

""" board = [[empty, empty, empty, empty], 
            [empty, empty, empty, empty], 
            [empty, empty, empty, empty], 
            [empty, empty, empty, empty]] """

def generate_board (row, col):
    for row in range(row):
        board.append([])
        for i in range(col):
            board[row].append("0")

def print_board():
    print("| 1 | 2 | 3 | 4 |")
    print("| _ | _ | _ | _ |")
    for row in range(0, len(board)):
        for col in board[row]:
            print("| " + col, end = " ")
        print("|")
       
def mark(col, player):
    for row in board:
            row[col] = player

def check_row_wincon(board,row):
    #counts the number of P's or V's in a row and resets the wincon_counter if there is a new type
    current_wincon = ""
    wincon_counter = 0
    for V in range(col):
        for num in range(row):
            if board[V][num] != current_wincon:
                wincon_counter = 0
            if board[V][num] == player1:
                wincon_counter +=1
                current_wincon = player1
            elif board[V][num] == player2:
                wincon_counter +=1
                current_wincon = player2
            if wincon_counter == 4:
                print(f"{current_wincon} has won")

def check_collum_wincon(board,col):
    current_wincon = ""
    wincon_counter = 0
    for P in range(row):
        for num in range(col):
            if board[num][P] != current_wincon:
                wincon_counter = 0
            if board[num][P] == player1:
                wincon_counter += 1
                current_wincon = player1
            elif board[num][P] == player2:
                wincon_counter += 1
                current_wincon = player2
            if wincon_counter == 4:
                print(f"{current_wincon} has won")


def check_for_win(player):
    #Check rows
    check_row_wincon(board, row)

    #Check columns
    check_collum_wincon(board, col)

    #Check diagonal 1

    #Check diagonal 2
    pass 

def game_loop():
    generate_board(row,col)
    print_board()
    while True:
        
        user_inp = int(input("Player 1 >"))-1
        mark(user_inp, player1)
        print_board()
            
game_loop()