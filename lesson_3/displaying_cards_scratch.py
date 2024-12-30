import random, os, copy, time

RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

SUITS = ['Clubs', 'Spades' ,'Hearts', 'Diamonds']

DECK = [ { rank: suit } for rank in RANKS for suit in SUITS ]

def prompt(message):
    print(f"==>{message}")

def shuffle(deck):
     random.shuffle(deck)

def deal(deck):
    return deck.pop()

def center_card_info(info):
    card_width = 10
    return info.center(card_width, ' ')

def display_cards(hand):    

    prompt("Hand:")
    
    for card in hand:
        print('')
        print('------------')
        print('|          |')
        
        for rank in card:
       
            print(f'|{center_card_info(rank)}|')
            print('|    of    |')
            print(f'|{center_card_info(card[rank])}|')
            
        print('|          |')
        print('------------')


play_deck = copy.deepcopy(DECK)

shuffle(play_deck)

hand = [ deal(play_deck) for _ in range(2) ]

display_cards(hand)
