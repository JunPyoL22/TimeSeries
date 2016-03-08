""" IID Bootstrap with Antithetic RV """
import numpy as np

n =100
iidSample = np.random.randn(n,1)
mu=np.mean(iidSample)
B= 1000
muStar = np.zeros((B,1))
iidSample = np.sort(iidSample)

for i in np.arange(0,B,2):
    index = np.random.randint(n,size=(n,))
    xStar = iidSample[index]
    muStar[i] = np.mean(xStar)
    index = (n-1)-index
    xStar = iidSample[index]
    muStar[i+1] = np.mean(xStar)
x=muStar[range(0,B,2)]
y=muStar[range(1,B,2)]
# print (np.hstack((x,y)))
# print (len(x),len(y))
print(np.cov(np.hstack((x,y))))
print(np.corrcoef(np.hstack((x,y))))
