import emoji

# Lista de emojis disponíveis para uso
emojis_disponiveis = {
    ":sorriso:": emoji.emojize(":smile:", use_aliases=True),
    ":coração:": emoji.emojize(":heart:", use_aliases=True),
    ":dedão_para_cima:": emoji.emojize(":thumbs_up:", use_aliases=True),
    ":fogo:": emoji.emojize(":fire:", use_aliases=True),
    ":carinha_chorando:": emoji.emojize(":cry:", use_aliases=True),
    ":carinha_de_olhos_coracao:": emoji.emojize(":heart_eyes:", use_aliases=True)
}

# Apresenta a lista de emojis disponíveis
print("Emojis disponíveis:")
for texto, emojizado in emojis_disponiveis.items():
    print(f"{texto} -> {emojizado}")

# Solicita uma frase codificada ao usuário
frase_codificada = input("\nDigite uma frase codificada com emojis: ")

# Decodifica a frase com emojis
frase_decodificada = emoji.emojize(frase_codificada, use_aliases=True)

# Apresenta a frase decodificada
print("\nFrase decodificada:")
print(frase_decodificada)