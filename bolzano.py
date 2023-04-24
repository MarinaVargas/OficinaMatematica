# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 14:36:11 2023

@author: varga
"""

import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return - x**2 - 2*x + 1

def bissecao(f, a, b, tol=1e-6, max_iter=1000):
    iter_count = 0
    while iter_count < max_iter:
        iter_count += 1
        x_star = (a + b) / 2

        if f(a) * f(x_star) < 0:
            b = x_star
        else:
            a = x_star

        if abs(f(x_star)) < tol:
            break

    return x_star

a, b = -2, 2
x = np.linspace(-3, 3, 1000)

x_star = bissecao(f, a, b)

plt.plot(x, f(x), label='f(x) = - x^2 - 2x + 1')
plt.axhline(y=0, color='k', linewidth=0.8)
plt.axvline(x=0, color='k', linewidth=0.8)

if f(a) * f(b) < 0:
    plt.axvline(x=a, color='r', linestyle='--', label=f'a = {a}')
    plt.axvline(x=b, color='b', linestyle='--', label=f'b = {b}')
    plt.fill_between(x, f(x), where=(x >= a) & (x <= b), color='gray', alpha=0.3)
    plt.plot(x_star, f(x_star), 'go', label=f'x* ≈ {x_star:.6f}')

plt.legend()
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Teorema de Bolzano (Teorema do Valor Intermediário)')
plt.show()

