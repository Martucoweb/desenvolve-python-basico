# Lista dos meses do ano
meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", 
         "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

# Solicita ao usuário que digite a data de nascimento
data_nascimento = input("Digite uma data de nascimento (dd/mm/aaaa): ")

# Divide a data de nascimento em dia, mês e ano
dia, mes, ano = data_nascimento.split('/')

# Converte o mês para um índice (inteiro)
mes = int(mes)

# Obtém o nome do mês por extenso
mes_extenso = meses[mes - 1]