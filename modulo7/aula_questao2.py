import os

# Solicitar uma frase do usuário
frase = input("Digite uma frase: ")

# Definir o caminho completo para o arquivo "frase.txt"
caminho_arquivo = os.path.join(os.path.dirname(os.path.abspath(__file__)), "frase.txt")

# Salvar a frase no arquivo "frase.txt"
with open(caminho_arquivo, "w") as arquivo:
    arquivo.write(frase)

# Imprimir o caminho completo do arquivo salvo
    import os
import re

# Definir o caminho completo para o arquivo "frase.txt"
caminho_arquivo_frase = os.path.join(os.path.dirname(os.path.abspath(__file__)), "frase.txt")

# Ler o conteúdo do arquivo "frase.txt"
with open(caminho_arquivo_frase, "r") as arquivo:
    conteudo = arquivo.read()

# Remover espaços em branco e caracteres não alfabéticos, e separar cada palavra em uma linha
palavras = re.findall(r'\b[A-Za-zÀ-ÿ]+\b', conteudo)

# Definir o caminho completo para o arquivo "palavras.txt"
caminho_arquivo_palavras = os.path.join(os.path.dirname(os.path.abspath(__file__)), "palavras.txt")

# Salvar cada palavra em uma linha no arquivo "palavras.txt"
with open(caminho_arquivo_palavras, "w") as arquivo:
    for palavra in palavras:
        arquivo.write(palavra + '\n')

# Imprimir o conteúdo do arquivo "palavras.txt"
with open(caminho_arquivo_palavras, "r") as arquivo:
    conteudo_palavras = arquivo.read()

print("Conteúdo do arquivo 'palavras.txt':")
print(conteudo_palavras)