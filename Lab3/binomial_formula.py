# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 13:54:39 2019

@author: Jesus Ojeda
"""
import numpy
from scipy.stats import binom
import matplotlib.pyplot as plt 
def binomial():
    p = 0.20 * 0.10 * 0.15
    n = 1000
    q = 1 - p
    k = numpy.arange(0,20)
    y = binom.pmf(k, n, p)
    plt.stem(k, y)
    plt.title('Bernoulli Trials: PMF – Binomial Formula')
    plt.xlabel('Number of Successes in n = 1000 trials')
    plt.ylabel('Probability')
    plt.show()

binomial()