empty = ".."
player1 = "🔴"
player2 = "🔵"

row = 6
col = 7
board = []

def generate_board (row, col):
    for row in range(row):
        board.append([])
        for i in range(col):
            board[row].append(empty)

def print_board(col):
    for i in range(col):
        print(f"| {i+1} ", end = " ")
    print("|")
    for j in range(col):
        print(f"| __", end = " ")
    print("|")
    for row in range(0, len(board)):
        for col in board[row]:
            print("| " + col, end = " ")
        print("|")
       
def mark(col, player):
    for row in range (len(board)-1,-1,-1):
           if board[row][col] == empty:
               board[row][col] = player
               return True
    print("there is no more room here")
    return False

def check_row_wincon(board,row):
    #counts the number of C's or R's in a row and resets the wincon_counter if there is a new type
    current_wincon = ""
    wincon_counter = 0
    for R in range(col):
        for num in range(row):
            if board[num][R] != current_wincon:
                wincon_counter = 0
            if board[num][R] == player1:
                wincon_counter +=1
                current_wincon = player1
            elif board[num][R] == player2:
                wincon_counter +=1
                current_wincon = player2
            if board[num][R] == empty:
                wincon_counter = 0
                current_wincon = ""
            if wincon_counter == 4:
                print(f"{current_wincon} has won row")
        wincon_counter = 0
        current_wincon = ""

def check_collum_wincon(board,col):
    current_wincon = ""
    wincon_counter = 0
    for C in range(row):
        for num in range(col):
            if board[C][num] != current_wincon:
                wincon_counter = 0
            if board[C][num] == player1:
                wincon_counter += 1
                current_wincon = player1
            elif board[C][num] == player2:
                wincon_counter += 1
                current_wincon = player2
            if board[C][num] == empty:
                wincon_counter = 0
                current_wincon = ""
            if wincon_counter == 4:
                print(f"{current_wincon} has won col")
        wincon_counter = 0
        current_wincon = ""

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
    print_board(col)
    while True:
        
        user_inp = int(input("Player 1 >"))-1
        mark(user_inp, player1)
        print_board(col)
        check_for_win(player1)
        user_inp = int(input("Player 2 >"))-1
        mark(user_inp,player2)
        print_board(col)
        check_for_win(player2)
               
game_loop()