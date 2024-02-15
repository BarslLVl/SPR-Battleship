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
            msg = ("Computer hit your ship at {}{}!"
                   .format(chr(ord('A') + y), x))
            print(msg)
            player_board[x][y] = "*"
            return "hit"
        elif player_board[x][y] == ".":
            msg = ("Computer missed your ships at {}{}."
                   .format(chr(ord('A') + y), x))
            print(msg)
            player_board[x][y] = "X"
            return "miss"


def player_turn(computer_board):
    while True:
        input_str = input("Enter the target coordinates (e.g., A5): ")
        coordinates = convert_coordinates(input_str)
        if coordinates is None \
           or coordinates[0] >= len(computer_board) \
           or coordinates[1] >= len(computer_board):
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
    user_input = input("\nType 'e' and press Enter to exit "
                       "or type 'r' and press Enter to play again... ")
    if user_input.lower() == 'r':
        if os.name == 'nt':  # Check if the operating system is Windows
            os.system('cls')
        else:
            os.system('clear')
        play_game()
    elif user_input.lower() == 'e':
        print("Goodbye!")
        exit()
    else:
        print("Invalid input. Please try again.")
        play_again()


def print_board(board, show_ships=False):
    print("  " + " ".join(chr(ord('A') + i) for i in range(len(board))))
    for i, row in enumerate(board):
        print(str(i) + " " + " ".join(
            (cell if cell != "@" or show_ships else ".") for cell in row))


def play_game():
    print("_________________________________")
    print()
    print("Welcome to the SPR Battleship")
    print("Get ready for an epic naval battle!")
    print("May the winds be in your favor. Good luck!")
    print("_________________________________")
    player_name = input("Please enter your name: ")
    difficulty = input(
        "Choose the difficulty level (easy, medium, hard): "
    ).lower()
    if difficulty == "easy":
        board_size = 5
    elif difficulty == "medium":
        board_size = 7
    elif difficulty == "hard":
        board_size = 10
    else:
        print(
            "Incorrect difficulty level. Setting the default difficulty "
            "level to medium."
        )
        board_size = 7
    player_board, computer_board = initialize_player_and_computer_boards(
        board_size
    )
    print("\nMarkers:")
    print(". - selectable for shooting")
    print("@ - your ships")
    print("* - destruction of enemy target")
    print("X - your missed shots")
    player_score = 0
    computer_score = 0
    loss_messages = [
        "Don't worry, you'll get them next time!",
        "Better luck next game!",
        "Every defeat is a lesson. Keep playing and improving!",
        "It's not about the result, but the journey. Keep sailing!",
        "You fought well! Try again for victory!",
        "The sea is vast, and so are the opportunities. Keep exploring!",
        "Chin up! Your naval prowess will shine in the next battle.",
        "Remember, even the greatest admirals faced setbacks."
        "Keep your head high!",
        "A setback is a setup for a comeback. Ready for the next round?",
        "Your resilience is your greatest asset. Keep challenging yourself!"
    ]
    win_messages = [
        "Congratulations, {}! You are the master of the high seas!",
        "Well done, {}! Your naval strategy is unmatched!",
        "Victory is yours, {}! You've conquered the ocean!",
        "You've emerged victorious, {}! Your fleet reigns supreme!",
        "Bravo, {}! Your tactical brilliance led to a glorious win!",
        "A salute to you, {}! Your naval command has triumphed!",
        "Hail the victorious admiral, {}! You've achieved naval excellence!",
        "Cheers, {}! Your fleet sails as the undisputed champion!",
        "A decisive win, {}! The seas bow to your command!",
        "You've achieved naval glory, {}! Bask in the triumph of victory!"
    ]
    while True:
        print("\nYour board:")
        print_board(player_board, show_ships=True)
        print("\nComputer's board:")
        print_board(computer_board)
        player_result = player_turn(computer_board)
        if player_result == "hit":
            player_score += 1
        print("\nScore: {}: {} - Computer: {}".format(
            player_name, player_score, computer_score))
        if check_game_over(computer_board):
            print("-------------------------------")
            print(random.choice(win_messages).format(player_name))
            print("-------------------------------")
            play_again()
        print("\nComputer's Turn:")
        computer_result = computer_turn(player_board)
        if computer_result == "hit":
            computer_score += 1
        print("\nScore: {}: {} - Computer: {}".format(
            player_name, player_score, computer_score))
        if check_game_over(player_board):
            print("-------------------------------")
            print("\nSorry, {}, but you lost!".format(player_name))
            print(random.choice(loss_messages))
            print()
            print("-------------------------------")
            play_again()


if __name__ == "__main__":
    play_game()