def solicitar_numeros():
    numeros = []
    print("Digite pelo menos 4 números inteiros (digite 'fim' para finalizar a entrada de dados):")
    while True:
        entrada = input()
        if entrada.lower() == 'fim':
            if len(numeros) >= 4:
                break
            else:
                print("Você precisa digitar pelo menos 4 números. Continue digitando.")
        else:
            try:
                numero = int(entrada)
                numeros.append(numero)
            except ValueError:
                print("Entrada inválida. Por favor, insira um número inteiro ou 'fim' para finalizar.")
    return numeros

def main():
    # Solicita os números ao usuário
    lista = solicitar_numeros()

    # Imprime a lista original
    print("Lista original:")
    print(lista)

    # Imprime os 3 primeiros elementos
    print("\nOs 3 primeiros elementos:")
    print(lista[:3])

    # Imprime os 2 últimos elementos
    print("\nOs 2 últimos elementos:")
    print(lista[-2:])

    # Imprime a lista invertida
    print("\nLista invertida:")
    print(lista[::-1])

    # Imprime os elementos de índice par
    print("\nElementos de índice par:")
    print(lista[::2])

    # Imprime os elementos de índice ímpar
    print("\nElementos de índice ímpar:")
    print(lista[1::2])

if __name__ == "__main__":
    main()