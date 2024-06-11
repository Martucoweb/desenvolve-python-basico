
# Abrir o arquivo para leitura
with open("estomago.txt", "r", encoding="utf-8") as arquivo:
    linhas = arquivo.readlines()

# Imprimir as primeiras 25 linhas do texto
print("Primeiras 25 linhas do texto:")
for linha in linhas[:25]:
    print(linha.strip())

# Imprimir o número total de linhas do arquivo
numero_de_linhas = len(linhas)
print(f"\nNúmero total de linhas no arquivo: {numero_de_linhas}")

# Encontrar a linha com o maior número de caracteres
linha_mais_longa = max(linhas, key=len)
print(f"\nLinha com o maior número de caracteres:\n{linha_mais_longa.strip()}")
print(f"Número de caracteres na linha mais longa: {len(linha_mais_longa.strip())}")

# Contar o número de menções aos nomes "Nonato" e "Íria" (incluindo variações de maiúsculas e minúsculas)
nome_nonato = sum(1 for linha in linhas if "nonato" in linha.lower())
nome_iria = sum(1 for linha in linhas if "íria" in linha.lower() and not any(c.isalnum() for c in linha.lower().split("íria")[0][-1:]))

print(f"\nNúmero de menções ao personagem 'Nonato': {nome_nonato}")
print(f"Número de menções ao personagem 'Íria': {nome_iria}")