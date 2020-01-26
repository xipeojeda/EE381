# -*- coding: utf-8 -*-
"""
Created on Wed Jan 23 20:14:09 2019

@author: Jesus Ojeda
"""

import numpy
import matplotlib.pyplot as plt
def sum2dice(N):
    count = [None] * N
    for i in range (0,N): 
        complete = 1
        counter = 0
        while complete:
            dice1 = numpy.random.randint(1,7)#represents 6 sided dice
            dice2 = numpy.random.randint(1,7)
            sum = dice1 + dice2#summation of 2 dice
            counter += 1
            if sum == 7:#if sum is 7 success
                complete = 0#end while
                count[i] = counter    
                
    b = range(1,30)
    sb = numpy.size(b)
    h1, bin_edges = numpy.histogram(count,bins = b)
    b1 = bin_edges[0:sb-1]
    plt.close('all')
    
    fig1 = plt.figure(1)
    p1 = h1/N
    plt.stem(b1,p1)
    plt.title('Sum of 2 Dice is 7: PMF')
    plt.xlabel('Number of rolls to get 7')
    plt.ylabel('Probability')  
    
    

print(sum2dice(100000))

                
    