class Movie:
    def __init__(self,name,duration):
        self.name = name
        self.duration = duration
    
    def __str__(self):
        return f'Nome do filme : {self.name}'
    
    def ficha (self):
        print (f'Nome: {self.name}')
        print (f'duration: {self.duration} ')

moana = Movie('Moana', 200)

moana.ficha()