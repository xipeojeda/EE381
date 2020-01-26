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

ch = weightTransition(n)
x = np.array(ch)
pyplt.figure()
pyplt.yticks([0,1,2,3,4])
pyplt.ylim([-.5, 4.5])
line1, = pyplt.plot(x, linestyle='--', marker = ".", 
                    markerfacecolor = 'red', markersize = '12')
pyplt.title('A simulation run of a three-stage Markov Chain')
pyplt.ylabel('State')
pyplt.xlabel('Step Number')
pyplt.show()