# -*- coding: utf-8 -*-
"""
Created on Sun Sep 24 18:03:56 2017

"""

import matplotlib.pyplot as plt
import numpy as np
'''
0-10  -1 with weight 10
10-20 -11 with weight 1
20-30 -21 with weight 40 and so on....
'''

plt.hist([1,11,21,31,41], bins=[0,10,20,30,40,50], weights=[10,1,40,33,6]);
plt.title("Gaussian Histogram")
plt.xlabel("Value")
plt.ylabel("Frequency")


#number of bins equals to take the square root of the total number of values in your distribution.
#If False, the result will contain the number of samples in each bin. 
#If True, the result is the value of the probability density function at the bin, 
#normalized such that the integral over the range is 1

gaussian_numbers = np.random.randn(10) #generates 10 random numbers
print(gaussian_numbers)
plt.hist(gaussian_numbers,25,normed=True) # data,bin,probability distribution
plt.title("Gaussian Histogram")
plt.xlabel("Value")
plt.ylabel("Frequency")


import matplotlib.pyplot as plt
from numpy.random import normal, uniform
gaussian_numbers = normal(size=1000)
uniform_numbers = uniform(low=-3, high=3, size=1000)
plt.hist(gaussian_numbers, bins=20, histtype='stepfilled', normed=True, color='b', label='Gaussian')
plt.hist(uniform_numbers, bins=20, histtype='stepfilled', normed=True, color='r', alpha=0.5, label='Uniform')
plt.title("Gaussian/Uniform Histogram")
plt.xlabel("Value")
plt.ylabel("Probability")
plt.legend()
plt.show()
