import string

def limpar_frase(frase):
    # Remove espaços em branco e sinais de pontuação, e converte para minúsculas
    frase_limpa = ''.join(char.lower() for char in frase if char.isalnum())
    return frase_limpa

def eh_palindromo(frase):
    # Limpa a frase para verificar se é um palíndromo
    frase_limpa = limpar_frase(frase)
    # Verifica se a frase limpa é igual à sua inversa
    return frase_limpa == frase_limpa[::-1]

while True:
    # Solicita ao usuário que digite uma frase
    frase = input('Digite uma frase (digite "fim" para encerrar): ')
    
    # Verifica se o usuário digitou "fim" para encerrar o programa
    if frase.lower() == 'fim':
        break
    
    # Verifica se a frase é um palíndromo
    if eh_palindromo(frase):
        print(f'"{frase}" é palíndromo')
    else:
        print(f'"{frase}" não é palíndromo')