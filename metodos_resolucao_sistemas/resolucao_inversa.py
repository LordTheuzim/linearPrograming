"""Codigo para resolucao de problemas de algebra linear. Entra o valor da dimensao
    'n' da matriz. Apos isso as n^2 entradas dos elementos. Apos isso as b entradas.
    O programa ira retornar o valor das incognitas"""
import numpy as np
#imput
matriz_A = []
vetor_b = []

print("Digite a dimensao n da matriz")
#dimensao matriz
dim_n = int(input())

print("Matriz A")
for x in range(dim_n**2):
    print("Digite o elemento: ", x)
    matriz_A.append(float(input()))

print("Vetor b")
for x in range(dim_n):
    print("Digite o elemento: ", x)
    vetor_b.append(float(input()))

vetor_bout = np.transpose(np.array(vetor_b))
matriz_Aout = np.reshape(np.array(matriz_A), (dim_n,dim_n))

# x = A^-1 * b
x = np.dot(np.linalg.inv(matriz_Aout), vetor_bout)

print(x)
