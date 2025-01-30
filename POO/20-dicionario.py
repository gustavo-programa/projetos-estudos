'''
DICIONARIO

Estrutura de dados que armazena chaves-valor. É como se fosse uma lista com rotulo
'''

emails_empresa = {
    'Gustavo' : 'email1@gmail.com'
    #Chaves(Rotulo)     (Valor)
}

#Para acessar os dados do dicionario

email = emails_empresa['Gustavo']
print(email)

#Para adicionar dados no dicionario

emails_empresa['teste'] = 'teste@gmail.com'
print(emails_empresa)

#Para pegar todas as chaves (Rotulo)

for variavel in emails_empresa:
    print(variavel)

#Para pegar todas os valores
for variavel in emails_empresa:
    emails = emails_empresa[variavel] 
    print (emails)

#Retirar um email = Tem de se usar o metodo pop
emails_empresa.pop('teste') #retirar na posicao teste
print(emails_empresa)
