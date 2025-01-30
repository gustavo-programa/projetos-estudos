from pathlib import Path

p1 = Path('dados', 'teste.txt')
print (p1)
print(p1.name) #printar nome do arquivo
print(p1.stem) #printar nome antes da extensao
print(p1.suffix) #printar nome depois da extensao
print(p1.exists()) #printar se existe o arquivo

if p1.exists():
    #With Ele é usado para abrir um recurso, como um arquivo, e garante que esse recurso seja fechado corretamente, mesmo que ocorram erros durante o uso.
    # 'r' abrir em modo leitura | encoding se tiver cacter especial(acentuacao) | as file (pode colocar outro nome ao inves de file) file é a variavel onde vai armazenar o objeto retoernado por essa funcao

    with open(p1, 'r', encoding='utf-8') as file:
        print(file.read())