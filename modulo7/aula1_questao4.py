def formatar_numero(numero):
    # Verifica se o número tem 8 dígitos
    if len(numero) == 8:
        numero = '9' + numero
    
    # Verifica se o número tem 9 dígitos e começa com 9
    elif len(numero) == 9 and numero[0] != '9':
        print("Número inválido. Deve começar com 9.")
        return
    
    # Adiciona o separador "-"
    numero_formatado = numero[:5] + '-' + numero[5:]
    return numero_formatado

# Solicita ao usuário que digite um número de celular
numero = input("Digite o número: ")

# Formata o número de celular
numero_completo = formatar_numero(numero)

# Exibe o número completo formatado, se for válido
if numero_completo:
    print(f"Número completo: {numero_completo}")