def substituir_vogais(frase):
    # Definir uma string com todas as vogais (maiúsculas e minúsculas)
    vogais = "aeiouAEIOU"
    # Inicializar uma string vazia para construir a frase modificada
    frase_modificada = ""
    
    # Iterar sobre cada caractere na frase
    for char in frase:
        # Se o caractere for uma vogal, adicionar '*' à frase modificada
        if char in vogais:
            frase_modificada += "*"
        # Caso contrário, adicionar o próprio caractere à frase modificada
        else:
            frase_modificada += char
    
    # Retornar a frase modificada
    return frase_modificada

# Solicitar ao usuário que digite uma frase
frase = input("Digite uma frase: ")

# Substituir as vogais por "*" na frase fornecida
frase_modificada = substituir_vogais(frase)

# Imprimir a frase modificada
print("Frase modificada:", frase_modificada)