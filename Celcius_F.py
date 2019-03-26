'''
Created on Feb 21, 2019
Created for: ICS3U
@author: Francesca Berkoh

This program converts the temp in celcius to farenheit
'''

def fun(c):
    f = (1.8)*c+32
    print ("Answer is:" + str(f) + "F")

c = input ("Enter temp in Celcius")
c = float(c)
fun(c)

