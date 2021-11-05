'''
This is a file that allows you to play a game of blackjack
For now it will just be something you play on the command line
'''
import random

# displays basic instructions of the game
def display_instructions():
    print('\n \nThis is a Blackjack\n' + 'The goal is to get more than the dealer while having 21 or less when combining all your cards')
    print('Rules: ')
    print('1) Blackjack pays 3 to 2')
    print('2) Insurance pays 2 to 1')
    print('3) Double down only on first two cards')
    print('4) Limited to 4 splits per hand')
    print('5) Only get one card when splitting aces')
    print('6) Playing with 6 decks of cards')

# creates a single deck for the game containing 52 cards
def create_deck(cards):
    deck = []

    for i in range(4):
        for card in cards:
            deck.append(card)

    return deck

# shuffles a deck of cards
def shuffle(shoe):
    random.shuffle(shoe)
    
    #for i in range(decks):
        

# creates a stack for a shoe of how ever many decks desired

def create_shoe(num_decks, deck):
    shoe = []
    for i in range(num_decks):
        for card in deck:
            shoe.append(card)

    return shoe    

def deal_hand(shoe):
    player_hand = []
    dealer_hand = []

    player_hand.append(shoe.pop())
    dealer_hand.append(shoe.pop())
    player_hand.append(shoe.pop())
    dealer_hand.append(shoe.pop())

    return shoe, player_hand, dealer_hand

def hit_or_stay(shoe, player_hand):
    userIn = input('Would you like to hit or stay? (h/s): ')

    while((userIn != 's' or userIn != 'S')):
        if(userIn == 'h' or userIn == 'H'):
            player_hand.append(shoe.pop())
        else:
            print('Error: Enter a valid option (s/h)\n')
            hit_or_stay(shoe, player_hand)

    return player_hand

def get_hand_value(hand):
    sum = 0

    # 2 sums for hands that contain an ace
    sum2 = 0

    for card in hand:
        if card.isnumeric():
            # add to sum
            sum += card
            sum2 += card
        # add 2 different values for hands that have aces
        elif card == 'A':
            sum += 1
            sum2 += 11
        # add value of face card
        else:
            sum += 10
            sum2 += 10

    return sum, sum2

def check_hand(sum, sum2):
    if sum > 21:
        print('Bust.\n' + 'Dealer Wins')    


def main():
    display_instructions()
    cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    shoe = []
    deck = create_deck(cards)
    # print(deck)
    shoe = create_shoe(6, deck)
    shuffle(shoe)

    # print(shoe)

    shoe, player_hand, dealer_hand = deal_hand(shoe)

    
    print('Dealers top card: ' + str(dealer_hand[0]) + '\n')
    print('Your hand: ' + str(player_hand[0]) + ' ' + str(player_hand[1]))
    hit_or_stay(shoe, player_hand)
    print('\n')

main()