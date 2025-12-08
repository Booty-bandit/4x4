empty = "."
player1 = "0"
player2 = "X"

row = 5
collum = 5
board = []

""" board =    [[empty, empty, empty, empty], 
            [empty, empty, empty, empty], 
            [empty, empty, empty, empty], 
            [empty, empty, empty, empty]] """

def generate_board (row, collum):
    for row in range(row):
        board.append([])
        for x in range(collum):
            board[row].append(0)

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
    #counts the number of x's or y's in a row and resets the wincon_counter if there is a new type
    current_wincon = ""
    wincon_counter = 0
    for y in range(collum):
        for num in range(row):
            if board[y][num] != current_wincon:
                wincon_counter = 0
            if board[y][num] == "x":
                wincon_counter +=1
                current_wincon = "x"
            elif board[y][num] == "y":
                wincon_counter +=1
                current_wincon = "y"
            if wincon_counter == 4:
                print(f"{current_wincon} has won")

def check_collum_wincon(board,collum):
    current_wincon = ""
    wincon_counter = 0
    for x in range(row):
        for num in range(collum):
            if board[num][x] != current_wincon:
                wincon_counter = 0
            if board[num][x] == "x":
                wincon_counter += 1
                current_wincon = "x"
            elif board[num][x] == "y":
                wincon_counter += 1
                current_wincon = "y"
            if wincon_counter == 4:
                print(f"{current_wincon} has won")


def check_for_win(player):
    #Check rows
    check_row_wincon(board, row)

    #Check columns
    check_collum_wincon(board, collum)

    #Check diagonal 1

    #Check diagonal 2
    pass 

def game_loop():
    
    print_board()
    while True:
        
        user_inp = int(input("Player 1 >"))-1
        mark(user_inp, player1)
        print_board()
            
game_loop()