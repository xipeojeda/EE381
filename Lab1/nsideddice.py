# -*- coding: utf-8 -*-
"""
Created on Wed Jan 23 20:12:50 2019

@author: Jesus Ojeda
"""
#Use following probability vector :
#p=[0.10,  0.15,  0.20,  0.05,  0.30, 0.10, 0.10]
import numpy
import matplotlib.pyplot as plt

def nSidedDie(p):
   N = 10000
   n = numpy.size(p)
   cs = numpy.cumsum(p)
   cp = numpy.append(0,cs)
   
   for j in range(0,N): #rolling die N times
       r = numpy.random.rand()
       for k in range(0,n):
           if r>cp[k] and r <=cp[k+1]:
               d=k+1
       return d

def tester():
    #array to pass in 
    p = numpy.array([0.10,  0.15,  0.20,  0.05,  0.30, 0.10, 0.10])
    N = 10000
    s = numpy.zeros((N,1))
    for i in range(0,N):
        r=nSidedDie(p)
        s[i]=r
    b=range(1,numpy.size(p)+2)
    sb=numpy.size(b)
    h1,bin_edges=numpy.histogram(s,bins=b)
    b1=bin_edges[0:sb-1]
    plt.close('all')
    prob=h1/N
    plt.stem(b1,prob)

    plt.title('PMF for an unfair n-sided die')
    plt.xlabel('Number on the face of the die')
    plt.ylabel('Probability')
    plt.xticks(b1)

print(tester())