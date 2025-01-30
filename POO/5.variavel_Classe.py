class Movie :
    plataforma = 'OrbiWeb' #Variavel de Classe
    def __init__(self,name,duration,data ):
        self.name = name
        self.duration= duration
        self.data = data

    
    def __str__(self):
        return f'Nome do Filme: {self.name}'
    
    def ficha (self):
        print (f'#Dados do Filme')
        print(f'Nome do Filme: {self.name}')
        print(f'Tempo de Duracao: {self.duration}')
        print (f'Ano de Lancamento: {self.data}')
        print(f'Plataforma: {Movie.plataforma}')

moana = Movie('Moana2', 200, '21-02-2023')

moana.ficha()