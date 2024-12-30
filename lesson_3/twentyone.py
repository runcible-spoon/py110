import random
import os
import copy
import time

RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10',
         'Jack', 'Queen', 'King', 'Ace']

SUITS = ['Clubs', 'Spades' ,'Hearts', 'Diamonds']

DECK = [ { rank: suit } for rank in RANKS for suit in SUITS ]

CARD_WIDTH = 10

# DEALING

def shuffle(deck):
    random.shuffle(deck)

def deal(deck):
    return deck.pop()

# DISPLAY

def clear_screen():
    os.system('clear')

def prompt(message):
    print(f"==> {message}")

def card_prepend():
    print(f' {'-' * CARD_WIDTH}')
    print(f'|{' ' * CARD_WIDTH}|')

def card_append():
    print(f'|{' ' * CARD_WIDTH}|')
    print(f' {'-' * CARD_WIDTH}')
    print('')

def center_card_info(info):
    return info.center(CARD_WIDTH, ' ')

def display_full_hand(hand):
    for card in hand:
        card_prepend()

        for rank in card:
            print(f'|{center_card_info(rank)}|')
            print(f'|{center_card_info('of')}|')
            print(f'|{center_card_info(card[rank])}|')

        card_append()

def display_first_dealer_card(hand):
    for rank in hand[0]:
        card_prepend()
        print(f'|{center_card_info(rank)}|')
        print(f'|{center_card_info('of')}|')
        print(f'|{center_card_info(hand[0][rank])}|')
        card_append()

def display_hole_card():
    card_prepend()
    print(f'|{center_card_info('Hole')}|')
    print(f'|{center_card_info('???')}|')
    print(f'|{center_card_info('Card')}|')
    card_append()

def display_turn(current_player, player_hand, dealer_hand):

    clear_screen()

    match current_player:
        case 'Player':
            prompt("Your hand:")
            display_full_hand(player_hand)

            prompt("Dealer's hand:")
            display_first_dealer_card(dealer_hand)
            display_hole_card()

        case 'Dealer':
            prompt("Your hand:")
            display_full_hand(player_hand)

            prompt("Dealer's hand:")
            display_full_hand(dealer_hand)

def turn_transition():
    clear_screen()

    card_prepend()
    print(f'|{center_card_info("Dealer's")}|')
    print(f'|{' ' * CARD_WIDTH}|')
    print(f'|{center_card_info("Turn")}|')
    card_append()

    time.sleep(2)

def display_result(result, player_hand, dealer_hand):
    prompt(f"Result: {result}")
    prompt(f"Your total: {total(player_hand)}")
    prompt(f"Dealer's total: {total(dealer_hand)}")

# TURNS

def turn(current_player, deck, player_hand, dealer_hand):

    match current_player:
        case 'Player':
            while True:

                display_turn(current_player, player_hand, dealer_hand)

                if blackjack(player_hand):
                    prompt("You got a natural 21! Blackjack!")

                prompt("(H)it or (S)tay?")
                answer = input().lower()

                if answer == 'h':
                    player_hand += [deal(deck)]
                    if twenty_one(player_hand):
                        prompt("Twenty-one!")

                if answer == 's' or busted(player_hand):
                    break

            if busted(player_hand):
                display_turn(current_player, player_hand, dealer_hand)
                prompt("You busted....")
                prompt(f"Your total: {total(player_hand)}")
                time.sleep(2)
                return None

            prompt("You chose to stay.")
            time.sleep(2)
            return player_hand

        case 'Dealer':
            prompt("Dealer reveals hole card...")
            time.sleep(1)

            while True:
                display_turn(current_player, player_hand, dealer_hand)
                time.sleep(3)

                if total(dealer_hand) >= 17:
                    prompt("The dealer chose to stay.")
                    break

                prompt("Dealer hits.")
                time.sleep(2)

                dealer_hand += [deal(deck)]

                display_turn(current_player, player_hand, dealer_hand)
                time.sleep(2)

                if busted(dealer_hand):
                    prompt("Dealer busted!")
                    break

            time.sleep(2)
            return dealer_hand

# CALCULATIONS

def total(hand):
    values = [ rank for card in hand for rank in card ]

    sum_value = 0
    for value in values:
        if value == 'Ace':
            sum_value += 11
        elif value in ['Jack', 'Queen', 'King']:
            sum_value += 10
        else:
            sum_value += int(value)

    aces = values.count('Ace')
    while sum_value > 21 and aces:
        sum_value -= 10
        aces -= 1

    return sum_value

def blackjack(hand):
    return total(hand) == 21 and len(hand) == 2

def twenty_one(hand):
    return total(hand) == 21

def busted(hand):
    return total(hand) > 21

def calculate_result(player_hand, dealer_hand):
    outcomes = {

    'Dealer wins': {
        busted(player_hand),
        blackjack(dealer_hand) and not blackjack(player_hand),
        (total(dealer_hand) > total(player_hand)) and not busted(dealer_hand)},

    'Player wins': {
        busted(dealer_hand),
        blackjack(player_hand) and not blackjack(dealer_hand),
        (total(player_hand) > total(dealer_hand)) and not busted(player_hand)}
    }

    if any(outcomes['Dealer wins']):
        return 'Dealer won.'
    if any(outcomes['Player wins']):
        return 'Player won!'
    return 'Push.'

# PLAY AGAIN?

def play_again():
    prompt("Play again? y / n")
    answer = input().lower()
    while answer not in ('y', 'n'):
        prompt('''Invalid input. Enter Y to play again
                or N to terminate program.''')
        answer = input().lower()

    return answer

# MAIN

def play_twentyone():
    # play again loop
    while True:
        # game
        while True:
            play_deck = copy.deepcopy(DECK)
            shuffle(play_deck)

            dealer_hand = [ deal(play_deck) for _ in range(2) ]
            player_hand = [ deal(play_deck) for _ in range(2) ]

            current_player = 'Player'
            player_final_hand = turn(current_player,
                                     play_deck,
                                     player_hand,
                                     dealer_hand)
            if not player_final_hand:
                break

            turn_transition()

            current_player = 'Dealer'
            dealer_final_hand = turn(current_player,
                                     play_deck,
                                     player_hand,
                                     dealer_hand)

            result = calculate_result(player_final_hand, dealer_final_hand)
            display_result(result, player_hand, dealer_hand)
            break

        play_again_choice = play_again()
        if play_again_choice == 'n':
            break

    prompt("Thanks for playing!")

play_twentyone()
