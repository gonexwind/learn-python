# -*- coding: utf-8 -*-
"""
Created on Mon May  4 10:11:57 2020

@author: F
"""


# print('Hello World!')
# def hello():
#     print('Hello World!')
    
# def hi(name):
#     print(f'Hai {name}!')

def hai(name='Fikky'):
    print(f'Hai {name}!')
    
def fib(n):
    a = 0
    b = 1
    for i in range(n):
        a, b = b, a + b
    return a

def calc_mean(first_number, *remainder):
    mean = (first_number + sum(remainder)) / (1 + len(remainder))
    print(mean)