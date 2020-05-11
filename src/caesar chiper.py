# -*- coding: utf-8 -*-
"""
Created on Wed May  6 02:34:52 2020

@author: F
"""

# CAESAR CHIPHER
class CaesarChiper(object):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    plain = input('Enter plaintext:>\t').lower()
    key = int(input('Enter key:>\t'))

    def __init__(self, plain, key, alphabet):
        self.plain = plain
        self.key = key
        self.alphabet = alphabet

    def encrypt(self):
        enkripsi = ''
        for char in self.plain:
            alpha_index = self.alphabet.find(char)
            enkripsi = enkripsi + self.alphabet[(alpha_index+self.key)%26]         
        print(f'Enkripsi: {enkripsi}')
        
    def decrypt(self):
        dekripsi = ''
        for char in self.plain:
            alpha_index = self.alphabet.find(char)
            dekripsi = dekripsi + self.alphabet[(alpha_index+self.key)%26]         
        print(f'Dekripsi: {dekripsi}')
        