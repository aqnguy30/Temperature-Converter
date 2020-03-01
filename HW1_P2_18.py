# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
def temp_convert():
    #Ask user's input
    temp_c = float(input("Enter a temparature in Celsius (degrees): "))
    ##Plugging in variables to the formula to calculate
    temp_f = (9/5) * temp_c + 32
    #Display the result
    print("The temperature converted to Fahrenheit is:", format(temp_f, '.2f') + " degrees")

temp_convert()
    