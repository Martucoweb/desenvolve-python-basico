import random

# Gera aleatoriamente 20 valores inteiros entre -100 e 100 e armazena em uma lista
lista_original = [random.randint(-100, 100) for _ in range(20)]

# Cria uma cópia da lista original e ordena a cópia
lista_ordenada = sorted(lista_original)

# Encontra o índice do maior valor da lista
indice_maior = lista_original.index(max(lista_original))

# Encontra o índice do menor valor da lista
indice_menor = lista_original.index(min(lista_original))

# Imprime a lista ordenada
print("Lista ordenada (sem modificar a lista original):")
print(lista_ordenada)

# Imprime a lista original
print("\nLista original:")
print(lista_original)

# Imprime o índice do maior valor da lista
print("\nÍndice do maior valor da lista:")
print(indice_maior)

# Imprime o índice do menor valor da lista
print("\nÍndice do menor valor da lista:")
print(indice_menor)