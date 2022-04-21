
# Exercise2 
import  numpy as np 
from operator import add 
import math
import signal 
import matplotlib.pyplot as plt 
#make a linsapce
t = np.linspace(-10,10,1000) 

funcl = [] 
func2 = []
func3 = []
func4 = [] 

for i in range (len(t)): 
    funcl.append(math.sin(2*t[i])+3) 
    func2.append(math.sin(3*t[i])+2)
    func3.append(math.cos(2*t[i])+3) 
    func4.append(math.cos(3*t[i])+2) 
a1=list (map(add, funcl, func2)) 
a2=list (map(add, func3, func4)) 
signal = list(map(add, a1 ,a2)) 
 # plot the signal that generate from sin and cos

plt.plot( t,signal) 
plt.title("The periodic singal")
plt.xlabel ("Values of t") 
plt.ylabel ("Values of singal") 
#plt.show()
#fft = np.fft.fft(signal)
#plt.plot(fft)
#plt.show()
noise = np.random.normal(0,1,1000) 
plt.subplot(211)
plt.plot(t,signal); plt.title('wave')
plt.subplot(212)
plt.plot(t,signal+noise) ; plt.title('noisy wave')
plt.show()
fft = np.fft.fft(signal+noise)
plt.plot(fft)
plt.show()