# -*- coding: utf-8 -*-
"""
Created on Mon May  4 22:31:45 2020

@author: F
"""


class Patient(object):
    status = 'Patient'
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.conditions = []
        
    def get_details(self):
        print(f'Patient record: {self.name}, {self.age} years.', 
              f' Current information: {self.conditions}')
    
    def add_info(self, information):
        self.conditions.append(information)

class Infant(Patient):
    def __init__(self, name, age):
        self.vaccinations = []
        super().__init__(name, age)
    
    def add_vac(self, vaccine):
        self.vaccinations.append(vaccine)
    
    def get_details(self):
        print(f'Patient record: {self.name}, {self.age} years.' \
              f' Patient has had {self.vaccinations} vaccines.' \
              f' Current information: {self.conditions}.' \
              f'\n{self.name} IS AN INFANT, HAS HE HAD ALL HIS CHECKS?')
    
fikky = Patient('Fikky Ardianto', 20)
print(fikky.status)