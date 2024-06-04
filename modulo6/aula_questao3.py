import random
from collections import Counter

# Gera duas listas com 20 valores inteiros aleatórios entre 0 e 50
lista1 = [random.randint(0, 50) for _ in range(20)]
lista2 = [random.randint(0, 50) for _ in range(20)]

# Cria a lista interseccao contendo apenas os valores que se repetem nas duas listas
interseccao = list(set(lista1) & set(lista2))

# Ordena a lista interseccao
interseccao.sort()

# Conta a quantidade de vezes que cada elemento aparece em cada lista
contagem_lista1 = Counter(lista1)
contagem_lista2 = Counter(lista2)

# Imprime ambas as listas
print("Lista 1:")
print(lista1)

print("\nLista 2:")
print(lista2)

# Imprime a lista interseccao ordenada
print("\nLista Interseccao ordenada:")
print(interseccao)

# Imprime a quantidade de vezes que cada elemento da interseccao aparece em cada lista
print("\nQuantidade de vezes que cada elemento aparece em cada lista:")
for elemento in interseccao:
    print(f"Elemento {elemento}: aparece {contagem_lista1[elemento]} vez(es) em lista1 e {contagem_lista2[elemento]} vez(es) em lista2")