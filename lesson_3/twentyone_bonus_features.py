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
WINS_GAME = 21
GAME_POINT = 1
WINS_MATCH = 3

# DECKBUILDING, DEALING

def initialize_deck():
    initialized_deck = [ { rank: suit } for rank in RANKS for suit in SUITS ]
    random.shuffle(initialized_deck)
    return initialized_deck

def deal(deal_deck):
    return deal_deck.pop()

# GENERAL DISPLAY

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def prompt(message):
    print(f"==> {message}")

def center_card_info(info):
    return info.center(CARD_WIDTH, ' ')

def pause():
    time.sleep(2)

def advance():
    prompt("Press any key to continue.")
    advance_input = input().lower()
    while not advance_input:
        prompt("Press any key to continue.")
        advance_input = input().lower()

    return advance_input

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

def display_player_turn(stats):
    prompt("Your hand:")
    display_full_hand(stats['player_hand'])

    prompt("Dealer's hand:")
    display_first_dealer_card(stats['dealer_hand'])
    display_hole_card()

    prompt(f"Your total: {stats['player_total']}")

def display_dealer_turn(stats):
    prompt("Your hand:")
    display_full_hand(stats['player_hand'])

    prompt("Dealer's hand:")
    display_full_hand(stats['dealer_hand'])

    prompt(f"Your total: {stats['player_total']}")
    prompt(f"Dealer's total: {stats['dealer_total']}")

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
    while sum_value > WINS_GAME and aces:
        sum_value -= FACE_VALUE
        aces -= ACE_LOW_VALUE

    return sum_value

def blackjack(hand, hand_total):
    return hand_total == WINS_GAME and len(hand) == STARTING_HAND

def twenty_one(hand_total):
    return hand_total == WINS_GAME

def busted(hand_total):
    return hand_total > WINS_GAME

# RESULTS

def calculate_game_result(stats):
    game_outcomes = {

    'DEALER_WINS_GAME': {
        # player busted
        busted(stats['player_total']),

        # dealer got blackjack, player didn't
        blackjack(stats['dealer_hand'], stats['dealer_total']) and not blackjack(stats['player_hand'], stats['player_total']),

        # dealer's hand larger than player's and dealer didn't bust
        (stats['dealer_total'] > stats['player_total']) and not busted(stats['dealer_total'])},

    'PLAYER_WINS_GAME': {
        # dealer busted
        busted(stats['dealer_total']),

        # player got blackjack, dealer didn't
        blackjack(stats['player_hand'], stats['player_total']) and not blackjack(stats['dealer_hand'], stats['dealer_total']),

        # player's hand larger than dealer's and player didn't bust
        (stats['player_total'] > stats['dealer_total']) and not busted(stats['player_total'])}
    }

    if any(game_outcomes['DEALER_WINS_GAME']):
        return 'DEALER_WINS_GAME'

    if any(game_outcomes['PLAYER_WINS_GAME']):
        return 'PLAYER_WINS_GAME'

    return None

def display_game_result(game_result, stats):
    if not game_result:
        prompt("This game is a push! No winner."
               f"Your hand was {stats['player_total']}.")
        prompt(f"Dealer's hand was {stats['dealer_total']}.")

    elif game_result == 'DEALER_WINS_GAME':
        prompt(f"Dealer won this game with {stats['dealer_total']}.")
        prompt(f"You lost with {stats['player_total']}.")

    elif game_result == 'PLAYER_WINS_GAME':
        prompt (f"You won this game with {stats['player_total']}.")
        prompt(f"Dealer lost with {stats['dealer_total']}.")

def increment_score(result, stats):
    match result:
        case 'DEALER_WINS_GAME':
            stats['dealer_score'] += GAME_POINT
            return
        case 'PLAYER_WINS_GAME':
            stats['player_score'] += GAME_POINT
            return

    return

def display_score(stats):
    prompt("============= SCORES =============")
    prompt(f"Player score: {stats['player_score']} | Dealer score: {stats['dealer_score']}")
    print('')

def detect_best_of_five(stats):
    if stats['dealer_score'] == WINS_MATCH:
        return 'DEALER_WINS_MATCH'
    if stats['player_score'] == WINS_MATCH:
        return 'PLAYER_WINS_MATCH'

    return None

def display_best_of_five_result(stats):
    result = detect_best_of_five(stats)

    match result:
        case 'DEALER_WINS_MATCH':
            prompt(f"Dealer wins with {stats['dealer_score']} out of {WINS_MATCH}!")
            prompt("Better luck next time.")
        case 'PLAYER_WINS_MATCH':
            prompt(f"You win with {stats['player_score']} out of {WINS_MATCH}!")
            prompt("Lady Luck smiles upon you tonight!")

# GAME LOOP

def play_game(stats):
    while not detect_best_of_five(stats):

        stats['deck'] = initialize_deck()

        stats['dealer_hand'] = [ deal(stats['deck']) for _ in range(STARTING_HAND) ]
        stats['dealer_total'] = total(stats['dealer_hand'])

        stats['player_hand'] = [ deal(stats['deck']) for _ in range(STARTING_HAND) ]
        stats['player_total'] = total(stats['player_hand'])

        display_score(stats)
        display_player_turn(stats)

        # PLAYER TURN
        player_busted = player_turn(stats, player_busted=None)

        if player_busted:
            continue

        # DEALER TURN
        dealer_turn(stats)

    return

def player_turn(stats, player_busted=None):

    if twenty_one(stats['player_total']):
        prompt("You got a natural 21! Blackjack!")

    while True:
        prompt("(H)it or (S)tay?")
        player_choice = input().lower()
        if player_choice not in ['h', 's']:
            prompt("Enter 'h' to hit and receive another card "
                "or 's' to stay and end your turn.")
            continue

        if player_choice == 'h':
            stats['player_hand'].append(deal(stats['deck']))
            stats['player_total'] = total(stats['player_hand'])

            clear_screen()
            display_score(stats)
            display_player_turn(stats)

            if twenty_one(stats['player_total']):
                prompt("Twenty-one!")

        if player_choice == 's' or busted(stats['player_total']):
            break

    if busted(stats['player_total']):
        prompt("You busted....")
        pause()

        result = calculate_game_result(stats)
        display_game_result(result, stats)
        increment_score(result, stats)

        advance()
        clear_screen()
        player_busted = True
        return player_busted

    prompt("You chose to stay.")
    return

def dealer_turn(stats):
    prompt("Dealer reveals hole card...")
    pause()

    clear_screen()
    display_score(stats)
    display_dealer_turn(stats)

    while stats['dealer_total'] < DEALER_CUTOFF:
        prompt("Dealer hits.")
        pause()

        stats['dealer_hand'].append(deal(stats['deck']))
        stats['dealer_total'] = total(stats['dealer_hand'])

        clear_screen()
        display_score(stats)
        display_dealer_turn(stats)

    if busted(stats['dealer_total']):
        prompt("Dealer busted!")
        pause()

        result = calculate_game_result(stats)
        display_game_result(result, stats)
        increment_score(result, stats)

        advance()
        clear_screen()
        return

    prompt("Dealer chose to stay.")
    pause()

    result = calculate_game_result(stats)
    display_game_result(result, stats)

    increment_score(result, stats)
    advance()
    clear_screen()

    return

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
        stats = {
            'player_score':     0,
            'dealer_score':     0,

            'deck':             None,

            'dealer_hand':      None,
            'dealer_total':     None,

            'player_hand':      None,
            'player_total':     None,
        }

        print(stats)

        clear_screen()
        prompt("Welcome to Twenty-One!")
        prompt("Best out of five wins.")
        print('')

        # GAME LOOP
        play_game(stats)

        display_best_of_five_result(stats)

        play_again_input = play_again()
        match play_again_input:
            case 'y':
                continue
            case 'n':
                break

    prompt("Thanks for playing!")

play_twentyone()
