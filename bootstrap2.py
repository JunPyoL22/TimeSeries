"""IID Balanced Boostrap"""

import numpy as np

n=100
B=1000
iidSample=np.random.randn(n,1)
mu = np.mean(iidSample)
muStar = np.zeros((B,1))
iidSampleRepl = np.tile(iidSample,(B,1))
u = np.random.permutation(n*B)

for i in range(B):
    index = list(n*(i)+np.arange(0,n))
    bootstrapSample = iidSampleRepl[u[index]]
    muStar[i] = np.mean(bootstrapSample)

s2 = np.sum((iidSample-mu)**2)*(1/(n-1))
stdErr = s2/n
bootstrapStdErr = np.mean((muStar-mu)**2)

print("s2:", s2)
print("stdErr:", stdErr)
print("bootstapStdErr:", boostrapStdErr)
