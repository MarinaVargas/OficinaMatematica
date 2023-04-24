# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 16:26:13 2023

@author: varga
"""

import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**2 + x - 4

def g(x):
    return np.sqrt(4 - x)

x_0 = 1
iterations = 7

x = np.linspace(-2, 3, 1000)
y = np.linspace(-2, 3, 1000)

plt.plot(x, g(x), label='g(x) = sqrt(4 - x)')
plt.plot(x, x, label='y = x')

for i in range(iterations):
    x_1 = g(x_0)
    plt.plot([x_0, x_0], [x_0, x_1], 'k--')
    plt.plot([x_0, x_1], [x_1, x_1], 'k--')
    x_0 = x_1

plt.axhline(y=0, color='k', linewidth=0.8)
plt.axvline(x=0, color='k', linewidth=0.8)

plt.legend()
plt.xlabel('x')
plt.ylabel('g(x)')
plt.title('Método do Ponto Fixo: Iterações')
plt.grid(True)
plt.show()
