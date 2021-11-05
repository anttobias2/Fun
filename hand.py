class Hand:

    def __init__(my_hand):
        my_hand.hand = []

    def add_card(my_hand, card):
        my_hand.hand.append(card)

    def get_hand(my_hand):
        cards = []
        for card in my_hand.hand:
            cards.append(card.get_card())
        return cards

    def check_blackjack(my_hand):
        total = 0
        for card in my_hand.hand:
            total += card.get_value()

        if(len(my_hand.hand) == 2 and total == 21):
            return True
        else:
            return False

    def check_bust(my_hand):
        total = my_hand.get_hand_value()

        if(total > 21):
            print("Bust\n")
            return True
        return False
    
    def print_hand(player_hand):
        print(player_hand.get_hand())

    def print_dealer_hand(dealer_hand):
        hand = dealer_hand.get_hand()
        print("Dealer's top card: " + hand[0])

    def hit_or_stay(my_hand, shoe):
        while(my_hand.check_bust() == False):
            h_s = input('Would you like to hit or stay?(h/s): ')
            if(h_s == 'h' or h_s == 'H'):
                my_hand.add_card(shoe.pop())
                my_hand.print_hand()
            elif h_s == 's' or h_s == 'S':
                return my_hand
            else:
                print('Error: Please enter a valid character (h/s). ')
                
        return my_hand

    def get_hand_value(my_hand):
        total = 0

        for card in my_hand.hand:
            total += card.get_value()
        return total
            