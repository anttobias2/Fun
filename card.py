class card:
    
    # constructor
    # gives card a numerical value and suit display char
    def __init__(the_card, val, type_suit):
        the_card.suit = type_suit

        if(val.isnumeric()):
            the_card.value = int(val)
        elif(val == 'A'):
            the_card.value = 11
            the_card.value2 = 11
        else:
            the_card.value = 10
        
        the_card.display = val

    # returns the value the card holds
    def get_value(the_card):
        return the_card.value

    # returns the display char of card
    def get_card(the_card):
        return the_card.display

    # returns suit of card
    def get_suit(the_card):
        return the_card.suit