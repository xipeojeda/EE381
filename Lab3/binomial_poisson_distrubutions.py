# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 14:04:02 2019

@author: Jesus Ojeda
"""
#p=[0.2,  0.1,  0.15, 0.3, 0.2, 0.05]
import numpy
import matplotlib.pyplot as plt
def bernoulli_trials(c,n,p):
    count = 0
   
    x1 = numpy.random.choice(c,n,p=p)
    x2 = numpy.random.choice(c,n,p=p)
    x3 = numpy.random.choice(c,n,p=p)
    for i in range(0,n):
        if x1[i] == 1 and x2[i] == 2 and x3[i] == 3:
            count+=1     
    return count
            
def test1():
    c = [1,2,3,4,5,6]
    p = [0.2,  0.1,  0.15, 0.3, 0.2, 0.05]
    N = 10000
    n = 1000
    s = numpy.zeros((N,1))
    for i in range(0,N):
        r = bernoulli_trials(c,n,p)
        s[i] = r
    b = range(0,30)
    sb=numpy.size(b)
    h1,bin_edges=numpy.histogram(s,bins=b)
    b1=bin_edges[0:sb-1]
    plt.close('all')
    prob=h1/N
    plt.stem(b1,prob)

print(test1())