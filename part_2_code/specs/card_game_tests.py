import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame (unittest.TestCase):

    def setUp(self):
        self.card1 = Card("Clubs", 10)
        self.card2 =Card("Heart", 1)
        self.cardgame =CardGame


    def test_check_for_ace__False(self):
        self.assertEqual(False, self.cardgame.check_for_ace(self,self.card1))
    
    def test_check_for_ace__True(self):
        self.assertEqual(True, self.cardgame.check_for_ace(self,self.card2))
        
    def test_highest_card(self):
        self.assertEqual(self.card1, self.cardgame.highest_card(self,self.card1,self.card2))
    
    def test_cards_total(self):
        cards = [self.card1,self.card2]
        self.assertEqual("You have a total of 11", self.cardgame.cards_total(self,cards))
    
    
    
    
