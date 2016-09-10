from PokerHand import *


def print_all(hand):
    print "Flush :" + str(hand.has_flush())
    print "Four kind :" + str(hand.has_fourkind())
    print "Pair : " + str(hand.has_pair())
    print "Two Pair : " + str(hand.has_twopair())
    print "Three kind : " + str(hand.has_threekind())
    print "Full house : " + str(hand.has_fullhouse())
    print "Straight : " + str(hand.has_straight())
    print "Straight flush : " + str(hand.has_straightflush())


def test1():
    # make a deck
    deck = Deck()
    deck.shuffle()

    hand = PokerHand()

    ## Cards of one suit in consecutive order
    for i in range(1, 10):
        hand.add_card(Card(0, i))

    hand.sort()
    print_all(hand)


def test2():
    # make a deck
    deck = Deck()
    deck.shuffle()

    hand = PokerHand()

    ## Cards of one suit in alternate order
    for i in range(1, 13, 2):
        hand.add_card(Card(0, i))

    hand.sort()
    print_all(hand)


def test3():
    deck = Deck()
    deck.shuffle()

    hand = PokerHand()

    hand.add_card(Card(0, 1))
    hand.add_card(Card(2, 10))
    hand.add_card(Card(3, 11))
    hand.add_card(Card(1, 12))
    hand.add_card(Card(0, 13))
    hand.sort()

    print_all(hand)


def test4():
    deck = Deck()
    deck.shuffle()

    hand = PokerHand()

    hand.add_card(Card(0, 1))
    hand.add_card(Card(0, 10))
    hand.add_card(Card(0, 11))
    hand.add_card(Card(0, 12))
    hand.add_card(Card(0, 13))

    hand.add_card(Card(2, 2))
    hand.add_card(Card(3, 3))
    hand.add_card(Card(1, 4))
    hand.add_card(Card(1, 5))
    hand.sort()

    print_all(hand)


def test5():
    deck = Deck()
    deck.shuffle()

    hand = PokerHand()

    hand.add_card(Card(0, 1))
    hand.add_card(Card(1, 1))
    hand.add_card(Card(0, 2))
    hand.add_card(Card(1, 2))
    hand.add_card(Card(2, 2))

    hand.add_card(Card(1, 10))
    hand.add_card(Card(2, 10))
    hand.add_card(Card(3, 10))
    hand.add_card(Card(0, 10))
    hand.sort()

    print_all(hand)


def test6():
    deck = Deck()
    deck.shuffle()

    hand = PokerHand()

    hand.add_card(Card(0, 1))
    hand.add_card(Card(0, 10))
    hand.add_card(Card(0, 11))
    hand.add_card(Card(0, 12))
    hand.add_card(Card(0, 13))

    hand.add_card(Card(2, 2))
    hand.add_card(Card(3, 3))
    hand.add_card(Card(1, 4))
    hand.add_card(Card(1, 5))

    hand.add_card(Card(1, 1))
    hand.add_card(Card(0, 2))
    hand.add_card(Card(1, 2))

    hand.add_card(Card(1, 10))
    hand.add_card(Card(2, 10))
    hand.add_card(Card(3, 10))

    hand.sort()

    print_all(hand)
    print hand.classify()


def test7():
    deck = Deck()
    deck.shuffle()

    hand = PokerHand()

    hand.add_card(Card(0, 1))
    hand.add_card(Card(1, 1))

    hand.sort()

    print_all(hand)
    print hand.classify()

def test8():
    deck = Deck()
    deck.shuffle()

    hand = PokerHand()

    hand.add_card(Card(0, 1))
    hand.add_card(Card(1, 1))
    hand.add_card(Card(2, 1))
    hand.add_card(Card(0, 2))
    hand.add_card(Card(1, 2))

    hand.sort()

    print_all(hand)
    print hand.classify()


if __name__ == '__main__':
    # test1()
    # test2()
    # test3()
    # test4()
    # test5()
    # test6()
    # test7()
    test8()
