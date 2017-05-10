##encoding=utf-8
#draw f(x) = x + 10*sin(5*x) + 7*cos(4*x) 在区间[0,9]的最大值
import numpy as np
import matplotlib.pyplot as plt
#numpy.arange( 0 , 2π ,0.01)  从0到2π，以0.01步进
x=np.arange(0,9,0.01)
y=x+10*np.sin(5*x)+7*np.cos(4*x)
plt.plot(x,y)
plt.show(1000)