import numpy as np
from scipy.optimize import minimize
import matplotlib.pyplot as plt

# Definición de las medidas
med1 = [1.209443, 1.191362, 1.151709, 1.113285, 1.074993, 1.051908, 1.027126, 1.012847, 1.003128, 0.999993]
med2 = [1.211220, 1.183132, 1.148188, 1.145329, 1.082458, 1.051098, 1.027108, 1.012718, 1.003537, 0.999988]
med3 = [1.210304, 1.188723, 1.137770, 1.090090, 1.071441, 1.051151, 1.027150, 1.012774, 1.002514, 0.999986]
med4 = [1.219251, 1.177786, 1.147447, 1.097841, 1.098259, 1.052040, 1.027577, 1.012909, 1.002424, 0.999987]
med5 = [1.224337, 1.182249, 1.155211, 1.098738, 1.022527, 1.051177, 1.026870, 1.012891, 1.002316, 0.999986]
med6 = [1.215287, 1.187225, 1.146810, 1.098564, 1.083576, 1.054503, 1.027421, 1.012748, 1.003328, 0.999989]
med7 = [1.213535, 1.191360, 1.158022, 1.092774, 1.092919, 1.051625, 1.026453, 1.012694, 1.003243, 0.999994]
med8 = [1.217230, 1.175413, 1.140837, 1.128617, 1.060242, 1.051857, 1.027322, 1.012928, 1.002300, 0.999988]
med9 = [1.224528, 1.183652, 1.149073, 1.086520, 1.072258, 1.050512, 1.026762, 1.012975, 1.001746, 0.999992]
med10 = [1.217990, 1.197390, 1.152143, 1.108644, 1.093941, 1.051457, 1.026282, 1.012940, 1.002342, 0.999986]
media = [1.216313, 1.185829, 1.148721, 1.106040, 1.075262, 1.051733, 1.027007, 1.012842, 1.002688, 0.999989]

# Lista de medidas
medidas = [med1, med2, med3, med4, med5, med6, med7, med8, med9, med10]

# Calculating the deviation
desviacion = np.zeros(10)
for i in range(10):
    desviacion[i] = np.sqrt(((med1[i] - media[i])**2 + (med2[i] - media[i])**2 + 
                              (med3[i] - media[i])**2 + (med4[i] - media[i])**2 + 
                              (med5[i] - media[i])**2 + (med6[i] - media[i])**2 + 
                              (med7[i] - media[i])**2 + (med8[i] - media[i])**2 + 
                              (med9[i] - media[i])**2 + (med10[i] - media[i])**2) / 9)
print("la desviación es :", desviacion)


# Creating ten functions and minimizing each of those 10 functions
# where M[0] = M and M[1] = P
from scipy.optimize import minimize

# Definir las funciones para cada medida
def function1(M):
    y1 = (med1[0] - ((1 - (4/3) * (1/M[1])) * M[0]**2 + 1))**2 / 10 + \
          (med1[1] - ((1 - (4/3) * (2/M[1])) * M[0]**2 + 1))**2 / 10 + \
          (med1[2] - ((1 - (4/3) * (3/M[1])) * M[0]**2 + 1))**2 / 10 + \
          (med1[3] - ((1 - (4/3) * (4/M[1])) * M[0]**2 + 1))**2 / 10 + \
          (med1[4] - ((1 - (4/3) * (5/M[1])) * M[0]**2 + 1))**2 / 10 + \
          (med1[5] - (((4/3) * (6/M[1]) - (1/3) * M[1]**2 / 36 + 2 * M[1] / 6 - 3) * M[0]**2 + 1))**2 / 10 + \
          (med1[6] - (((4/3) * (7/M[1]) - (1/3) * M[1]**2 / 49 + 2 * M[1] / 7 - 3) * M[0]**2 + 1))**2 / 10 + \
          (med1[7] - (((4/3) * (8/M[1]) - (1/3) * M[1]**2 / 64 + 2 * M[1] / 8 - 3) * M[0]**2 + 1))**2 / 10 + \
          (med1[8] - (((4/3) * (9/M[1]) - (1/3) * M[1]**2 / 81 + 2 * M[1] / 9 - 3) * M[0]**2 + 1))**2 / 10 + \
          (med1[9] - (((4/3) * (10/M[1]) - (1/3) * M[1]**2 / 100 + 2 * M[1] / 10 - 3) * M[0]**2 + 1))**2 / 10
    return y1

def function2(M):
    y2 = (med2[0] - ((1 - (4/3) * (1/M[1])) * M[0]**2 + 1))**2 / 10 + \
          (med2[1] - ((1 - (4/3) * (2/M[1])) * M[0]**2 + 1))**2 / 10 + \
          (med2[2] - ((1 - (4/3) * (3/M[1])) * M[0]**2 + 1))**2 / 10 + \
          (med2[3] - ((1 - (4/3) * (4/M[1])) * M[0]**2 + 1))**2 / 10 + \
          (med2[4] - ((1 - (4/3) * (5/M[1])) * M[0]**2 + 1))**2 / 10 + \
          (med2[5] - (((4/3) * (6/M[1]) - (1/3) * M[1]**2 / 36 + 2 * M[1] / 6 - 3) * M[0]**2 + 1))**2 / 10 + \
          (med2[6] - (((4/3) * (7/M[1]) - (1/3) * M[1]**2 / 49 + 2 * M[1] / 7 - 3) * M[0]**2 + 1))**2 / 10 + \
          (med2[7] - (((4/3) * (8/M[1]) - (1/3) * M[1]**2 / 64 + 2 * M[1] / 8 - 3) * M[0]**2 + 1))**2 / 10 + \
          (med2[8] - (((4/3) * (9/M[1]) - (1/3) * M[1]**2 / 81 + 2 * M[1] / 9 - 3) * M[0]**2 + 1))**2 / 10 + \
          (med2[9] - (((4/3) * (10/M[1]) - (1/3) * M[1]**2 / 100 + 2 * M[1] / 10 - 3) * M[0]**2 + 1))**2 / 10
    return y2

# Repetir el proceso para las medidas 3 a 10
def function3(M):
    y3 = (med3[0] - ((1 - (4/3) * (1/M[1])) * M[0]**2 + 1))**2 / 10 + \
          (med3[1] - ((1 - (4/3) * (2/M[1])) * M[0]**2 + 1))**2 / 10 + \
          (med3[2] - ((1 - (4/3) * (3/M[1])) * M[0]**2 + 1))**2 / 10 + \
          (med3[3] - ((1 - (4/3) * (4/M[1])) * M[0]**2 + 1))**2 / 10 + \
          (med3[4] - ((1 - (4/3) * (5/M[1])) * M[0]**2 + 1))**2 / 10 + \
          (med3[5] - (((4/3) * (6/M[1]) - (1/3) * M[1]**2 / 36 + 2 * M[1] / 6 - 3) * M[0]**2 + 1))**2 / 10 + \
          (med3[6] - (((4/3) * (7/M[1]) - (1/3) * M[1]**2 / 49 + 2 * M[1] / 7 - 3) * M[0]**2 + 1))**2 / 10 + \
          (med3[7] - (((4/3) * (8/M[1]) - (1/3) * M[1]**2 / 64 + 2 * M[1] / 8 - 3) * M[0]**2 + 1))**2 / 10 + \
          (med3[8] - (((4/3) * (9/M[1]) - (1/3) * M[1]**2 / 81 + 2 * M[1] / 9 - 3) * M[0]**2 + 1))**2 / 10 + \
          (med3[9] - (((4/3) * (10/M[1]) - (1/3) * M[1]**2 / 100 + 2 * M[1] / 10 - 3) * M[0]**2 + 1))**2 / 10
    return y3

def function4(M):
    y4 = (med4[0] - ((1 - (4/3) * (1/M[1])) * M[0]**2 + 1))**2 / 10 + \
          (med4[1] - ((1 - (4/3) * (2/M[1])) * M[0]**2 + 1))**2 / 10 + \
          (med4[2] - ((1 - (4/3) * (3/M[1])) * M[0]**2 + 1))**2 / 10 + \
          (med4[3] - ((1 - (4/3) * (4/M[1])) * M[0]**2 + 1))**2 / 10 + \
          (med4[4] - ((1 - (4/3) * (5/M[1])) * M[0]**2 + 1))**2 / 10 + \
          (med4[5] - (((4/3) * (6/M[1]) - (1/3) * M[1]**2 / 36 + 2 * M[1] / 6 - 3) * M[0]**2 + 1))**2 / 10 + \
          (med4[6] - (((4/3) * (7/M[1]) - (1/3) * M[1]**2 / 49 + 2 * M[1] / 7 - 3) * M[0]**2 + 1))**2 / 10 + \
          (med4[7] - (((4/3) * (8/M[1]) - (1/3) * M[1]**2 / 64 + 2 * M[1] / 8 - 3) * M[0]**2 + 1))**2 / 10 + \
          (med4[8] - (((4/3) * (9/M[1]) - (1/3) * M[1]**2 / 81 + 2 * M[1] / 9 - 3) * M[0]**2 + 1))**2 / 10 + \
          (med4[9] - (((4/3) * (10/M[1]) - (1/3) * M[1]**2 / 100 + 2 * M[1] / 10 - 3) * M[0]**2 + 1))**2 / 10
    return y4

def function5(M):
    y5 = (med5[0] - ((1 - (4/3) * (1/M[1])) * M[0]**2 + 1))**2 / 10 + \
          (med5[1] - ((1 - (4/3) * (2/M[1])) * M[0]**2 + 1))**2 / 10 + \
          (med5[2] - ((1 - (4/3) * (3/M[1])) * M[0]**2 + 1))**2 / 10 + \
          (med5[3] - ((1 - (4/3) * (4/M[1])) * M[0]**2 + 1))**2 / 10 + \
          (med5[4] - ((1 - (4/3) * (5/M[1])) * M[0]**2 + 1))**2 / 10 + \
          (med5[5] - (((4/3) * (6/M[1]) - (1/3) * M[1]**2 / 36 + 2 * M[1] / 6 - 3) * M[0]**2 + 1))**2 / 10 + \
          (med5[6] - (((4/3) * (7/M[1]) - (1/3) * M[1]**2 / 49 + 2 * M[1] / 7 - 3) * M[0]**2 + 1))**2 / 10 + \
          (med5[7] - (((4/3) * (8/M[1]) - (1/3) * M[1]**2 / 64 + 2 * M[1] / 8 - 3) * M[0]**2 + 1))**2 / 10 + \
          (med5[8] - (((4/3) * (9/M[1]) - (1/3) * M[1]**2 / 81 + 2 * M[1] / 9 - 3) * M[0]**2 + 1))**2 / 10 + \
          (med5[9] - (((4/3) * (10/M[1]) - (1/3) * M[1]**2 / 100 + 2 * M[1] / 10 - 3) * M[0]**2 + 1))**2 / 10
    return y5

def function6(M):
    y6 = (med6[0] - ((1 - (4/3) * (1/M[1])) * M[0]**2 + 1))**2 / 10 + \
          (med6[1] - ((1 - (4/3) * (2/M[1])) * M[0]**2 + 1))**2 / 10 + \
          (med6[2] - ((1 - (4/3) * (3/M[1])) * M[0]**2 + 1))**2 / 10 + \
          (med6[3] - ((1 - (4/3) * (4/M[1])) * M[0]**2 + 1))**2 / 10 + \
          (med6[4] - ((1 - (4/3) * (5/M[1])) * M[0]**2 + 1))**2 / 10 + \
          (med6[5] - (((4/3) * (6/M[1]) - (1/3) * M[1]**2 / 36 + 2 * M[1] / 6 - 3) * M[0]**2 + 1))**2 / 10 + \
          (med6[6] - (((4/3) * (7/M[1]) - (1/3) * M[1]**2 / 49 + 2 * M[1] / 7 - 3) * M[0]**2 + 1))**2 / 10 + \
          (med6[7] - (((4/3) * (8/M[1]) - (1/3) * M[1]**2 / 64 + 2 * M[1] / 8 - 3) * M[0]**2 + 1))**2 / 10 + \
          (med6[8] - (((4/3) * (9/M[1]) - (1/3) * M[1]**2 / 81 + 2 * M[1] / 9 - 3) * M[0]**2 + 1))**2 / 10 + \
          (med6[9] - (((4/3) * (10/M[1]) - (1/3) * M[1]**2 / 100 + 2 * M[1] / 10 - 3) * M[0]**2 + 1))**2 / 10
    return y6

def function7(M):
    y7 = (med7[0] - ((1 - (4/3) * (1/M[1])) * M[0]**2 + 1))**2 / 10 + \
          (med7[1] - ((1 - (4/3) * (2/M[1])) * M[0]**2 + 1))**2 / 10 + \
          (med7[2] - ((1 - (4/3) * (3/M[1])) * M[0]**2 + 1))**2 / 10 + \
          (med7[3] - ((1 - (4/3) * (4/M[1])) * M[0]**2 + 1))**2 / 10 + \
          (med7[4] - ((1 - (4/3) * (5/M[1])) * M[0]**2 + 1))**2 / 10 + \
          (med7[5] - (((4/3) * (6/M[1]) - (1/3) * M[1]**2 / 36 + 2 * M[1] / 6 - 3) * M[0]**2 + 1))**2 / 10 + \
          (med7[6] - (((4/3) * (7/M[1]) - (1/3) * M[1]**2 / 49 + 2 * M[1] / 7 - 3) * M[0]**2 + 1))**2 / 10 + \
          (med7[7] - (((4/3) * (8/M[1]) - (1/3) * M[1]**2 / 64 + 2 * M[1] / 8 - 3) * M[0]**2 + 1))**2 / 10 + \
          (med7[8] - (((4/3) * (9/M[1]) - (1/3) * M[1]**2 / 81 + 2 * M[1] / 9 - 3) * M[0]**2 + 1))**2 / 10 + \
          (med7[9] - (((4/3) * (10/M[1]) - (1/3) * M[1]**2 / 100 + 2 * M[1] / 10 - 3) * M[0]**2 + 1))**2 / 10
    return y7

def function8(M):
    y8 = (med8[0] - ((1 - (4/3) * (1/M[1])) * M[0]**2 + 1))**2 / 10 + \
          (med8[1] - ((1 - (4/3) * (2/M[1])) * M[0]**2 + 1))**2 / 10 + \
          (med8[2] - ((1 - (4/3) * (3/M[1])) * M[0]**2 + 1))**2 / 10 + \
          (med8[3] - ((1 - (4/3) * (4/M[1])) * M[0]**2 + 1))**2 / 10 + \
          (med8[4] - ((1 - (4/3) * (5/M[1])) * M[0]**2 + 1))**2 / 10 + \
          (med8[5] - (((4/3) * (6/M[1]) - (1/3) * M[1]**2 / 36 + 2 * M[1] / 6 - 3) * M[0]**2 + 1))**2 / 10 + \
          (med8[6] - (((4/3) * (7/M[1]) - (1/3) * M[1]**2 / 49 + 2 * M[1] / 7 - 3) * M[0]**2 + 1))**2 / 10 + \
          (med8[7] - (((4/3) * (8/M[1]) - (1/3) * M[1]**2 / 64 + 2 * M[1] / 8 - 3) * M[0]**2 + 1))**2 / 10 + \
          (med8[8] - (((4/3) * (9/M[1]) - (1/3) * M[1]**2 / 81 + 2 * M[1] / 9 - 3) * M[0]**2 + 1))**2 / 10 + \
          (med8[9] - (((4/3) * (10/M[1]) - (1/3) * M[1]**2 / 100 + 2 * M[1] / 10 - 3) * M[0]**2 + 1))**2 / 10
    return y8

def function9(M):
    y9 = (med9[0] - ((1 - (4/3) * (1/M[1])) * M[0]**2 + 1))**2 / 10 + \
          (med9[1] - ((1 - (4/3) * (2/M[1])) * M[0]**2 + 1))**2 / 10 + \
          (med9[2] - ((1 - (4/3) * (3/M[1])) * M[0]**2 + 1))**2 / 10 + \
          (med9[3] - ((1 - (4/3) * (4/M[1])) * M[0]**2 + 1))**2 / 10 + \
          (med9[4] - ((1 - (4/3) * (5/M[1])) * M[0]**2 + 1))**2 / 10 + \
          (med9[5] - (((4/3) * (6/M[1]) - (1/3) * M[1]**2 / 36 + 2 * M[1] / 6 - 3) * M[0]**2 + 1))**2 / 10 + \
          (med9[6] - (((4/3) * (7/M[1]) - (1/3) * M[1]**2 / 49 + 2 * M[1] / 7 - 3) * M[0]**2 + 1))**2 / 10 + \
          (med9[7] - (((4/3) * (8/M[1]) - (1/3) * M[1]**2 / 64 + 2 * M[1] / 8 - 3) * M[0]**2 + 1))**2 / 10 + \
          (med9[8] - (((4/3) * (9/M[1]) - (1/3) * M[1]**2 / 81 + 2 * M[1] / 9 - 3) * M[0]**2 + 1))**2 / 10 + \
          (med9[9] - (((4/3) * (10/M[1]) - (1/3) * M[1]**2 / 100 + 2 * M[1] / 10 - 3) * M[0]**2 + 1))**2 / 10
    return y9

def function10(M):
    y10 = (med10[0] - ((1 - (4/3) * (1/M[1])) * M[0]**2 + 1))**2 / 10 + \
          (med10[1] - ((1 - (4/3) * (2/M[1])) * M[0]**2 + 1))**2 / 10 + \
          (med10[2] - ((1 - (4/3) * (3/M[1])) * M[0]**2 + 1))**2 / 10 + \
          (med10[3] - ((1 - (4/3) * (4/M[1])) * M[0]**2 + 1))**2 / 10 + \
          (med10[4] - ((1 - (4/3) * (5/M[1])) * M[0]**2 + 1))**2 / 10 + \
          (med10[5] - (((4/3) * (6/M[1]) - (1/3) * M[1]**2 / 36 + 2 * M[1] / 6 - 3) * M[0]**2 + 1))**2 / 10 + \
          (med10[6] - (((4/3) * (7/M[1]) - (1/3) * M[1]**2 / 49 + 2 * M[1] / 7 - 3) * M[0]**2 + 1))**2 / 10 + \
          (med10[7] - (((4/3) * (8/M[1]) - (1/3) * M[1]**2 / 64 + 2 * M[1] / 8 - 3) * M[0]**2 + 1))**2 / 10 + \
          (med10[8] - (((4/3) * (9/M[1]) - (1/3) * M[1]**2 / 81 + 2 * M[1] / 9 - 3) * M[0]**2 + 1))**2 / 10 + \
          (med10[9] - (((4/3) * (10/M[1]) - (1/3) * M[1]**2 / 100 + 2 * M[1] / 10 - 3) * M[0]**2 + 1))**2 / 10
    return y10

# Minimizar las funciones para cada medida
res1 = minimize(function1, x0=(1, 10), bounds=[(0.48, 0.52), (7, 13)])
res2 = minimize(function2, x0=(1, 10), bounds=[(0.48, 0.52), (7, 13)])
res3 = minimize(function3, x0=(1, 10), bounds=[(0.48, 0.52), (7, 13)])
res4 = minimize(function4, x0=(1, 10), bounds=[(0.48, 0.52), (7, 13)])
res5 = minimize(function5, x0=(1, 10), bounds=[(0.48, 0.52), (7, 13)])
res6 = minimize(function6, x0=(1, 10), bounds=[(0.48, 0.52), (7, 13)])
res7 = minimize(function7, x0=(1, 10), bounds=[(0.48, 0.52), (7, 13)])
res8 = minimize(function8, x0=(1, 10), bounds=[(0.48, 0.52), (7, 13)])
res9 = minimize(function9, x0=(1, 10), bounds=[(0.48, 0.52), (7, 13)])
res10 = minimize(function10, x0=(1, 10), bounds=[(0.48, 0.52), (7, 13)])

# Imprimir los resultados de la minimización
print("Resultados de la minimización para med1:", res1.x)
print("Resultados de la minimización para med2:", res2.x)
print("Resultados de la minimización para med3:", res3.x)
print("Resultados de la minimización para med4:", res4.x)
print("Resultados de la minimización para med5:", res5.x)
print("Resultados de la minimización para med6:", res6.x)
print("Resultados de la minimización para med7:", res7.x)
print("Resultados de la minimización para med8:", res8.x)
print("Resultados de la minimización para med9:", res9.x)
print("Resultados de la minimización para med10:", res10.x)

import numpy as np
import matplotlib.pyplot as plt

# Definir las funciones teóricas
def f11(M, P, T):
    return (1 - (4/3) * T / P) * M**2 + 1

def f21(M, P, T):
    return ((4/3) * (T / P) - (1/3) * (T / P)**(-2) + 2 * (T / P)**(-1) - 3) * M**2 + 1

results = [res1, res2, res3, res4, res5, res6, res7, res8, res9, res10]

experimental_values = [med1, med2, med3, med4, med5, med6, med7, med8, med9, med10]

# Crear las gráficas para cada medida
for i in range(10):
    P = results[i].x[1]
    M = results[i].x[0]
    
    T = np.linspace(1, 10, 10)  
    T1 = np.linspace(1, P/2, 10000)  
    T2 = np.linspace(P/2, 10, 10000)  
    
    # Graficar los valores experimentales
    plt.plot(T, experimental_values[i], 'bo', label='Experimental values')
    
    # Graficar la primera parte de la curva teórica
    plt.plot(T1, f11(M, P, T1), 'k', label='Theoretical curve')
    
    # Graficar la segunda parte de la curva teórica
    plt.plot(T2, f21(M, P, T2), 'k')
    
    plt.xlabel(r'$T$/ms')
    plt.ylabel(r'$n^{(2)}$')
    plt.title(f'Series {i+1}')
    plt.legend()
    
    plt.show()


# Calcular el promedio de M y P
M = sum(res.x[0] for res in results) / 10
P = sum(res.x[1] for res in results) / 10

print("Promedio de M:", M)
print("Promedio de P:", P)

# Calcular la desviación estándar de M y P
desviacionM = np.sqrt(sum((res.x[0] - M)**2 for res in results) / 9)
desviacionP = np.sqrt(sum((res.x[1] - P)**2 for res in results) / 9)










print("Desviación estándar de M:", desviacionM)
print("Desviación estándar de P:", desviacionP)

# Now we plot the theoretical curve vs the experimental values
# Performing two functions with M and P
def f1(M, P, T1):
    return (1 - (4/3) * T1/P) * M**2 + 1

def f2(M, P, T1):
    return ((4/3) * (T1/P) - (1/3) * (T1/P)**-2 + 2 * (T1/P)**-1 - 3) * M**2 + 1



# Plotting the average with its error vs the theoretical curve
plt.errorbar(T, media, yerr=desviacion, fmt='bo', label='Average')
T1 = np.linspace(1, P/2, 10000)
plt.plot(T1, f1(M, P, T1), 'k', label='Theoretical curve')
T2 = np.linspace(P/2, 10, 10000)
plt.plot(T2, f2(M, P, T2), 'k')
plt.xlabel(r'$T$/ms')
plt.ylabel(r'$n^{(2)}$')

# Mostrar ecuación de la recta en notación científica con errores
eq_text = (f"$M = (0,501 \\pm 0,007)$\n"
           f"$P = (9,7 \\pm 0,5)$")
plt.text(0.05, 0.15, eq_text, transform=plt.gca().transAxes, fontsize=12, 
         bbox=dict(facecolor='white', alpha=0.8, edgecolor='black'))

# Mostrar la gráfica
plt.legend()
plt.show()
