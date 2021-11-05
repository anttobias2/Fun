import random
from card import card
from hand import Hand
from player import Player
from dealer import Dealer


# makes a single deck of cards and return the deck
def make_deck(cards, suits):
    deck_cards = []

    for suit in suits:
        for value in cards:
            my_card = card(value, suit)
            # deck_cards.append([my_card.get_card(), my_card.get_suit()]) // This would add the card display and its suit
            deck_cards.append(my_card)

    return deck_cards

# makes a shoe of cards containing num_decks decks
def make_shoe(deck, num_decks):
    shoe = []

    for i in range(num_decks):
        for card in deck:
            shoe.append(card)

    return shoe

# shuffle the shoe and return the shuffled shoe
def shuffle_shoe(shoe):
    return random.shuffle(shoe)

# print shoe used for debugging/testing
def print_shoe(shoe):
    for card in shoe:
        print(card.get_card() + ' ' + card.get_suit())

# deal hands to a single player and a dealer
def deal_hands(shoe):
    # create hand objects for player and dealer
    player_hand = Hand()
    dealer_hand = Hand()

    # deal 2 cards to each player
    player_hand.add_card(shoe.pop())
    dealer_hand.add_card(shoe.pop())
    player_hand.add_card(shoe.pop())
    dealer_hand.add_card(shoe.pop())

    return player_hand, dealer_hand, shoe

def play_again():
    user_input = input('Would you like to play again: ')

    if user_input == 'y':
        return True
    else:
        return False

def check_blackjacks(dealer_hand, player_hand):
    if dealer_hand.check_blackjack():
            print('Dealer has blackjack. Dealer wins with : ')
            print(dealer_hand.print_hand())
            return True
    elif player_hand.check_blackjack():
        print('You have blackjack. You win 3 to 2!')
        return True

    return False

def check_win(player_hand, dealer_hand):
    player_total = player_hand.get_hand_value()
    dealer_total = dealer_hand.get_hand_value()

    if(not player_hand.check_bust() and player_total > dealer_total):
        return True
    return False

def main():
    # print('This is blackjack\n')

    # define cards and suits that will be in the decks
    cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']

    # define empty arrays for deck and shoe
    deck_cards = []
    shoe = []

    # create a deck of cards
    deck_cards = make_deck(cards, suits)
    
    
    # create a shoe of 6 decks, shuffle and print
    shoe = make_shoe(deck_cards, 6)
    shuffle_shoe(shoe)
    # print_shoe(shoe)
    num_hand = 0 # used for error checking

    while(len(shoe) > 25):
        player_hand, dealer_hand, shoe = deal_hands(shoe)
        player_hand.print_hand()
        dealer_hand.print_dealer_hand()
        # check for blackjacks right away
        check_blackjacks(dealer_hand, player_hand)
        player_hand = player_hand.hit_or_stay(shoe)
        player_hand.print_hand()
        if(check_win(player_hand, dealer_hand)):
            print("You win!")
        #play_again()
        
        num_hand += 1
    # print('Shuffling new shoe. Num hands played: ' + str(num_hand))
    # print_shoe(shoe)

        
main()