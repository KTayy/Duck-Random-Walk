# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 22:52:53 2019
simulating a random walk
@author: LENOVO
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib.colors as col
import random 
from matplotlib.cm import get_cmap
from matplotlib.colors import PowerNorm


def Duck_walk(n,p,coordinates):
    'simulating a random walk with n number of steps'
    x,y = 0,0
    path = []
    for i in range(n):
        (dx,dy) = random.choice([(1,0),(0,1),(-1,0),(0,-1)])
        x += dx
        y += dy
        path.append((x,y))
    if p == True:
        return path
    if coordinates == True:
        return (x,y)
    
def Plot_walk(n):
    'plotting the simulated random walk'
    net_walks =[]
    for i in range(1,n+1):
        
        #find the path
        path = Duck_walk(i,True,False)
        
        #seperate values x and y from path
        xs,ys =zip(*path)
        x,y = Duck_walk(i,False,True)
        #find net distance
        net_walk = abs(x) + abs(y)
        net_walks.append(net_walk)
        
        #plot the results
        plt.plot(xs,ys)
        plt.grid(True)
        plt.title('walking duck')
        plt.show()
        
    
        
Plot_walk(1000)

        
    
  
    

        
        



