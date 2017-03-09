#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 21:46:17 2017

@author: congdonguyen
"""

import numpy as np
import matplotlib.pyplot as plt

#Load data
arr = np.loadtxt('trades.txt', comments="#", delimiter=None, skiprows=0, dtype=float)
arr = np.array(arr, dtype=float)

#Calculate balance changes and cumulative changes
balanceChanges = (arr[:,2]-arr[:,1])*arr[:,3]
cumBalanceChanges = balanceChanges.cumsum()

#Scat plot
def scatterPlot():
    plt.figure(1)
    colors = balanceChanges
    plt.scatter(range(len(arr)), cumBalanceChanges, c=colors, cmap=plt.cm.autumn)
    plt.plot(range(0,len(arr)), cumBalanceChanges)
    plt.title('Forex Account Balance')
    plt.xlabel('Day')
    plt.ylabel('Balance($)')
    plt.colorbar()
    plt.savefig("scatter.png", dpi=200)
    plt.close()
    
#Hist plot
def histPlot():
    plt.figure(2)
    plt.hist(balanceChanges, bins=30)
    plt.title('Gain/loss distribution')
    plt.xlabel('Gain/loss')
    plt.ylabel('Number of gain/loss')
    plt.savefig("histogram.png", dpi=200)
    plt.close()

#Pie plot
def piePlot():
    plt.figure(3)
    fraction = ['Positive','Negative','Zeros']
    positive = len(np.where(balanceChanges>0)[0])
    negative = len(np.where(balanceChanges<0)[0])
    zeros = len(np.where(balanceChanges==0)[0])
    numData = [positive, negative, zeros]
    plt.title("Trade results")
    plt.pie(numData, labels=fraction, shadow=True, autopct='%1.1f%%')
    plt.savefig("pie.png", dpi=200)
    plt.close()
    
#Call Plot
scatterPlot()
piePlot()
histPlot()
