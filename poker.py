""" Make poker hands
"""


import random


VALUES = '2 3 4 5 6 7 8 9 10 Jack Queen King Ace'.split()
SUITS = 'Hearts Diamonds Clubs Spades'.split()


def make_new_deck():
    cards = []
    for suit in SUITS:
        for value in VALUES:
            card = value + ' of ' + suit
            cards.append(card)
    return cards


def test_new_deck():
    # We will test the `make_new_deck` function
    deck = make_new_deck()
    assert len(deck) == 52
    first_card = deck[0]
    assert first_card == "2 of Hearts"
    assert deck[12]  == "Ace of Hearts"
    assert deck[13]  == "2 of Diamonds"
    assert deck[26]  == "2 of Clubs"
    assert deck[51]  == "Ace of Spades"
    # Make sure all cards are unique
    assert len(set(deck)) == len(deck)


def shuffled(deck):
    re_ordered = deck.copy()
    random.shuffle(re_ordered)
    return re_ordered


def test_shuffled():
    decks = []
    # Put an ordered deck into the list of decks
    decks.append(make_new_deck())
    for i in range(1000):
        deck = make_new_deck()
        shuffled_deck = shuffled(deck)
        # Compare this deck to all previous ones. Do any match?
        assert shuffled_deck not in decks
        decks.append(shuffled_deck)


if __name__ == "__main__":
    print("Running tests")
    test_new_deck()
    test_shuffled()
    print("Finished")
