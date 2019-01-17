import random

class Card(object):
    suit_names =  ["Diamonds","Clubs","Hearts","Spades"]
    rank_levels = [1,2,3,4,5,6,7,8,9,10,11,12,13]
    faces = {1:"Ace",11:"Jack",12:"Queen",13:"King"}

    def __init__(self, suit=0,rank=2):
        self.suit_name = self.suit_names[suit]
        if rank in self.faces: # self.rank_name handles printed representation
            self.rank_name = self.faces[rank]
        else:
            self.rank_name = rank
        self.rank_num = rank # To handle winning comparison

    def __str__(self):
        return "{} of {}".format(self.rank_name,self.suit_name)

class Deck(object):
    def __init__(self): # Don't need any input to create a deck of cards
        # This working depends on Card class existing above
        self.cards = []
        for suit in range(4):
            for rank in range(1,14):
                card = Card(suit,rank)
                self.cards.append(card) # appends in a sorted order

    def __str__(self):
        total = []
        for card in self.cards:
            total.append(card.__str__())
        # shows up in whatever order the cards are in
        return "\n".join(total) # returns a multi-line string listing each card

    def pop_card(self, i=-1):
        # removes and returns a card from the Deck
        # default is the last card in the Deck
        return self.cards.pop(i) # this card is no longer in the deck -- taken off

    def shuffle(self):
        random.shuffle(self.cards)

    def replace_card(self, card):
        card_strs = [] # forming an empty list
        for c in self.cards: # each card in self.cards (the initial list)
            card_strs.append(c.__str__()) # appends the string that represents that card to the empty list
        if card.__str__() not in card_strs: # if the string representing this card is not in the list already
            self.cards.append(card) # append it to the list

    def rebuild_deck_and_sort_cards(self):
        # Basically, remake the deck in a sorted way
        # This is assuming you cannot have more than the normal 52 cards in a deck and that you are rebuilding full deck
        self.cards = []
        for suit in range(4):
            for rank in range(1,14):
                card = Card(suit,rank)
                self.cards.append(card)

# Call this function with testing = True and it won't print out all the game stuff
# -- which makes it hard to see test results
def play_war_game(testing=False):
    player1 = Deck()
    player2 = Deck()

    p1_score = 0
    p2_score = 0

    player1.shuffle()
    player2.shuffle()
    if not testing:
        print("\n*** BEGIN THE GAME ***\n")
    for i in range(52):
        p1_card = player1.pop_card()
        p2_card = player2.pop_card()
        if not testing:
            print("Player 1 plays", p1_card,"& Player 2 plays", p2_card)

        if p1_card.rank_num > p2_card.rank_num:
            if not testing:
                print("\tPlayer 1 wins a point!")
            p1_score += 1
        elif p1_card.rank_num < p2_card.rank_num:
            if not testing:
                print("\tPlayer 2 wins a point!")
            p2_score += 1
        else:
            if not testing:
                print("Tie. Next turn.")

    if p1_score > p2_score:
        return "Player1", p1_score, p2_score
    elif p2_score > p1_score:
        return "Player2", p1_score, p2_score
    else:
        return "Tie", p1_score, p2_score


result = play_war_game()
print("\n\nWinner is: {} - Player 1 scored {}, Player 2 scored {}".format(*result))
