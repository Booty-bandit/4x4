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

def check_row_wincon(map,row):
    #counts the number of x's or y's in a row and resets the wincon_counter if there is a new type
    current_wincon = ""
    wincon_counter = 0
    for y in range(collum):
        for num in range(row):
            if map[y][num] != current_wincon:
                wincon_counter = 0
            if map[y][num] == "x":
                wincon_counter +=1
                current_wincon = "x"
            elif map[y][num] == "y":
                wincon_counter +=1
                current_wincon = "y"
            if wincon_counter == 4:
                print(f"{current_wincon} has won")

def check_collum_wincon(map,collum):
    current_wincon = ""
    wincon_counter = 0
    for x in range(row):
        for num in range(collum):
            if map[num][x] != current_wincon:
                wincon_counter = 0
            if map[num][x] == "x":
                wincon_counter += 1
                current_wincon = "x"
            elif map[num][x] == "y":
                wincon_counter += 1
                current_wincon = "y"
            if wincon_counter == 4:
                print(f"{current_wincon} has won")


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