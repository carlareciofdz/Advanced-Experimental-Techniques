# first , it ’s important to import the numpy library
import numpy as np
# Second , we define the modulation factor vector
M= [0.1 , 0.25, 0.5, 0.75, 1];
# we define the function T/P with a linspace in the first part (linear part)
TP1 = np.linspace (0, 0.5 , 100);
print (TP1)
# with this linespace we conmute the value of the second factorial moment
#in the first zone
# For 0<T<P/2
n21 = np.zeros((100,5));
for i in range(100):
    for j in range(5):
        n21[i,j] = (1-(4/3)*TP1[i])*M[j]**2+1;

print(n21)
# we define the function T/P with a linspace in the second part
TP2 = np.linspace (0.5, 1, 100);
print(TP2)
# For P/2<T<P
n22 = np.zeros((100,5));
for i in range(100):
    for j in range(5):
        n22[i,j] = ((4/3)*TP2[i]-(1/3)*TP2[i]**(-2)+(2)*TP2[i]**(-1)-3)*M[j]**2+1;
print(n22)
# plotting n21 y n22
import matplotlib.pyplot as plt
plt.plot(TP1, n21[:,0], 'k', label=r'M=0.1')
plt.plot(TP2, n22[:,0], 'k')
plt.plot(TP1, n21[:,1], 'm', label=r'M=0.25')
plt.plot(TP2, n22[:,1], 'm')
plt.plot(TP1, n21[:,2], 'g', label=r'M=0.5')
plt.plot(TP2, n22[:,2], 'g')
plt.plot(TP1, n21[:,3], 'r', label=r'M=0.75')
plt.plot(TP2, n22[:,3], 'r')
plt.plot(TP1, n21[:,4], 'b', label=r'M=1')
plt.plot(TP2, n22[:,4], 'b')
plt.xlabel(r'$T/P$')
plt.ylabel(r'$n^{(2)}(T)$')
plt.legend()
#plt.grid()
plt.xlim(0, 1)

plt.show()
