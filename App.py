from random import choice

def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    for i in range(0, 9 ,3):
        print(f" {board[i] or ' '} | {board[i+1] or ' '} | {board[i+2] or ' '}")
        if i < 6:
            print("---|---|---")
    print("\n")
    
def enter_move(board):
    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.
    while True:
        user_input = input("Enter your move, Cell 1-9: ")
        if user_input.isdigit():
            user_input = int(user_input)
            if 1 <= user_input <= 9:
                user_input -= 1
                if board[user_input] == '':
                    board[user_input] = 'O'
                    break
                else:
                    print("Cell is already occupied. Try again")
        else:
            print("Invalid input. Try again using a number between 1 and 9")

def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares;
    return [index for index, value in enumerate(board) if value == '']

def victory_for(board, sign):
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game

    winning_combo = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 4, 8),
        (2, 4, 6),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8)
    ]

    for combo in winning_combo:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == sign:
            return True
    return False

def draw_move(board):
    # The function draws the computer's move and updates the board.
    
    free_fields = make_list_of_free_fields(board)
    if free_fields:
        move = choice(free_fields)
        board[move] = 'X' #Computer starts with 'X in the middle

# Implement the logic  for the program
def start_game():
    board = [''] * 9
    board[4] = 'X'
    
    while True:
        display_board(board)
        
        # Your round
        enter_move(board)
        if victory_for(board, 'O'):
            display_board(board)
            print("Player wins")
            break
        
        if not make_list_of_free_fields(board):
            display_board(board)
            print("We have a draw")
            break
            
        # Computer's round
        draw_move(board)
        display_board(board)
        if victory_for(board, 'X'):
            print("Loser! You ain't better than a machine.")
            break
        
        if not make_list_of_free_fields(board):
            display_board(board)
            print("We have a draw.")
            break

start_game()