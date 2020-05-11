# -*- coding: utf-8 -*-
"""
Created on Sun May  3 23:06:28 2020

@author: Fikky Ardianto
"""

# DICTIONARY

countries = {
    'id': 'Indonesia',
    'sg': 'Singapore',
    'us': 'United States',
    'uk': 'United Kingdom',
}

# for code, country in countries.items():
#     print(f'Kode {code} merupakan negara {country}')
    
print(countries.keys())

if 'us' in countries:
    print('Ada US didalam Dictionary')