import random

# Gera um número aleatório entre 1 e 10
numero_aleatorio = random.randint(1, 10)

print("Tente adivinhar o número aleatório entre 1 e 10.")

while True:
    try:
        palpite = int(input("Digite seu palpite: "))

        if palpite < 1 or palpite > 10:
            print("Por favor, insira um número entre 1 e 10.")
            continue
        
        if palpite < numero_aleatorio:
            print("Seu palpite é muito baixo. Tente novamente.")
        elif palpite > numero_aleatorio:
            print("Seu palpite é muito alto. Tente novamente.")
        else:
            print("Parabéns! Você acertou o número.")
            break
    except ValueError:
        print("Entrada inválida. Por favor, insira um número inteiro.")