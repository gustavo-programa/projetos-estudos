from pathlib import Path


root_dir = Path('dados')
file_paths = root_dir.iterdir() # saber quais arquivos possuem na pasta
#  print(list(file_paths))

for path in file_paths:
    # ira printar todos os prefixos e sufixos dos arquivos na pasta
    #print (path.stem)
    #print(path.suffix)


    # Irá acrescentar um prefixo no nome de cada arquivo
    # f é para formatar | novo é o nome que escolhi para ser o prefixo (Posso colocar qualquer nome)
    new_filename = f'novo-{path.stem} {path.suffix}'
    print(new_filename)
    
    #ira renomear o arquivo na pasta
    #whith_name é um metodo da biblioteca Path para criar um novo caminho baseado no atual | new_filename, pega o nome do prefixo criado acima | Renomeia o arquivo
    new_filepath = path.with_name(new_filename)
    path.rename(new_filepath)
