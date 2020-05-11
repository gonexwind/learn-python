# -*- coding: utf-8 -*-
"""
Created on Mon May  4 23:31:49 2020

@author: Fikky Ardianto
"""

# class BankAccount(object):
#     def __init__(self, balance = 0.0):
#         self.balance = balance
    
#     def display_balance(self):
#         print(f'Your current balance is {self.balance}')
    
#     def make_deposito(self):
#         amount = float(input('How much would you like to deposit?'))
#         self.balance += amount
#         print(f'Balance is now {self.balance}')
    
#     def make_withdrawal(self):
#         amount = float(input('How much would you like to withdraw?'))
#         if amount > self.balance:
#             print(f'Sorry, you dont have sufficient funds, your balance is now {self.balance}')
#         else:
#             self.balance -= amount
#             print(f'Withdraw successful: balance is now {self.balance}')

### CIRCLE AREA
from math import pi

class Circle(object):
    def __init__(self, radius):
        self.radius = radius
    
    def calc_area(self):
        area = pi * (self.radius)**2
        return area

    
    
    
    
    
    
    
    
    
    
    
    