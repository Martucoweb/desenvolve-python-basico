import random

# Gera uma lista de 20 elementos entre -10 e 10
lista = [random.randint(-10, 10) for _ in range(20)]

# Função para encontrar o intervalo com a maior quantidade de números negativos
def encontrar_intervalo_negativos(lista):
    max_negativos = 0
    intervalo_inicio = 0
    intervalo_fim = 0
    
    for i in range(len(lista)):
        for j in range(i, len(lista)):
            sublista = lista[i:j+1]
            negativos = len([num for num in sublista if num < 0])
            if negativos > max_negativos:
                max_negativos = negativos
                intervalo_inicio = i
                intervalo_fim = j
    
    return intervalo_inicio, intervalo_fim

# Encontra o intervalo com a maior quantidade de números negativos
inicio, fim = encontrar_intervalo_negativos(lista)

# Imprime a lista original
print("Original:", lista)

# Deleta o intervalo encontrado da lista
del lista[inicio:fim+1]

# Imprime a lista editada
print("Editada:", lista)