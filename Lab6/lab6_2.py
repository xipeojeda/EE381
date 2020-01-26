# -*- coding: utf-8 -*-
"""
Created on Thu May  9 20:05:10 2019

@author: Jesus Ojeda
"""

import numpy as np
from matplotlib import pylab as pyplt
from matplotlib.legend_handler import HandlerLine2D
import random

initial = [0,1/3,1/3,1/3,0]
states = [0,1,2,3,4]
state0 = [1,0,0,0,0]
state1 = [0.3,0,0.7,0,0]
state2 = [0,0.5,0,0.5,0]
state3 = [0,0,0.6,0,0.4]
state4 = [0,0,0,0,1]
n = 15
N = 10000
zeroCounter, fourCounter = 0, 0

def weightTransition(num):
    chain = []
    prev = np.random.choice(states, 1, p = initial)
    chain.append(prev[0])
    for i in range(n-1):
        if(prev == 0):
            prev = np.random.choice(states, 1, p = state0)
            chain.append(prev[0])
        elif(prev == 1):
            prev = np.random.choice(states, 1, p = state1)
            chain.append(prev[0])
        elif(prev == 2):
            prev = np.random.choice(states, 1, p = state2)
            chain.append(prev[0])
        elif(prev == 3):
            prev = np.random.choice(states, 1, p = state3)
            chain.append(prev[0])
        elif(prev == 4):
            prev = np.random.choice(states, 1, p = state4)
            chain.append(prev[0])
    return chain


for i in range(N):
    ch = weightTransition(n)
    if(ch[14] == 0):
        zeroCounter += 1
    elif(ch[14] == 4):
        fourCounter += 1

print(zeroCounter/N, fourCounter/N)