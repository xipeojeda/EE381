# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 15:41:53 2019

@author: Jesus Ojeda
"""
import numpy
import matplotlib.pyplot as plt
n = 10000
mu = 2.5
sigma = 0.75 
def normal_rv(sigma,mu,T):
    f=(1/(sigma*numpy.sqrt(2 *numpy.math.pi)))*numpy.exp(-((T-mu)**2)/(2*sigma)**2)*numpy.ones(numpy.size(T))
    return f
def problem1c(sigma,mu,n):
    #Generate vales for RV X
    T = numpy.random.normal(mu,sigma,n)
    nbins=30
    edgecolor='w'
    bins=[float(T) for T in numpy.linspace(0,5,nbins+1)]
    h1, bin_edges = numpy.histogram(T,bins,density=True)

    be1= bin_edges[0:numpy.size(bin_edges)-1]
    be2= bin_edges[1:numpy.size(bin_edges)]
    b1=(be1+be2)/2
    barwidth = b1[1]-b1[0]
    plt.close('all')

    fig1=plt.figure(1)
    plt.bar(b1,h1,width =barwidth, edgecolor = edgecolor)

    f=normal_rv(sigma,mu,b1)
    plt.plot(b1,f,'r')
    plt.title('1.3 PDF of a Random Variable "X"')
    plt.xlabel('X')
    plt.ylabel('PDF')
    mu_x = numpy.mean(T)
    sig_x = numpy.std(T)
    e_mean = mu
    e_std = sigma
    print()
    print('Problem 1c:')
    print('Experimental Mean Measurement: ', mu_x)
    print('Theoretical Mean Calculation: ', e_mean)
    print('Experimental Standard Deviation Measurement: ', sig_x)
    print('Theoretical Standard Deviation Calculation: ', e_std)    
    
problem1c(sigma,mu,n)
