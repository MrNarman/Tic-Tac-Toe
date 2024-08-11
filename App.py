board = [' ' for _ in range(9)]

def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.

    print(f"{board[0]}|{board[1]}|{board[2]}")
    print("-" * 5)
    print(f"{board[3]}|{board[4]}|{board[5]}")
    print("-" * 5)
    print(f"{board[6]}|{board[7]}|{board[8]}")

def enter_move(board):
    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.

    user_input = int(input("Enter your move. Cell 1-9: "))
    user_input -= 1

    board[user_input] = "X"

    display_board(board)

def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares;
    return [(index // 3, index % 3) for index, value in enumerate (board) if value == '']