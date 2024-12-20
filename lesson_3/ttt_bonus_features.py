import os
import random
import pdb

INITIAL_MARKER = ' '
HUMAN_MARKER = 'X'
COMPUTER_MARKER = 'O'

GAME_POINT = 1
TO_WIN_MATCH = 5

WINNING_LINES = [
        [1, 2, 3], [4, 5, 6], [7, 8, 9],
        [1, 4, 7], [2, 5, 8], [3, 6, 9],
        [1, 5, 9], [3, 5, 7]
    ]

# DISPLAY BOARD

def prompt(message):
    print(f"==> {message}")


def display_board(board, game_number, player_score, computer_score):
    os.system('clear')

    prompt(f"You are {HUMAN_MARKER}. Computer is {COMPUTER_MARKER}.")
    prompt(f"Game number {game_number}. First to 5 points wins.")
    prompt(f"Player score: {player_score} | Computer score: {computer_score}")
    
    print('')
    print('     |     |')
    print(f"  {board[1]}  |  {board[2]}  |  {board[3]}")
    print('     |     |')
    print('-----+-----+-----')
    print('     |     |')
    print(f"  {board[4]}  |  {board[5]}  |  {board[6]}")
    print('     |     |')
    print('-----+-----+-----')
    print('     |     |')
    print(f"  {board[7]}  |  {board[8]}  |  {board[9]}")
    print('     |     |')
    print('')

def initialize_board():
    return {square: INITIAL_MARKER for square in range(1, 10)}

def empty_squares(board):
    return [key for key, value in board.items() if value == INITIAL_MARKER]

def join_or(sequence, delimiter=', ', conjunction='or'):
    match len(sequence):
        case 0:
            return ''
        case 1:
            return str(sequence[0])
        case 2:
            return f"{sequence[0]} {conjunction} {sequence[1]}"
        
    zipped_list = list(zip(sequence, [delimiter for _ in range(len(sequence))]))
    zipped_list.insert(-1, conjunction + ' ')
    return ''.join([ str(element) for sublist in zipped_list
                                    for element in sublist ])[:-2]

# TURN ACTIONS

def player_chooses_square(board):
    while True:
        valid_choices = [str(num) for num in empty_squares(board)]
        prompt(f"Choose a square ({join_or(valid_choices, ', ', 'or')})")
        square = input().strip()
        if square in valid_choices:
            break

        prompt("Sorry, that's not a valid choice.")

    board[int(square)] = HUMAN_MARKER

def computer_chooses_square(board):
    if len(empty_squares(board)) == 0:
        return None
    square = random.choice(empty_squares(board))
    board[square] = COMPUTER_MARKER

# DETERMINE OUTCOME

def detect_game_winner(board):
    for line in WINNING_LINES:
        sq1, sq2, sq3 = line
        if (        board[sq1] == HUMAN_MARKER
                and board[sq2] == HUMAN_MARKER
                and board[sq3] == HUMAN_MARKER):
            return 'Player'
        elif (      board[sq1] == COMPUTER_MARKER
                and board[sq2] == COMPUTER_MARKER
                and board[sq3] == COMPUTER_MARKER):
            return 'Computer'

    return None

def someone_won_game(board):
    return bool(detect_game_winner(board))

def board_full(board):
    return len(empty_squares(board)) == 0

def detect_match_winner(player_score, computer_score):
    if player_score == TO_WIN_MATCH:
        return 'Player'
    elif computer_score == TO_WIN_MATCH:
        return 'Computer'
    
    return None

def someone_won_match(player_score, computer_score):
    return bool(detect_match_winner(player_score, computer_score))

# SCORETENDING

def display_game_outcome(board):
    if someone_won_game(board):
        prompt(f'{detect_game_winner(board)} won!')
    else:
        prompt("It's a tie!")

def increment_score(board, player_score, computer_score):
    if someone_won_game(board):
        match detect_game_winner(board):
            case 'Player':
                print("PLAYER SCORE INCREMENTED")
                return player_score + GAME_POINT, computer_score
            case 'Computer':
                print("COMPUTER SCORE INCREMENTED")
                return player_score, computer_score + GAME_POINT
            
    return player_score, computer_score

def display_match_outcome(player_score, computer_score):
    prompt(f"{detect_match_winner(player_score, computer_score)} won!")

def play_again():
    answer = input(prompt(f"Play again? y / n")).lower()
    return answer[0] == 'y'

# MAIN

def play_tic_tac_toe():

    # PLAY AGAIN LOOP
    while True:
   
        player_score = 0
        computer_score = 0

        game_number = 1

        # MATCH LOOP
        while True:

            if detect_match_winner(player_score, computer_score):
                break

            board = initialize_board()

            # GAME LOOP
            while True:
                display_game_outcome(board)
                display_board(board, game_number, player_score, computer_score)

                player_chooses_square(board)
                if someone_won_game(board) or board_full(board):
                    break
            
                computer_chooses_square(board)
                if someone_won_game(board) or board_full(board):
                    break

            player_score, computer_score = increment_score(board, player_score, computer_score)

            display_board(board, game_number, player_score, computer_score)

            game_number += 1


        display_board(board, game_number, player_score, computer_score)
        display_match_outcome(player_score, computer_score)


        if not play_again():
            break
        
    prompt("Thanks for playing!")

play_tic_tac_toe()




        
        






                
