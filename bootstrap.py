import numpy as np
# import matplotlib.pyplot as plt

n = 100
iidSample = np.random.randn(n,1)
mu = np.mean(iidSample)
B = 1000
muStar = np.zeros((B,1))
for i in range(B):
    order = list(np.random.randint(n,size=(n,)))
    bootstrapSample = iidSample[order]
    muStar[i] = np.mean(bootstrapSample)
s2 = np.sum((iidSample-mu)**2)*(1/(n-1))
stdErr = s2/n
bootstrapStdErr = np.mean((muStar-mu)**2)

print("s2:", s2)
print("stdErr:", stdErr)
print("bootstapStdErr:", boostrapStdErr)
