import random
import os
import time

# THE DECK
RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10',
         'Jack', 'Queen', 'King', 'Ace']

SUITS = ['Clubs', 'Spades' ,'Hearts', 'Diamonds']

# CARD VALUES
ACE_HIGH_VALUE = 11
ACE_LOW_VALUE = 1
FACE_VALUE = 10

CARD_WIDTH = 10 # width of card display. See CARD GENERATION

STARTING_HAND = 2
DEALER_CUTOFF = 17

# SCORE CONSTANTS
TO_WIN_GAME = 21
GAME_POINT = 1
TO_WIN_MATCH = 3

# DECKBUILDING, DEALING

def initialize_deck():
    initialized_deck = [ { rank: suit } for rank in RANKS for suit in SUITS ]
    random.shuffle(initialized_deck)
    return initialized_deck

def deal(deal_deck):
    return deal_deck.pop()

# GENERAL DISPLAY

def clear_screen():
    os.system('clear')

def prompt(message):
    print(f"==> {message}")

def center_card_info(info):
    return info.center(CARD_WIDTH, ' ')

def short_pause():
    time.sleep(2)

def longer_pause():
    time.sleep(3)

# CARD GENERATION

def display_full_hand(hand):
    for card in hand:
        print(f' {'-' * CARD_WIDTH}')
        for rank in card:
            print(f'|{center_card_info(rank)}|')
            print(f'|{center_card_info('of')}|')
            print(f'|{center_card_info(card[rank])}|')
        print(f' {'-' * CARD_WIDTH}')

def display_first_dealer_card(hand):
    for rank in hand[0]:
        print(f' {'-' * CARD_WIDTH}')
        print(f'|{center_card_info(rank)}|')
        print(f'|{center_card_info('of')}|')
        print(f'|{center_card_info(hand[0][rank])}|')
        print(f' {'-' * CARD_WIDTH}')

def display_hole_card():
    print(f' {'-' * CARD_WIDTH}')
    print(f'|{center_card_info('Hole')}|')
    print(f'|{center_card_info('???')}|')
    print(f'|{center_card_info('Card')}|')
    print(f' {'-' * CARD_WIDTH}')

# DISPLAY TURNS

def display_player_turn(player_hand, player_total, dealer_hand):
    prompt("Your hand:")
    display_full_hand(player_hand)

    prompt("Dealer's hand:")
    display_first_dealer_card(dealer_hand)
    display_hole_card()

    prompt(f"Your total: {player_total}")

def display_dealer_turn(player_hand, player_total, dealer_hand, dealer_total):
    prompt("Your hand:")
    display_full_hand(player_hand)

    prompt("Dealer's hand:")
    display_full_hand(dealer_hand)

    prompt(f"Your total: {player_total}")
    prompt(f"Dealer's total: {dealer_total}")

# CALCULATIONS

def total(hand):
    values = [ rank for card in hand for rank in card ]

    sum_value = 0
    for value in values:
        if value == 'Ace':
            sum_value += ACE_HIGH_VALUE
        elif value in ['Jack', 'Queen', 'King']:
            sum_value += FACE_VALUE
        else:
            sum_value += int(value)

    aces = values.count('Ace')
    while sum_value > TO_WIN_GAME and aces:
        sum_value -= FACE_VALUE
        aces -= ACE_LOW_VALUE

    return sum_value

def blackjack(hand, hand_total):
    return hand_total == TO_WIN_GAME and len(hand) == STARTING_HAND

def twenty_one(hand_total):
    return hand_total == TO_WIN_GAME

def busted(hand_total):
    return hand_total > TO_WIN_GAME

# RESULTS

def calculate_game_result(player_hand,
                          player_total,
                          dealer_hand,
                          dealer_total):
    game_outcomes = {

    'DEALER_WINS_GAME': {
        busted(player_total),
        blackjack(dealer_hand, dealer_total)
            and not blackjack(player_hand, player_total),
        (dealer_total > player_total)
            and not busted(dealer_total)},

    'PLAYER_WINS_GAME': {
        busted(dealer_total),
        blackjack(player_hand, player_total)
            and not blackjack(dealer_hand, dealer_total),
        (player_total > dealer_total)
            and not busted(player_total)}
    }

    if any(game_outcomes['DEALER_WINS_GAME']):
        return 'DEALER_WINS_GAME'
    if any(game_outcomes['PLAYER_WINS_GAME']):
        return 'PLAYER_WINS_GAME'

    return None

def display_game_result(game_result, player_total, dealer_total):

    if not game_result:
        prompt("This game is a push! No winner."
               f"Your hand was {player_total}.")
        prompt(f"Dealer's hand was {dealer_total}.")
    elif game_result == 'DEALER_WINS_GAME':
        prompt(f"Dealer won this game with {dealer_total}.")
        prompt(f"You lost with {player_total}.")
    elif game_result == 'PLAYER_WINS_GAME':
        prompt (f"You won this game with {player_total}.")
        prompt(f"Dealer lost with {dealer_total}.")

def increment_score(result, player_score, computer_score):
    match result:
        case 'DEALER_WINS_GAME':
            return player_score, computer_score + GAME_POINT
        case 'PLAYER_WINS_GAME':
            return player_score + GAME_POINT, computer_score
        case _:
            return player_score, computer_score

def display_score(player_score, dealer_score):
    prompt("============= SCORES =============")
    prompt(f"Player score: {player_score} | Dealer score: {dealer_score}")
    print('')

def detect_best_of_five(player_score, dealer_score):
    if dealer_score == TO_WIN_MATCH:
        return 'DEALER_WINS_MATCH'
    if player_score == TO_WIN_MATCH:
        return 'PLAYER_WINS_MATCH'

    return None

def display_best_of_five_result(player_score, dealer_score):
    result = detect_best_of_five(player_score, dealer_score)
    match result:
        case 'DEALER_WINS_MATCH':
            prompt(f"Dealer wins with {dealer_score} out of {TO_WIN_MATCH}!")
            prompt("Better luck next time.")
        case 'PLAYER_WINS_MATCH':
            prompt(f"You win with {player_score} out of {TO_WIN_MATCH}!")
            prompt("Lady Luck smiles upon you tonight!")

# PLAY AGAIN?

def play_again():
    prompt("Play again? y / n")
    answer = input().lower()
    while answer not in ('y', 'n'):
        prompt('Invalid input. Enter Y to play again '
               'or N to terminate program.')
        answer = input().lower()

    return answer

# MAIN
def play_twentyone():

    # PLAY AGAIN LOOP
    while True:
        player_score = 0
        dealer_score = 0

        clear_screen()
        prompt("Welcome to Twenty-One!")
        prompt("Best out of five wins.")
        print('')

        # GAME LOOP
        while not detect_best_of_five(player_score, dealer_score):
            deck = initialize_deck()

            dealer_hand = [ deal(deck) for _ in range(STARTING_HAND) ]
            dealer_total = total(dealer_hand)

            player_hand = [ deal(deck) for _ in range(STARTING_HAND) ]
            player_total = total(player_hand)

            display_score(player_score, dealer_score)
            display_player_turn(player_hand, player_total, dealer_hand)

            if twenty_one(player_total):
                prompt("You got a natural 21! Blackjack!")

            # PLAYER TURN
            while True:
                prompt("(H)it or (S)tay?")
                player_choice = input().lower()
                if player_choice not in ['h', 's']:
                    prompt("Enter 'h' to hit and receive another card "
                           "or 's' to stay and end your turn.")
                    continue

                if player_choice == 'h':
                    player_hand.append(deal(deck))
                    player_total = total(player_hand)

                    clear_screen()
                    display_score(player_score, dealer_score)
                    display_player_turn(player_hand, player_total, dealer_hand)

                    if twenty_one(player_total):
                        prompt("Twenty-one!")

                if player_choice == 's' or busted(player_total):
                    break

            if busted(player_total):
                prompt("You busted....")
                short_pause()

                result = calculate_game_result(player_hand,
                                            player_total,
                                            dealer_hand,
                                            dealer_total)
                display_game_result(result, player_total, dealer_total)
                player_score, dealer_score = increment_score(result,
                                                            player_score,
                                                            dealer_score)

                longer_pause()

                clear_screen()
                continue

            prompt("You chose to stay.")
            short_pause()

            # DEALER TURN
            prompt("Dealer reveals hole card...")
            short_pause()

            clear_screen()
            display_score(player_score, dealer_score)
            display_dealer_turn(player_hand,
                                player_total,
                                dealer_hand,
                                dealer_total)

            while dealer_total < DEALER_CUTOFF:
                prompt("Dealer hits.")
                short_pause()

                dealer_hand.append(deal(deck))
                dealer_total = total(dealer_hand)

                clear_screen()
                display_score(player_score, dealer_score)
                display_dealer_turn(player_hand,
                                    player_total,
                                    dealer_hand,
                                    dealer_total)

            if busted(dealer_total):
                prompt("Dealer busted!")
                short_pause()

                result = calculate_game_result(player_hand,
                                            player_total,
                                            dealer_hand,
                                            dealer_total)
                display_game_result(result, player_total, dealer_total)
                player_score, dealer_score = increment_score(result,
                                                            player_score,
                                                            dealer_score)

                longer_pause()

                clear_screen()
                continue

            prompt("Dealer chose to stay.")
            short_pause()

            result = calculate_game_result(player_hand,
                                        player_total,
                                        dealer_hand,
                                        dealer_total)
            display_game_result(result, player_total, dealer_total)

            player_score, dealer_score = increment_score(result,
                                                        player_score,
                                                        dealer_score)
            longer_pause()
            clear_screen()

        display_best_of_five_result(player_score, dealer_score)

        play_again_input = play_again()
        match play_again_input:
            case 'y':
                continue
            case 'n':
                break

    prompt("Thanks for playing!")

play_twentyone()
