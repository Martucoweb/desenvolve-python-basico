import random

def embaralhar_palavras(frase):
    # Divide a frase em palavras
    palavras = frase.split()
    
    # Embaralha as letras internas de cada palavra
    frase_embaralhada = []
    for palavra in palavras:
        if len(palavra) > 2:  # Verifica se a palavra tem mais de duas letras
            letras = list(palavra[1:-1])  # Obtém as letras internas da palavra
            random.shuffle(letras)  # Embaralha as letras internas
            palavra_embaralhada = palavra[0] + ''.join(letras) + palavra[-1]  # Reconstrói a palavra embaralhada
        else:
            palavra_embaralhada = palavra  # Se a palavra tem 2 ou menos letras, não é embaralhada
        frase_embaralhada.append(palavra_embaralhada)
    
    # Junta as palavras embaralhadas em uma única string
    return ' '.join(frase_embaralhada)

# Exemplo de uso:
frase = "Python é uma linguagem de programação"
resultado = embaralhar_palavras(frase)
print(resultado)
# Possível saída: "Ptohyn é uma lignuagem de prrgaomaação"