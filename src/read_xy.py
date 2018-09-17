import pylab as pl
infile=open("../data/xy.dat","r")
import numpy as np

x=[]
y=[]
for line in infile:
    x_,y_=[float(w)for w in line.split()]
    x.append(x_)
    y.append(y_)
infile.close()
x=np.array(x)
y=np.array(y)
pl.plot(x,y)
pl.show()
print(max(y))
print(min(y))
