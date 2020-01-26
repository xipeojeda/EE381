# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 16:14:57 2019

@author: Irvin
"""

import numpy as np
import matplotlib
import matplotlib.pyplot as plt

def gaussian(mu_x,sig_x,z):
    f = np.exp(-(z-mu_x)**2/(2*sig_x**2))/(sig_x*np.sqrt(2*np.pi))
    return f


def q2(nbooks):
    N= 10000
    a =1
    b =4
    mu_x = (a+b)/2
    sig_x= np.sqrt((b-a)**2/12)
    X = np.zeros((N,1))
    for k in range(0,N):
        x = np.random.uniform(a,b,nbooks)
        w = np.sum(x)
        X[k]=w
        
    
    nbins=40; # Number of bins
    edgecolor='w'; # Color separating bars in the bargraph
    #
    bins=[float(x) for x in np.linspace(nbooks*a, nbooks*b,nbins+1)]
    h1, bin_edges = np.histogram(X,bins,density=True)
    # Define points on the horizontal axis
    be1=bin_edges[0:np.size(bin_edges)-1]
    be2=bin_edges[1:np.size(bin_edges)]
    b1=(be1+be2)/2
    barwidth=b1[1]-b1[0] # Width of bars in the bargraph
    plt.close('all')
   
    fig1=plt.figure(1)
    plt.bar(b1,h1, width=barwidth, edgecolor=edgecolor)
    f = gaussian(mu_x*nbooks,sig_x*np.sqrt(nbooks),b1)
    plt.plot(b1,f,'r')
    plt.title('PDF of book stack height and comparison with Gaussian')
    plt.xlabel('Book stack height for n = 15 books')
    plt.ylabel('PDF')
    
    mu_x = np.mean(X)
    print(mu_x)
    sig_x = np.std(X)
    print(sig_x)
    mu_formula = nbooks*mu_x
    sig_formula = mu_x * np.sqrt(nbooks)
    
q2(15)