class Movie:
    def __init__(self, name, duration, actor):
        self.name = name
        self.duration = duration
        self.actor = actor

    def __str__(self):
        return f"Filme: {self.name}"

    def technical_sheet(self):
        print(f"nome do filme: {self.name}")
        print(f'duraçao do filme: {self.duration}')
        print(f'Ator Principal \n')

moana2 = Movie('Moana2', 200, 'Personagem de desenho')

moana2.technical_sheet()
