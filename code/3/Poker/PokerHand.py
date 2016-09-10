"""This module contains code from
Think Python by Allen B. Downey
http://thinkpython.com

Copyright 2012 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

from Card import *
import copy


class PokerHand(Hand):
    labels = ['straightflush', 'fourkind', 'fullhouse', 'flush',
              'straight', 'threekind', 'twopair', 'pair']

    def rank_card_mapper(self):
        self.rank_card_map = {}
        for ind in range(1, 14):
            self.rank_card_map[ind] = []

        for card in self.cards:
            self.rank_card_map.get(card.rank).append(card)

    def rank_hist(self):
        """
         Builds a histogram of the ranks that appear in the hand and stores
         the result in attribute ranks
        """
        self.ranks = {}
        for card in self.cards:
            self.ranks[card.rank] = self.ranks.get(card.rank, 0) + 1

    def suit_hist(self):
        """Builds a histogram of the suits that appear in the hand.
        Stores the result in attribute suits.
        """
        self.suits = {}
        for card in self.cards:
            self.suits[card.suit] = self.suits.get(card.suit, 0) + 1

    def has_flush(self):
        """Returns True if the hand has a flush, False otherwise.

        Note that this works correctly for hands with more than 5 cards.
        """
        self.suit_hist()
        for val in self.suits.values():
            if val >= 5:
                return True
        return False

    def has_nkind(self, n):
        self.rank_hist();
        for val in self.ranks.values():
            if val >= n:
                return True
        return False

    def has_pair(self):
        return self.has_nkind(2)

    def has_twopair(self):
        self.rank_hist()
        count = 0
        for val in self.ranks.values():
            if val >= 2:
                count += 1

        if count >= 2:
            return True
        return False

    def has_threekind(self):
        return self.has_nkind(3)

    def has_straight(self):
        self.rank_hist()
        print self.ranks

        for iind in range(1, 11):
            found = True

            if iind != 10:
                for jind in range(0, 5):
                    if self.ranks.get(iind + jind) == None:
                        found = False

                if found:
                    return True
                else:
                    iind += (jind + 1)
            else:
                for jind in range(0, 4):
                    if self.ranks.get(iind + jind) == None:
                        found = False

                if self.ranks.get(1) == None:
                    found = False

                if found:
                    return True
                else:
                    iind += (jind + 1)

        return False;

    def has_fullhouse(self):
        self.rank_hist();

        two_found = False
        three_found = False
        for val in self.ranks.values():
            if val >= 2:
                two_found = True
            elif val >= 3:
                three_found = True

        return two_found and three_found

    def has_fourkind(self):
        return self.has_nkind(4)

    def belong_to_same_suit(self, rank_list, suit):
        self.rank_card_mapper()
        found = True
        for ind in range(0, len(rank_list)):
            curr_rank = rank_list[ind]
            curr_rank_cards = self.rank_card_map.get(curr_rank)

            curr_rank_found = False
            for card in curr_rank_cards:
                if card.suit == suit:
                    curr_rank_found = True
                    break

            if not curr_rank_found:
                return False
        return found

    def has_straightflush(self):
        self.rank_hist()

        for iind in range(1, 11):
            found = True

            if iind != 10:
                for jind in range(0, 5):
                    if self.ranks.get(iind + jind) == None:
                        found = False

                if found:
                    rank_list = range(iind, jind + iind + 1)
                    print rank_list
                    for suit in range(0, len(Card.suit_names)):
                        if self.belong_to_same_suit(rank_list, suit):
                            return True

                else:
                    iind += (jind + 1)
            else:
                for jind in range(0, 4):
                    if self.ranks.get(iind + jind) == None:
                        found = False

                if self.ranks.get(1) == None:
                    found = False

                if found:
                    rank_list = range(iind, jind + iind + 1)
                    rank_list.append(1)

                    print rank_list
                    for suit in range(0, len(Card.suit_names)):
                        if self.belong_to_same_suit(rank_list, suit):
                            return True


                else:
                    iind += (jind + 1)

        return False;

    def classify(self):
        index = -1
        if self.has_straightflush():
            index += 1
            return PokerHand.labels[index]
        elif self.has_fourkind():
            index += 1
            return PokerHand.labels[index]
        elif self.has_fullhouse():
            index += 1
            return PokerHand.labels[index]
        elif self.has_flush():
            index += 1
            return PokerHand.labels[index]
        elif self.has_straight():
            index += 1
            return PokerHand.labels[index]
        elif self.has_threekind():
            index += 1
            return PokerHand.labels[index]
        elif self.has_twopair():
            index += 1
            return PokerHand.labels[index]
        else:
            index += 1
            return PokerHand.labels[index]


if __name__ == '__main__':
    # make a deck
    deck = Deck()
    deck.shuffle()

    # hand = PokerHand()
    # deck.move_cards(hand, 10)
    # hand.sort()
    # print hand.has_straight()
    # print hand.has_straightflush()


    for i in range(7):
        hand = PokerHand()
        deck.move_cards(hand, 7)
        hand.sort()
        print hand
        print "Flush :" + str(hand.has_flush())
        print "Four kind :" + str(hand.has_fourkind())
        print "Pair : " + str(hand.has_pair())
        print "Two Pair : " + str(hand.has_twopair())
        print "Three kind : " + str(hand.has_threekind())
        print ''
