# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 15:09:21 2019

@author: Jesus Ojeda
"""
import numpy
import matplotlib.pyplot as plt
n = 10000
beta = 40  
def exp_rv(beta,T):
    f=((1/beta)*numpy.exp(-(1/beta)*T))*numpy.ones(numpy.size(T))
    return f
def problem1b(beta,n):
    #Generate vales for RV X
    T = numpy.random.exponential(beta,n)
    nbins=30
    edgecolor='w'
    bins=[float(T) for T in numpy.linspace(0,220,nbins+1)]
    h1, bin_edges = numpy.histogram(T,bins,density=True)

    be1= bin_edges[0:numpy.size(bin_edges)-1]
    be2= bin_edges[1:numpy.size(bin_edges)]
    b1=(be1+be2)/2
    barwidth = b1[1]-b1[0]
    plt.close('all')

    fig1=plt.figure(1)
    plt.bar(b1,h1,width =barwidth, edgecolor = edgecolor)

    f=exp_rv(beta,b1)
    plt.plot(b1,f,'r')
    plt.title('1.2 PDF of a Random Variable "T"')
    plt.xlabel('T')
    plt.ylabel('PDF')
    
    mu_x = numpy.mean(T)
    sig_x = numpy.std(T)
    e_mean = beta
    e_std = beta
    print()
    print('Problem 1b:')
    print('Experimental Mean Measurement: ', mu_x)
    print('Theoretical Mean Calculation: ', e_mean)
    print('Experimental Standard Deviation Measurement: ', sig_x)
    print('Theoretical Standard Deviation Calculation: ', e_std)    
    
problem1b(beta,n)
