'''
Created on Mar 18, 2018

@author: ola

Simulate poker hands. A card is a 2-tuple
of the form (rank,suit) where rank is a number
from 0-12 and suit is a number from 0-3.

So (0,0) represents the ace of spades and (12,3)
represents the king of clubs. That equivalence 
is evidenced in the function card_to_string.
An ace being 0 matters for some poker hands, but not others,
e.g., an ace could be any number for a pair or a full-house, but
not for a royal flush or for determining which of two
one-pair hands might win (not part of this program)
'''
import random

def card_to_string(card):
    """
    card is a 2-tuple where card[0] is 0-12 and
    card[1] is 0-3
    
    returns a string representing the card represented
    by parameter, e.g., "ace of spades", "two of hearts",
    or "king of diamonds"
    """
    rankStrings = ["ace","two","three","four","five","six","seven",
                   "eight","nine","ten","jack","queen","king"]
    suitStrings = ["spades", "hearts", "diamonds","clubs"]
    return rankStrings[card[0]] + " of " + suitStrings[card[1]]

def get_rank_counts(hand):
    '''
    returns list of how often each rank 0-12 occurs in a hand
    where e.g., list[0] is # aces, list[1] is # twos
    list[11] = # occurrences of queen since ranks go
    from 0-12 with 0 an ace.
    '''
    counts = [0]*13
    for card in hand:
        rank = card[0]
        counts[rank] += 1
    return counts

def one_pair(hand):
    '''
    hand is a list of cards
    Return true if and only if hand has exactly one pair
    '''
    ranks = get_rank_counts(hand)
    if ranks.count(2) == 1 and ranks.count(1) == 3:
        return True
    return False

def two_pair(hand):
    ranks = get_rank_counts(hand)
    if ranks.count(2) == 2 and ranks.count(1) == 1:
        return True
    return False

def three_kind(hand):
    ranks = get_rank_counts(hand)
    if ranks.count(3) == 1 and ranks.count(1) == 2:
        return True
    return False

def full_house(hand):
    ranks = get_rank_counts(hand)
    if ranks.count(3) == 1 and ranks.count(2) == 1:
        return True
    return False

def get_suit_counts(hand):
    counts = [0]*4
    for card in hand:
        suit = card[1]
        counts[suit] += 1
    return counts

def flush(hand):
    suits = get_suit_counts(hand)
    if suits.count(5) == 1:
        return True
    return False

def get_deck():
    '''
    create and return an unshuffled deck of cards
    '''
    d = []
    for rank in range(0,13):
        for suit in range(0,4):
            d.append((rank,suit))
    return d

def get_hand(deck):
    """
    returns one hand from the deck
    by shuffling and using first five cards
    """
    random.shuffle(deck)
    return deck[0:5]

def hand_to_string(hand):
    """
    hand is a list of cards (tuples)
    returns a string representing the hand
    e.g., for printing
    """
    st = '['
    strings = [card_to_string(card) for card in hand]
    st += ",".join(strings)
    return st + "]"
    

def deal_demo():
    """
    Demonstrates get_deck, get_hand,
    and hand_to_string functions
    """
    deck = get_deck()
    print(hand_to_string(deck))
    print(hand_to_string(get_hand(deck)))
    print(hand_to_string(get_hand(deck)))

def funcstring(funcname):
    """
    returns string of function name, e.g.,
    for printing legibly 
    """
    s = str(funcname)[10:]  #chop off '<function '
    spi = s.index(' ')
    return s[:spi]

def simulate(n,hand_type):
    '''
    Simulate dealing n poker hands, return number
    of times that hand_type occurs, where handType could
    b is_pair or is_flush or ...
    '''
    deck = get_deck()
    pc = 0
    for i in range(0,n):
        hand = get_hand(deck)
        if hand_type(hand):
            pc += 1
    print("# hands = %d, # %s = %d, prob = %.5f" % (n, funcstring(hand_type),pc, 1.0*pc/n))
    return pc

if __name__ == "__main__":
    #random.seed(2992)
    deal_demo()
    hands = 20000
    handfuncs = [one_pair, two_pair,three_kind, full_house, flush] #, two_pairs, three_kind, full_house, four_kind, flush, straight]
    for func in handfuncs:
        simulate(hands,func)
    #simulate(hands,three_kind)
    #simulate(hands,two_pairs)
    #simulate(hands,full_house)
    #simulate(hands,four_kind)
    #simulate(hands,flush)