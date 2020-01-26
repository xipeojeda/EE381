# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 13:57:56 2019

@author: Jesus Ojeda
"""
#  Use the following probabilities for this project: 
#  p0=0.6   ;   e0=0.05;   e1=0.03
import numpy
def signal(N, p0, e0, e1):
    count = 0 
    r=0
    for i in range(0,N):
        s = nSidedDie(p0, 1-p0)-1
        if s == 1:
          r = nSidedDie(e1, 1-e1)-1
        else:
          r = nSidedDie(1-e0, e0)-1
        if r!=s:
            count+=1
    print("Probability of Erroneous Transmission:", (count)/N)

#only focus in those transmissions where S = 1
def signal2(N, p0, e0, e1):
    countS = 0
    countR = 0
    r = 0
    for i in range(0,N):
        s = nSidedDie(p0, 1-p0)-1
        if s == 1:
            countS+=1
            r = nSidedDie(e1, 1-e1)-1
            if r == 1:
              countR+=1
        else:
          r = nSidedDie(1-e0, e0)-1
    print("Conditional probability of P(R=1|S=1):", countR/countS)
    
#only focus in those transmissions where R = 1
def signal3(N, p0, e0, e1):
    countS = 0
    countR = 0
    r = 0
    for i in range(0,N):
        s = nSidedDie(p0, 1-p0)-1
        if s == 1:
          r = nSidedDie(e1, 1-e1)-1
        else:
          r = nSidedDie(1-e0, e0)-1
          
        if r == 1: 
            countR += 1
            if s == 1:
                countS+=1
          
    print("Conditional probability of P(S=1|R=1):", countS/countR)
#problem 4
#comparing original to decoded
#decoded part is received from majority rule from r1,r2,r3
def enhancedTransmission(N,p0,e0,e1):
    count = 0
    decode = -1
    rSum = 0
    sList = []
    rList = []
    for i in range(0, N):
        #creating a list of 3 "S" transmissions
         s = nSidedDie(p0, 1-p0)-1
         sList = [s,s,s]
         if 1 in sList:
              rList = [nSidedDie(e1, 1-e1)-1,nSidedDie(e1, 1-e1)-1,nSidedDie(e1, 1-e1)-1]
         if 0 in sList:    
              rList = [nSidedDie(1-e0, e0)-1,nSidedDie(1-e0, e0)-1,nSidedDie(1-e0, e0)-1]
         rSum = numpy.sum(rList)
         if rSum >= 2:
             decode = 1
         else:
             decode = 0
         if decode != s:
             count+=1
    print("Probability of error with enhanced transmission: ", count/N)
         
def nSidedDie(p0,p1):
    n = 2
    p = numpy.array([p0,p1])
    cs = numpy.cumsum(p)
    cp = numpy.append(0,cs)
    r = numpy.random.rand()
    for k in range (0,n):
        if r > cp[k] and r <=cp[k+1]:
            d=k+1
    return d
    
print(signal(100000,0.6,0.05,0.03))
print(signal2(100000,0.6,0.05,0.03))
print(signal3(100000,0.6,0.05,0.03))
print(enhancedTransmission(100000,0.6,0.05,0.03))