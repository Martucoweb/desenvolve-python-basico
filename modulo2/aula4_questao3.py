#Leitura de dados (entrada)
valor=int(input("digite o valor: "))
#576

#Processamento
#####começar da maior nota{quantas nota}
notas_100 = valor// 100 #576 // 100 = 5
####atualizar quantas faltam depois da maior nota 
valor = valor % 100 #576 - 5*100 = 76

notas_50 = valor// 50 #76 // 50 = 1
valor= valor % 50 # valor - 50+notas 50 #26

notas_20 = valor// 20 #26 // 20 = 1
valor= valor % 20 #6

notas_10 = valor// 10 #6 // 10 = 0
valor= valor % 10 #6

notas_5 = valor// 5 #6 // 5= 1
valor= valor % 5 #1

notas_2 = valor// 2 #1 // 2 = 0
valor= valor % 2 #1

notas_1 = valor

#impressâo de dados
print(f"{notas_100} nota(s de 100)")
print(f"{notas_50} nota(s de 50)")
print(f"{notas_20} nota(s de 20)")
print(f"{notas_10} nota(s de 10)")
print(f"{notas_5} nota(s de 5)")
print(f"{notas_2} nota(s de 2)")
print(f"{notas_1} nota(s de 1)")

