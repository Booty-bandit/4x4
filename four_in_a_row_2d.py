empty = "."
player1 = "0"
player2 = "X"

board =    [[empty, empty, empty, empty], 
            [empty, empty, empty, empty], 
            [empty, empty, empty, empty], 
            [empty, empty, empty, empty]]

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

            
def check_for_win(player):
    #Check rows

    #Check columns

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