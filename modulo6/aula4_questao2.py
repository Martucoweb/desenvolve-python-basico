def main():
    # Solicita uma frase do usuário
    frase = input("Digite uma frase: ")

    # Definição das vogais
    vogais = "aeiouAEIOU"

    # Cria a lista de vogais usando compreensão de listas e ordena alfabeticamente
    lista_vogais = sorted([char for char in frase if char in vogais])

    # Cria a lista de consoantes usando compreensão de listas
    lista_consoantes = [char for char in frase if char.isalpha() and char not in vogais]

    # Imprime as listas geradas
    print("Vogais:", lista_vogais)
    print("Consoantes:", lista_consoantes)

if __name__ == "__main__":
    main()