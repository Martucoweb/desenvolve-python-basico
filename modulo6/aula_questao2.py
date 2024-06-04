import random

# Gera aleatoriamente um valor entre 5 e 20 e armazena em num_elementos
num_elementos = random.randint(5, 20)

# Gera aleatoriamente valores entre 1 e 10 em quantidade correspondente a num_elementos
elementos = [random.randint(1, 10) for _ in range(num_elementos)]

# Calcula a soma dos valores da lista
soma_valores = sum(elementos)

# Calcula a média dos valores da lista
media_valores = soma_valores / num_elementos

# Imprime a lista elementos
print("Lista de elementos:")
print(elementos)

# Imprime a soma dos valores da lista
print("\nSoma dos valores da lista:")
print(soma_valores)

# Imprime a média dos valores da lista
print("\nMédia dos valores da lista:")
print(f"{media_valores:.2f}")