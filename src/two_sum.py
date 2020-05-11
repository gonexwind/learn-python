# -*- coding: utf-8 -*-
"""
Created on Wed May  6 08:02:03 2020

@author: Fikky Ardianto
"""


L = [2, 5, 3, 7, 4]
target = 10

def two_sum(nums, target):
    d = {}
    
    for i in range(len(nums)):
        if target - nums[i] in d:
            print(d)
            return [d[target-nums[i]], i]
        d[nums[i]] = i
    return -1