# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 22:08:36 2018

"""
import statistics
import numpy as np

print(statistics.mean([1, 2, 3, 4, 4]))
print(statistics.mean([-1.0, 2.5, 3.25, 5.75]))
from fractions import Fraction as F

print(statistics.mean([F(3, 7), F(1, 21), F(5, 3), F(1, 3)]))

print(F(3,67))

from decimal import Decimal as D

print(statistics.mean([D("0.5"), D("0.75"), D("0.625"), D("0.375")]))
#harmonic mean
print(statistics.harmonic_mean([2.5, 3, 10]))
#median
print(statistics.median([1, 3,4, 5]))
#median high
print(statistics.median_high([1, 3, 5, 7]))

#mode
print(statistics.mode(["red", "blue", "blue", "red", "green", "red", "red"]))

# print(statistics.mode([1,1,2,2]))
# 'no unique mode; found %d equally common values' % len(table)

#std] 
a = np.array([[1, 2], [3, 4]])
print(np.std(a))
#variance
print(np.var(a))

var = np.array([10, 7, 4, 3, 2, 1]) # input array

print(np.percentile(var, np.arange(0, 100, 25))) # quartiles
#array([ 1.  ,  2.25,  3.5 ,  6.25]) # output

print(np.percentile(var, np.arange(0, 100, 10))) # deciles
#array([ 1. ,  1.5,  2. ,  2.5,  3. ,  3.5,  4. ,  5.5,  7. ,  8.5]) #output
