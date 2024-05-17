#entrada de dados
# genero, idade e tempo de serviço

genero = input()
idade= int (input())
tempo=int(input())

#processamento
# A:para mulheres ter mais de 60 anos.Para homens mais de 65
# B: ou ter trabalhado mais de 30 anos
# C:ou ter 60 anos e trabalho pelo menos 25 anos.

a = (genero =='f' and idade >= 60)or  ( genero == 'm' and idade>= 65 )
b = tempo >30
c = idade >= 60 and tempo >= 25

pode_aposentar = a or b or c

# saida
print(pode_aposentar)