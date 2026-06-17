import random

def display_board(board):
    print('\n'*100)
    print(board[7]+"|"+board[8]+"|"+board[9])
    print("-"+"-"+"-"+"-"+"-")
    print(board[4]+"|"+board[5]+"|"+board[6])
    print("-"+"-"+"-"+"-"+"-")
    print(board[1]+"|"+board[2]+"|"+board[3])

def player_input():
    
    marker = ''

    while not (marker == 'X' or marker == 'O'):
        marker = input("Please pick a marker to play('X' or 'O): ").upper()
    if marker == 'X':
        print("Player1 picked 'X', Player2 gets 'O'")
        return ('X','O')
    else:
        print("Player1 picked 'O', Player2 gets 'X'")
        return ('O','X')

def place_marker(board, marker, position):
     board[position] = marker

def win_check(board, mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or
    (board[4] == mark and board[5] == mark and board[6] == mark) or
    (board[1] == mark and board[2] == mark and board[3] == mark) or
    (board[7] == mark and board[4] == mark and board[1] == mark) or
    (board[8] == mark and board[5] == mark and board[2] == mark) or
    (board[9] == mark and board[6] == mark and board[3] == mark) or
    (board[7] == mark and board[5] == mark and board[3] == mark) or
    (board[9] == mark and board[5] == mark and board[1] == mark))

def choose_first():
    flip = random.randint(0,1)
    if flip == 0:
        return 'Player1'
    else:
        return 'Player2'

def space_check(board, position):
    
    return board[position] == ' '

def full_board_check(board):
    
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True

def player_choice(board):
    position = 0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position = int(input("Please choose a position(1-9): "))
    return position

def replay():
    
    choice = input("Do you want to play again?(Y or N): ").upper()
    return choice == 'Y'

print('Welcome to Tic Tac Toe!')

while True:

    board = [' ']*10
    player1_marker,player2_marker = player_input()
    
    turn = choose_first()
    print(turn+" goes first")

    play_game = input("Ready to play?(choose Y or N)").upper()

    if play_game == 'Y':
        game_on = True
    else:
        game_on = False
    
    while game_on:
        if turn == 'Player1':
            display_board(board)
            position = player_choice(board)
            place_marker(board,player1_marker,position)

            if win_check(board,player1_marker):
                display_board(board)
                print("PLAYER1 HAS WON THE GAME!")
                game_on = False
            else:
                if full_board_check(board):
                    display_board(board)
                    print("TIE GAME!")
                    game_on = False
                else:
                    turn = 'Player2'
        else:
            display_board(board)

            position = player_choice(board)

            place_marker(board,player2_marker,position)


            if win_check(board,player2_marker):
                display_board(board)
                print("PLAYER2 HAS WON THE GAME!")
                game_on = False
            else:
                if full_board_check(board):
                    display_board(board)
                    print("TIE GAME!")
                    game_on = False
                else:
                    turn = 'Player1'

    if not replay():
        break