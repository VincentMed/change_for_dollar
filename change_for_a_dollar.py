# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 10:07:45 2022

@author: Vincent Medrano with help from geeks for geeks
"""

# Write a python program to find the total number of ways to make change for $1

def change(coins, n, sum):
 
    if (sum == 0):
        return 1
 
    if (sum < 0):
        return 0
 
    if (n <= 0):
        return 0
 
    # change is sum of solutions (i)
    # including coins[n-1] (ii) excluding coins[n-1]
    return change(coins, n - 1, sum) + change(coins, n, sum-coins[n-1])
 
coins = [1, 5, 10, 25, 50]
n = 5
print(change(coins, n, 100))
    
    
    
    



