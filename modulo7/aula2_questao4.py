import re

def validador_senha(senha):
    # Verifica o comprimento da senha
    if len(senha) < 8:
        return False
    
    # Verifica a presença de pelo menos uma letra maiúscula
    if not re.search(r'[A-Z]', senha):
        return False
    
    # Verifica a presença de pelo menos uma letra minúscula
    if not re.search(r'[a-z]', senha):
        return False
    
    # Verifica a presença de pelo menos um número
    if not re.search(r'[0-9]', senha):
        return False
    
    # Verifica a presença de pelo menos um caractere especial
    if not re.search(r'[@#$]', senha):
        return False
    
    # Se todos os critérios forem atendidos, retorna True
    return True

# Exemplo de uso:
senha1 = "Senha123@"
senha2 = "senhafraca"
senha3 = "Senha_fraca"

print(validador_senha(senha1))  # Saída esperada: True
print(validador_senha(senha2))  # Saída esperada: False
print(validador_senha(senha3))  # Saída esperada: False