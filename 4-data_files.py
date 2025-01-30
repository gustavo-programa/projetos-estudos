from pathlib import Path
from datetime import datetime

path = Path('files', 'dados', 'a.txt') 

#Obtem as informacoes do arquivo, no caso a gente ira precisar do st_atime que e o tempo de criacao ou ultima alteracao do arquivo
stats = path.stat()
#armazena o st_atime do path.stat, que é o segundos da criacao do arquivo
second_created = stats.st_atime

#aqui utila o datetime para converter a informacao obtida do st_atime que armazenamos na variavel second_created para data e hora legivel
date_created = datetime.fromtimestamp(second_created)

#print(date_created)

#aqui utila o str.ftime para formatar/decodificar a informacao obtida do st_atime que armazenamos na variavel date_created para uma string no formato 'ano-mês-dia_hora_minuto_segundo'
date_created_str = date_created.strftime('%Y-%m-%d_%H_%M_%S')
print(date_created_str)