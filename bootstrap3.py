""" IID Bootstrap with Antithetic RV """
import numpy as np

n =100
bootstrapSample = np.random.randn(n,1)
mu=np.mean(bootstrapSample)
B= 1000
muStar = np.zeros((n,1))
bootstrapSample = np.sort(bootstrapSample)

for i in range(0,B,2):
    index = np.random.randint(n,size=(n,))
    muStar[i] = np.mean(bootstrapSample[index])
    index = n-index
    muStar[i+1] = np.mean(bootstrapSample[index])

np.correlate(muStar[list(range(0,B,2))],muStar[range(1,B,2)])
