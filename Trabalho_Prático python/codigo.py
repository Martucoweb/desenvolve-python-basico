import csv
import os

# Estruturas de Dados
usuarios = {}
produtos = []

# Carregar Usuários
def carregar_usuarios():
    if os.path.exists('usuarios.csv'):
        with open('usuarios.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row and row[0] != 'username':  # Ignora o cabeçalho
                    username, password, role = row
                    usuarios[username] = (password, role)

# Carregar Produtos
def carregar_produtos():
    if os.path.exists('produtos.csv'):
        with open('produtos.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                produtos.append(row)

# Salvar Usuários
def salvar_usuarios():
    with open('usuarios.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['username', 'password', 'role'])
        for username, (password, role) in usuarios.items():
            writer.writerow([username, password, role])

# Salvar Produtos
def salvar_produtos():
    with open('produtos.csv', 'w', newline='') as file:
        fieldnames = ['product_id', 'name', 'price', 'quantity']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for produto in produtos:
            writer.writerow(produto)

# Funções de Usuários
def criar_usuario(username, password, role):
    usuarios[username] = (password, role)
    salvar_usuarios()

def ler_usuario(username):
    return usuarios.get(username)

def atualizar_usuario(username, password=None, role=None):
    if username in usuarios:
        current_password, current_role = usuarios[username]
        usuarios[username] = (password or current_password, role or current_role)
        salvar_usuarios()

def deletar_usuario(username):
    if username in usuarios:
        del usuarios[username]
        salvar_usuarios()

# Funções de Produtos
def criar_produto(product_id, name, price, quantity):
    produtos.append({'product_id': product_id, 'name': name, 'price': price, 'quantity': quantity})
    salvar_produtos()

def ler_produto(product_id):
    for produto in produtos:
        if produto['product_id'] == product_id:
            return produto

def atualizar_produto(product_id, name=None, price=None, quantity=None):
    for produto in produtos:
        if produto['product_id'] == product_id:
            if name:
                produto['name'] = name
            if price:
                produto['price'] = price
            if quantity:
                produto['quantity'] = quantity
            salvar_produtos()
            break

def deletar_produto(product_id):
    global produtos
    produtos = [produto for produto in produtos if produto['product_id'] != product_id]
    salvar_produtos()

def buscar_produto(nome):
    return [produto for produto in produtos if nome.lower() in produto['name'].lower()]

def imprimir_produtos_ordenados_por_nome():
    for produto in sorted(produtos, key=lambda x: x['name']):
        print(produto)

def imprimir_produtos_ordenados_por_preco():
    for produto in sorted(produtos, key=lambda x: float(x['price'])):
        print(produto)

# Controle de Acesso
def login(username, password):
    if username in usuarios and usuarios[username][0] == password:
        return usuarios[username][1]
    else:
        return None

# Função de Cadastro de Usuário
def cadastrar_usuario():
    username = input("Digite o nome do usuário: ")
    if username in usuarios:
        print("Usuário já existe!")
        return
    password = input("Digite a senha: ")
    role = input("Digite o papel do usuário: ")
    criar_usuario(username, password, role)
    print(f"Usuário {username} cadastrado com sucesso!")

# Função Principal
def main():
    carregar_usuarios()
    carregar_produtos()

    # Exemplo de Uso
    while True:
        print("Bem-vindo à Loja de Calçados!")
        username = input("Usuário: ")
        password = input("Senha: ")

        role = login(username, password)
        if role:
            print(f"Bem-vindo, {username}. Seu papel é {role}.")
            if role == 'gerente':
                while True:
                    print("\nMenu Gerente:")
                    print("1. Criar Usuário")
                    print("2. Atualizar Usuário")
                    print("3. Deletar Usuário")
                    print("4. Listar Usuários")
                    print("5. Criar Produto")
                    print("6. Atualizar Produto")
                    print("7. Deletar Produto")
                    print("8. Listar Produtos")
                    print("9. Buscar Produto")
                    print("10. Produtos Ordenados por Nome")
                    print("11. Produtos Ordenados por Preço")
                    print("12. Cadastrar Novo Usuário")
                    print("0. Sair")

                    opcao = input("Escolha uma opção: ")

                    if opcao == '1':
                        u = input("Usuário: ")
                        p = input("Senha: ")
                        r = input("Papel: ")
                        criar_usuario(u, p, r)
                    elif opcao == '2':
                        u = input("Usuário: ")
                        p = input("Nova Senha (deixe em branco para manter a atual): ")
                        r = input("Novo Papel (deixe em branco para manter o atual): ")
                        atualizar_usuario(u, p or None, r or None)
                    elif opcao == '3':
                        u = input("Usuário: ")
                        deletar_usuario(u)
                    elif opcao == '4':
                        print(usuarios)
                    elif opcao == '5':
                        pid = input("ID do Produto: ")
                        n = input("Nome: ")
                        pr = input("Preço: ")
                        q = input("Quantidade: ")
                        criar_produto(pid, n


