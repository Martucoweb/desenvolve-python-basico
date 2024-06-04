def obter_lista(nome_lista, quantidade):
    lista = []
    print(f"Digite os {quantidade} elementos da {nome_lista}:")
    for _ in range(quantidade):
        elemento = int(input())
        lista.append(elemento)
    return lista

def combinar_listas(lista1, lista2):
    lista_intercalada = []
    len1, len2 = len(lista1), len(lista2)
    min_len = min(len1, len2)
    
    # Intercala os elementos das duas listas
    for i in range(min_len):
        lista_intercalada.append(lista1[i])
        lista_intercalada.append(lista2[i])
    
    # Adiciona os elementos restantes da lista maior
    if len1 > len2:
        lista_intercalada.extend(lista1[min_len:])
    else:
        lista_intercalada.extend(lista2[min_len:])
    
    return lista_intercalada

# Solicita a quantidade de elementos de cada lista
quantidade1 = int(input("Digite a quantidade de elementos da lista 1: "))
lista1 = obter_lista("lista 1", quantidade1)

quantidade2 = int(input("Digite a quantidade de elementos da lista 2: "))
lista2 = obter_lista("lista 2", quantidade2)

# Combina as listas de forma alternada
lista_intercalada = combinar_listas(lista1, lista2)

# Imprime a lista intercalada
print("Lista intercalada:", ' '.join(map(str, lista_intercalada)))