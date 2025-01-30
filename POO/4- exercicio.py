"""
classe produto
metedo desconto

cada produto deve ter um preco e um nome
a classe com um meto contrutor e o metodo dundle str para voltar o nome do produto e nao da aquele erro
A classe deve ter um metodo para desconto. deve recer o desconto em porcentual e realciar o calculo de quando ficaria no fi.

"""

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
        
    def __str__(self):
        return f'Produto : {self.nome}'
    
    def technical_sheet(self):
        print ('\n# Informacoes do pedido')
        print(f'Produto: {self.nome}')
        print(f'Preco: {self.preco}\n')
        
    
    def desconto (self, desconto):
        valor = (self.preco/100) * desconto
        resultado = self.preco * valor
        return int(resultado)



arroz= Produto('Arroz Tio Joao', 20.50)
arroz.technical_sheet()
print(arroz.desconto(30))