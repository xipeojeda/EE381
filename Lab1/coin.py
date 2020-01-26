# -*- coding: utf-8 -*-
"""
Created on Wed Jan 23 19:59:31 2019

@author: Jesus Ojeda
"""
import numpy

def coin2(N):
    count = 0
    for i in range (0,N):#flipping coin N times
        coin = numpy.random.randint(0,2,100)#list of 100 0 or 1
        heads = numpy.sum(coin) #adding list up
        if heads == 50:#if heads success
            count += 1
        
    print('probability of 50 Heads: ', count/N)

print(coin2(100000))


