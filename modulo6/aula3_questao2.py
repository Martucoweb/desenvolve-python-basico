# Lista de URLs
urls = ["www.google.com", "www.gmail.com", "www.github.com", "www.reddit.com", "www.yahoo.com"]

# Cria uma lista de domínios usando fatiamento
dominios = [url[4:-4] for url in urls]

# Imprime a lista de domínios
print("dominios:", dominios)