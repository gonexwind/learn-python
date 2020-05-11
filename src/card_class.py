# -*- coding: utf-8 -*-
"""
Created on Wed May  6 08:21:52 2020

@author: Fikky Ardianto
"""

class Card(object):
    suits = {'s': 'Spades', 'h': 'Hearts', 'd': 'Diamonds', 'c': 'Clubs'}
    values = {1: 'Ace', 'j': 'Jack', 'q': 'Queen', 'k': 'King'}
   
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
        
    def get_value(self):
        return self.value;
    
    def get_suit(self):
        return self.suit
    
    def __str__(self):
        my_card = str(self.value) + ' of ' + str(self.suit)
        return my_card

my_card = Card(3, 'd')
