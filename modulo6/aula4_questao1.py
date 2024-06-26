# Lista com todos os números pares entre 20 e 50
pares_20_50 = [num for num in range(20, 51) if num % 2 == 0]

# Lista com os quadrados de todos os valores da lista [1,2,3,4,5,6,7,8,9]
quadrados = [num**2 for num in [1, 2, 3, 4, 5, 6, 7, 8, 9]]

# Lista com todos os números entre 1 e 100 que sejam divisíveis por 7
divisiveis_por_7 = [num for num in range(1, 101) if num % 7 == 0]

# Lista com "par" ou "impar" para todos os valores em range(0, 30, 3)
paridade = ["par" if num % 2 == 0 else "impar" for num in range(0, 30, 3)]

# Imprime as listas geradas
print("Números pares entre 20 e 50:")
print(pares_20_50)

print("\nQuadrados dos valores da lista [1,2,3,4,5,6,7,8,9]:")
print(quadrados)

print("\nNúmeros entre 1 e 100 que são divisíveis por 7:")
print(divisiveis_por_7)

print("\nParidade dos valores em range(0, 30, 3):")
print(paridade)