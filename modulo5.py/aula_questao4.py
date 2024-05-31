import datetime

# Obtém a data e hora atuais
data_hora_atual = datetime.datetime.now()

# Formata a data e a hora usando f-strings
data_formatada = f"{data_hora_atual.day:02d}/{data_hora_atual.month:02d}/{data_hora_atual.year}"
hora_formatada = f"{data_hora_atual.hour:02d}:{data_hora_atual.minute:02d}"

# Exibe a data e a hora formatadas
print(f"data:{data_formatada}")
print(f"hora:{hora_formatada}")