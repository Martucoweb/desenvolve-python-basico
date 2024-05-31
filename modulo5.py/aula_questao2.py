import random
import math

# Solicita ao usuário o valor de n
try:
    n = int(input("Digite a quantidade de valores inteiros aleatórios a serem gerados: "))
    if n <= 0:
        raise ValueError("O valor de n deve ser um inteiro positivo.")

    # Gera n valores inteiros aleatórios entre 0 e 100
    valores = [random.randint(0, 100) for _ in range(n)]

    # Calcula a soma dos valores
    soma_valores = sum(valores)

    # Calcula a raiz quadrada da soma dos valores
    raiz_quadrada = math.sqrt(soma_valores)

    # Exibe os valores gerados, a soma e a raiz quadrada da soma
    print(f"Valores gerados: {valores}")
    print(f"Soma dos valores: {soma_valores}")
    print(f"Raiz quadrada da soma: {raiz_quadrada:.2f}")

except ValueError as e:
    print(f"Entrada inválida: {e}")