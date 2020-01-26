# -*- coding: utf-8 -*-
"""
Created on Thu May  9 20:11:11 2019

@author: Jesus Ojeda
"""

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import random
import matplotlib.lines as mlines



def main():

    n = 15  # 15 times
    N = 10000
    throws = []
    throws = np.zeros(n)
    count0 = 0
    count4 = 0

    for j in range(N):
        initialThrow = nsideddie([0, 0, 1, 0, 0])
        throws[0] = initialThrow
        for i in range(n-1):

            if initialThrow == 0:
                initialThrow = nsideddie([1, 0, 0, 0, 0])
                throws[i+1] = initialThrow

            elif initialThrow == 1:
                initialThrow = nsideddie([0.3, 0, 0.7, 0, 0])
                throws[i+1] = initialThrow

            elif initialThrow == 2:
                initialThrow = nsideddie([0, 0.5, 0, 0.5, 0])
                throws[i+1] = initialThrow

            elif initialThrow == 3:
                initialThrow = nsideddie([0, 0, 0.6, 0, 0.4])
                throws[i+1] = initialThrow

            elif initialThrow == 4:
                initialThrow = nsideddie([0, 0, 0, 0, 1])
                throws[i+1] = initialThrow

        if throws[len(throws) -1] == 0:
            count0 += 1
        if throws[len(throws) - 1] == 4:
            count4 += 1

    print(str(count0/N) + 'ABSORPTION FOR 0 ENDING')
    print(str(count4/N) + 'ABSORPTION FOR 4 ENDING')


def nsideddie(p):
    n = len(p)  # length of the array p tell us the
                # how many sides the die has

    cs = np.cumsum(p)
    cp = np.append(0, cs)

    r = np.random.rand()
    for k in range(0, n):

        if r > cp[k] and r <= cp[k + 1]:
            d = k

    return d



main()