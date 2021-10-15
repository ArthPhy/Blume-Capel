import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import quad
from scipy.optimize import fsolve



def df(m,j,b,d,h):  # funçao zero
    U = 2*np.sinh(j*b*m+b*h)
    H = 2*np.cosh(j*b*m+b*h)+np.exp(b*d)
    return m - U/H

j = 4.0
d = 0.0
n = 1000
T = np.linspace(0.1,3,n)
b = 1/T
g = np.empty(n)
x = np.empty(n)
for i in range(n):
    g[i] = fsolve(df,1,args=(j,b[i],d,0))
    

h = 0.00001
gh = np.empty(n)
for i in range(n):
    gh[i] = fsolve(df,1,args=(j,b[i],d,h))



#	Faz o plot
fig, (ax1, ax2) = plt.subplots(2)
ax1.plot(T, g)
ax2.plot(T,(gh-g)/h)
ax1.set_ylabel('m')
ax2.set_ylabel('x')
ax2.set_xlabel('T')
ax1.text(2.5,0.93,'J = '+str(j))
ax1.text(2.5,0.80,'D = '+str(d))
plt.show()



