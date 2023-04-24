# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 16:02:59 2023

@author: varga
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def f(x):
    return x**2 - x - 1

def A(x):
    return 1/4

def g(x):
    return x + A(x) * f(x)

x = np.linspace(-2, 3, 1000)

# Gráfico da função g(x) e da reta y=x
plt.plot(x, g(x), label='g(x) = x + 1/4*(x^2 - x - 1)')
plt.plot(x, x, label='y=x')

# Ponto fixo modificado com 4 iterações
x_0 = 1.5
for i in range(5):
    x_1 = g(x_0)
    plt.plot([x_0, x_0], [x_0, x_1], 'r--', linewidth=0.8)
    plt.plot([x_0, x_1], [x_1, x_1], 'r--', linewidth=0.8)
    x_0 = x_1

# Destacando os eixos x e y
plt.axhline(y=0, color='k', linewidth=1.2)
plt.axvline(x=0, color='k', linewidth=1.2)

# Alterando a escala do gráfico
plt.xlim(-1, 2)
plt.ylim(-1, 2)

plt.legend()
plt.xlabel('x')
plt.ylabel('g(x) / y')
plt.title('Método do Ponto Fixo - 4 iterações')
plt.show()

df = pd.DataFrame(iter_data, columns=['x_k', 'g(x_k)', 'x_(k+1)'])
print(df)
