# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 14:06:38 2019

@author: Jesus Ojeda
"""

#Simulate a manufacturing process
#Creating steel bearing
#-Total number of bearings: N=1,500,000 --> Generate
#-Population mean: μ = 55  grams; --> mean weight
#-Population standard deviation: σ= 5  grams; --> standard deviation weight
#-Sample sizes: n= 1, 2, ... 200

#Choose a random sample of size n
#Find the mean weight of the sample
#Repeat for n = 1,2,3...200
#Plot x with respect to n
import numpy as np
import matplotlib.pyplot as plt
import random as r
import math as m 

def problem1():
    N = 1500000
    mu = 55
    sig = 5
    n = 200
    B = np.random.normal(mu,sig,N)
    mean = [None] * n
    top95 = [None] * n
    bottom95 = [None] * n
    top99 = [None] * n
    bottom99 = [None] * n
    for c in range (0,n):
        counter = c+1 
        x = B[r.sample(range(N), counter)]
        mean[c] = np.sum(x)/counter
        std = sig/m.sqrt(counter)
        top95[c] = mu + 1.96*(std)
        bottom95[c] = mu - 1.96*(std)
        top99[c] = mu + 2.58*(std)
        bottom99[c] = mu - 2.58*(std)
   
    list2 = [x for x in range(1, counter+1)] 
    
    plt.close('all')
    
    fig1 = plt.figure(1)
    plt.scatter(list2, mean, c = 'Blue', marker = 'x')
    plt.plot(list2, top95, 'r--')
    plt.plot(list2, bottom95, 'r--')
    plt.title('Sample Means & 95% confidence intervals')
    plt.xlabel('Sample Size')
    plt.ylabel('x_bar')
    
    fig2 = plt.figure(2)
    plt.scatter(list2, mean, c = 'Blue', marker = 'x')
    plt.plot(list2, top99, 'g--')
    plt.plot(list2, bottom99, 'g--')
    plt.title('Sample Means & 99% confidence intervals')
    plt.xlabel('Sample Size')
    plt.ylabel('x_bar')
    
problem1()