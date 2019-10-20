from matplotlib import cm
import numpy as np
import matplotlib.pyplot as plt
from numpy import random
import matplotlib.animation as animation
plt.style.use('fivethirtyeight')


def Duck_walk(n,p = True,co= False,x=0 ,y=0):
    '''simulating a random walk with n number of steps
     p = true : return path
     co = true: return final coordinates
     x,y are the starting co-ordinates of the walk
     '''
    pos_x = x
    pos_y = y
     
    path = [(pos_x,pos_y)]
    for i in range(n):
        step = random.choice(['N','S','E','W'])
        if step == 'N':
            pos_y += 1
            path.append((pos_x,pos_y))
        if step == 'S':
            pos_y -= 1       
            path.append((pos_x,pos_y))
        if step == 'E':
            pos_x += 1
            path.append((pos_x,pos_y))
        if step == 'W':
            pos_x -= 1
            path.append((pos_x,pos_y))
    if p == True:
        return path
    if co == True:
        return (x,y)

def anim(trials):
    ''' function to be called by funcAnimation changing only trials
        x,y initial coordinates of path_2
        n: steps of path_1
        n_2: steps of path_2
        '''
        
    x=6
    y=0
    n=5
    n_2=10
    Find_intersect(x,y,n,n_2,trials)
    print(trials)

def Find_intersect(x,y,n=10,n_2=10,trials = 10):
    ''' plot walk 1 n steps at origin 
        plot walk 2 n_2 steps at x,y
        find intersection points intersect =[]
        count number of intersects: len(intersect)
        '''
    '''we are preparing the color array by normalizing trials'''
    
    trial = [i for i in range(trials)]
    tmin,tmax = min(trial),max(trial)
    for i, val in enumerate(trial):
          trial[i] = (val-tmin) / (tmax-tmin)
          
    intersects = []
    
    for i in trial:
        
        path_1 =Duck_walk(n)
        path_2 =Duck_walk(n_2,x=x,y=y)

        color_1 = plt.cm.Purples(i)    
        xs,ys = zip(*path_1)
        plt.plot(xs,ys,color= color_1)
        plt.grid(True)
        plt.title('walking duck')
    
        color_2 = plt.cm.Wistia(i)    
        xs,ys = zip(*path_2)
        plt.plot(xs,ys,color= color_2)
        plt.grid(True)
        plt.title('Walking ducks')
        
        for i_1 in path_1:
            for i_2 in path_2:
                if i_1 == i_2:
                    intersects.append(i)
    p_inter = (len(intersects)*100)/trials
    print('the probability of two ducks meeting:')
    print(p_inter,'%')
        
    
    

    
t = [i for i in range(5,300,20)]
    
fig = plt.figure()
anim = animation.FuncAnimation(fig,anim,frames=t,interval= 200)
plt.show()
anim.save('animation.gif', writer='imagemagick', fps=3)