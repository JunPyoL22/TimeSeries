""" IID Bootstrap with Antithetic RV """
import numpy as np

n =100
iidSample = np.random.randn(n,1)
mu=np.mean(iidSample)
B= 1000
muStar = np.zeros((n,1))
iidSample = np.sort(iidSample)

for i in range(0,B,2):
    index = np.random.randint(n,size=(n,))
    muStar[i] = np.mean(iidSample[index])
    index = (n-1)-index
    muStar[i+1] = np.mean(iidSample[index])

np.correlate(muStar[list(range(0,B,2))],muStar[range(1,B,2)])
