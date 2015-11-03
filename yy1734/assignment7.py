# -*- coding: utf-8 -*-

import numpy as np
import math
import matplotlib.pyplot as plt



def questionOnetoThree():    
    # Question 1
    # 1 -1
  
    a1 = np.arange(1,16)
    
    a2 = a1.reshape((3,5)).T
    
    # 1-a containing the 2nd and 4th rows
    aa = a2[1::2,:]
    print "Question 1-a: " 
    print aa
    
    # 1-b: 2nd colum
    ab = a2[:,1]
    print "Question 1-b: " 
    print ab
    
    # 1-c: section between the coordinates [1,0] and [3,2]
    ac = a2[1:4,:]
    print "Question 1-c: " 
    print ac
    
    # 1-d: elements with values that are between 3 and 11
    ad = a2[(a2>=3)*(a2<=11)]
    print "Question 1-d: " 
    print ad
    
    # Question 2
    a = np.arange(25).reshape(5,5)
    b = np.array([1.,5,10,15,20])
    result = (a.T/b).T
    print "Question 2: " 
    print result
    
    # Question 3
    
    np.random.seed(1234)
    a1 = np.random.rand(10,3)
    
    a2 = abs(a1 - 0.5).argsort(axis = 1)
    a3 = a1[a2 == 0]
    print "Question 3: "
    print a3
    
    return
    
    
questionOnetoThree()
        
# Question 4

#construct grid
def grid(n):
    x = np.linspace(-2,1,n)
    y = np.linspace(-1.5,1.5,n)
    x2,y2 = np.meshgrid(x,y)
    return x2, y2
    
def fractal(n):
    n_max = 50
    threshold = 50
    
    x,y = grid(n)
    c = x + 1j*y
    
    z = c
    for v in range(n_max):
        z = z*z + c
    
    mask = (np.abs(z) < threshold)
    plt.imshow(mask.T, extent=[-2, 1, -1.5, 1.5])
    plt.gray()
    plt.savefig('mandelbrot.png')

fractal(1000)
    
    
        
