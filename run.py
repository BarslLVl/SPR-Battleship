import os
import random


def create_board(size):
    return [["."] * size for _ in range(size)]


def place_ships(board, num_ships):
    for _ in range(num_ships):
        while True:
            x, y = (random.randint(0, len(board) - 1),
                    random.randint(0, len(board) - 1))
            if board[x][y] == ".":
                board[x][y] = "@"
                break


def initialize_player_and_computer_boards(board_size):
    player_board = create_board(board_size)
    computer_board = create_board(board_size)
    place_ships(player_board, board_size)
    place_ships(computer_board, board_size)
    return player_board, computer_board


def convert_coordinates(input_str):
    try:
        col = ord(input_str[0].upper()) - ord('A')
        row = int(input_str[1:])
        return row, col
    except (ValueError, IndexError):
        return None


def computer_turn(player_board):
    while True:
        x, y = (random.randint(0, len(player_board) - 1),
                random.randint(0, len(player_board) - 1))
        if player_board[x][y] == "@":
            print("Computer hit your ship at {}{}!".format(
                chr(ord('A') + y), x))
            player_board[x][y] = "*"
            return "hit"
        elif player_board[x][y] == ".":
            print("Computer missed your ships at {}{}.".format(
                chr(ord('A') + y), x))
            player_board[x][y] = "X"
            return "miss"


def player_turn(computer_board):
    while True:
        input_str = input("Enter the target coordinates (e.g., A5): ")
        coordinates = convert_coordinates(input_str)
        if coordinates is None or coordinates[0] >= len(computer_board) or \
                coordinates[1] >= len(computer_board):
            print("Invalid coordinates. Please try again.")
            continue
        x, y = coordinates
        if computer_board[x][y] == "@":
            print("Hit! You've sunk an enemy ship!")
            computer_board[x][y] = "*"
            return "hit"
        elif computer_board[x][y] == ".":
            print("Miss! The enemy ship has evaded your attack.")
            computer_board[x][y] = "X"
            return "miss"


def check_game_over(board):
    return all(cell != "@" for row in board for cell in row)


def play_again():
    input("\nPress Enter to exit or Shift + Enter to play again...")
    if os.name == 'nt':  # Check if the operating system is Windows
        os.system('cls')
    else:
        os.system('clear')
    play_game()


def play_game():
    print("_________________________________")
    print("Welcome to the SPR Battleship")
    print("_________________________________")
    player_name = input("Enter your nickname: ")
    difficulty = input("Choose the difficulty level (easy, medium, hard): ").lower()
    if difficulty == "easy":
        board_size = 5
    elif difficulty == "medium":
        board_size = 7
    elif difficulty == "hard":
        board_size = 10
    else:
        print("Incorrect difficulty level. Setting the default difficulty level to medium.")
        board_size = 7
    player_board, computer_board = initialize_player_and_computer_boards(board_size)
    print("\nMarkers:")
    print(". - selectable for shooting")
    print("@ - your ships")
    print("* - destruction of enemy target")
    print("X - your missed shots")
    while True:
        print("\nYour board:")
        print_board(player_board, show_ships=True)
        print("\nComputer's board:")
        print_board(computer_board)
        player_result = player_turn(computer_board)
        if check_game_over(computer_board):
            print("\nCongratulations, {}! You have won!".format(player_name))
            play_again()
        print("\nComputer's Turn:")
        computer_result = computer_turn(player_board)
        if check_game_over(player_board):
            print("\nSorry, {}! You have lost!".format(player_name))
            play_again()


def print_board(board, show_ships=False):
    print("  " + " ".join(chr(ord('A') + i) for i in range(len(board))))
    for i, row in enumerate(board):
        print(str(i) + " " + " ".join((cell if cell != "@" or show_ships else ".") for cell in row))


if __name__ == "__main__":
    play_game()
