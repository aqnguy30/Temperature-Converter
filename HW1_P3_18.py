#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 02:13:49 2020

@author: anhnguyen
"""

def account():
    #Ask user's inputs
    p = float(input("Enter the amount of principal originally deposited ($): "))
    r = float(input("Enter the annual interest rate paid in (%): ")) / 100
    n = float(input("Enter the number of times per year that the interest is compounded (times per year): "))
    t = float(input("Enter the number of years the account will be left to earn interest (years): "))
    #Plugging in variables to the formula to calculate
    a = p * (1 + r/n)**(n*t)
    #Display the result
    print("After " + str(t) + " year(s)" + ", the final amount of money in the account is: " + format(a, '.2f') +" $")

account()
