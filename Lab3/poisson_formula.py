# -*- coding: utf-8 -*-
"""
Created on Sat Mar  9 01:58:35 2019

@author: Jesus Ojeda
"""
import numpy
from scipy.stats import poisson
import matplotlib.pyplot as plt 
def poisson_approx():
    n = 1000
    p = 0.20 * 0.10 * 0.15
    lamda = n*p
    k = numpy.arange(0,20)
    y = poisson.pmf(k,lamda)
    plt.stem(k,y)
    plt.title('Bernoulli Trials: PMF – Poisson Approximation')
    plt.xlabel('Number of Successes in n = 1000 trials')
    plt.ylabel('Probability')
    plt.show

poisson_approx()