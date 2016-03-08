"""Percentile Method"""
from numpy import *
import numpy as np

n=100
x=random.randn(n,1)
mu = np.mean(x)
B=1000
muStar =  np.zeros((B,1))

for i in range(B):
    index = random.randint(n,size=(n,))
    xStar = x[index]
    muStar[i]=np.mean(xStar)

alphaL = 0.5
alphaH = 0.95

muStar = np.sort(muStar)
CI = [muStar[alphaL*B],muStar[alphaH*B]]
print(CI)
print (mu)
print(CI-mu)
