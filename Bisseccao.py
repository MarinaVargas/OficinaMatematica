# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 14:51:36 2023

@author: varga
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def f(x):
    return - x**2 - 2*x + 1

def bissecao(f, a, b, tol=1e-6, max_iter=1000):
    iter_count = 0
    iter_data = []

    while iter_count < max_iter:
        iter_count += 1
        x_star = (a + b) / 2

        iter_data.append({'Iteração': iter_count, 'a': a, 'b': b, 'x*': x_star, 'f(x*)': f(x_star)})

        if f(a) * f(x_star) < 0:
            b = x_star
        else:
            a = x_star

        if abs(f(x_star)) < tol:
            break

    return x_star, iter_data

a, b = -2, 2
x = np.linspace(-3, 3, 1000)

x_star, iter_data = bissecao(f, a, b, max_iter=6)

# Plotando o gráfico
plt.plot(x, f(x), label='f(x) = - x^2 - 2x + 1')
plt.axhline(y=0, color='k', linewidth=0.8)
plt.axvline(x=0, color='k', linewidth=0.8)
plt.plot(x_star, f(x_star), 'go', label=f'x* ≈ {x_star:.6f}')

for i, data in enumerate(iter_data):
    plt.plot(data['x*'], f(data['x*']), 'ro', alpha=0.3)
    plt.text(data['x*'], f(data['x*']), f"x{i+1}", fontsize=8)

# Alterando a escala do gráfico
plt.xlim(-1, 2)
plt.ylim(-9, 9)

plt.legend()
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Método da Bissecção (6 iterações)')
plt.show()

# Exibindo os resultados tabulares
df = pd.DataFrame(iter_data)
pd.set_option('display.float_format', '{:.6f}'.format)
print(df)

