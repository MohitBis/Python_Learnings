"""
Given two strings, a and b, return the result of putting them together in the order abba,
e.g. "Hi" and "Bye" returns "HiByeByeHi".


make_abba('Hi', 'Bye') → 'HiByeByeHi'
make_abba('Yo', 'Alice') → 'YoAliceAliceYo'
make_abba('What', 'Up') → 'WhatUpUpWhat'

"""

def make_abba(a,b):
    return a+b+b+a
a = input("Enter first string: ")
b = input("Enter secound string: ")
print(make_abba(a,b))
