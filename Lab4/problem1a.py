"""
Created on Thu Mar 14 13:47:39 2019

@author: Jesus Ojeda
"""

#PROBLEM 1. The parameter values are    (P1a).   a=1.0 ;  b=4.0  ; (P1b).   beta =40 ;   (P1c).   mu=2.5  ;  sigma= 0.75
n = 10000
#(P1a)
a = 1.0  
b = 4.0
import numpy
import matplotlib.pyplot as plt
def uniform_rv(a,b,X):
    f = (1/abs(b-a))*numpy.ones(numpy.size(X))
    return f
def problem1a(a,b,n):
    #Generate vales for RV X
    X = numpy.random.uniform(a,b,n)
    nbins = 30
    edgecolor = 'w'
    bins = [float(X) for X in numpy.linspace(a,b,nbins + 1)]
    h1, bin_edges = numpy.histogram(X, bins,density = True)
    be1 = bin_edges[0:numpy.size(bin_edges)-1]
    be2 = bin_edges[1:numpy.size(bin_edges)]
    b1 = (be1 + be2)/2
    barwidth = b1[1] -b1[0]
    plt.close('all')
    
    #plot bar graph
    fig1 = plt.figure(1)
    plt.bar(b1,h1,width = barwidth,edgecolor=edgecolor)
    
    f = uniform_rv(a,b,b1)
    plt.plot(b1,f,'r')
    plt.title('1.1 PDF of a Random Variable "X"')
    plt.xlabel('X')
    plt.ylabel('PDF')
    
    #calculate the mean and standard deviation
    mu_x = numpy.mean(X)
    sig_x = numpy.std(X)
    e_mean = (a+b)/2
    e_std = ((b-a)**(2))/12
    print('Problem 1a:')
    print('Experimental Mean: ', mu_x)
    print('Theoretical Mean: ', e_mean)
    print('Experimental Standard Deviation: ', sig_x)
    print('Theoretical Standard Deviation: ', e_std)
problem1a(a,b,n)

