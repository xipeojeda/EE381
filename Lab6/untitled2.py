# -*- coding: utf-8 -*-
"""
Created on Thu May  9 20:09:52 2019

@author: Jesus Ojeda
"""

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import random
import matplotlib.lines as mlines


def main():

    n = 20
    initialProb = np.matrix([[0.2, 0.2, 0.2, 0.2, 0.2], [0, 0, 0, 0, 1.0]])
    transMatrix = np.matrix([[0, 1, 0, 0, 0], [0.5, 0, 0.5, 0, 0], [0.33, 0.33, 0, 0, 0.33], [1, 0, 0, 0, 0], [0, 0.33, 0.33, 0.33, 0]])
    result2 = np.zeros((n, 5))
    result = np.zeros((n, 5))
    initialProbability = initialProb[0, :]
    prob = initialProb[1, :]
    result[0, :] = initialProbability
    result2[0, :] = prob
    for j in range(0, n-1):
        result[j+1, :] = np.matmul(result[j, :], transMatrix)
        result2[j+1, :] = np.matmul(result2[j, :], transMatrix)

    nv = np.linspace(0, n, num=20)
    plt.figure()
    plt.plot(nv, result, marker='o', markersize=6)
    plt.title(('PageRank Probabilities: initial probability= ', np.str(initialProb[0, :])))
    plt.xlabel('Time step (n)')
    plt.ylabel('Probability of page visit')
    plt.legend((['A'], ['B'], ['C'], ['D'], ['E']))
    plt.show()

    plt.figure()
    plt.plot(nv, result2, marker='o', markersize=6)
    plt.title(('PageRank Probabilities: initial probability= ', np.str(initialProb[1, :])))
    plt.xlabel('Time step (n)')
    plt.ylabel('Probability of page visit')
    plt.legend((['A'], ['B'], ['C'], ['D'], ['E']))
    plt.show()



main()