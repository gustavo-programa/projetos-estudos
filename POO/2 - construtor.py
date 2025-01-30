class Movie:
    def __init__(self, nome, duracao, ator):
        self.nome = nome
        self.duracao = duracao
        self.ator = ator
    
    def __str__(self):
        return f"Filme : {self.nome}"

movie1 = Movie('teste', 0, 'teste')

print(movie1.nome)
print(movie1)