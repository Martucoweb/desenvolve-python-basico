import random

def carregar_palavras():
    with open("gabarito_forca.txt", "r", encoding="utf-8") as arquivo:
        palavras = arquivo.read().splitlines()
    return palavras

def carregar_enforcado():
    with open("gabarito_enforcado.txt", "r", encoding="utf-8") as arquivo:
        estagios = arquivo.read().split("----------\n")
    return estagios

def escolher_palavra(palavras):
    return random.choice(palavras)

def imprime_enforcado(estagios, erros):
    print(estagios[erros])

def jogo_forca():
    palavras = carregar_palavras()
    estagios = carregar_enforcado()
    palavra = escolher_palavra(palavras)
    palavra_oculta = ["_"] * len(palavra)
    tentativas = set()
    erros = 0

    print("Bem-vindo ao jogo da forca!")
    print("A palavra tem", len(palavra), "letras.")
    print(" ".join(palavra_oculta))

    while erros < 6 and "_" in palavra_oculta:
        letra = input("Digite uma letra: ").lower()

        if letra in tentativas:
            print("Você já tentou essa letra. Tente outra.")
            continue

        tentativas.add(letra)

        if letra in palavra:
            for indice, caractere in enumerate(palavra):
                if caractere == letra:
                    palavra_oculta[indice] = letra
            print("Acertou!")
        else:
            erros += 1
            print("Errou!")
            imprime_enforcado(estagios, erros)

        print(" ".join(palavra_oculta))
        print("Tentativas: ", " ".join(sorted(tentativas)))

    if "_" not in palavra_oculta:
        print("Parabéns! Você adivinhou a palavra:", palavra)
    else:
        print("Você perdeu! A palavra era:", palavra)

if __name__ == "__main__":
    jogo_forca()