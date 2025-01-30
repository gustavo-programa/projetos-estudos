import os
from pathlib import Path
from datetime import datetime

#Programa que organiza arquivos com esses tipos de arq. exe, html, jpg, pdf, zip
root_dir = Path('C:\\Users\\gusta\\Downloads')

for path in root_dir.glob('**/*'):
    if path.is_file():
        #print (path.suffix
        file_exe = '.exe'
        #if path.suffix == file_exe:
            #pasta_destino = Path(root_dir, 'exe')
            #novo_caminho = pasta_destino / path.name  
            #path.rename(novo_caminho)
        if path.suffix == '.zip':
            #Armazena o caminho da pasta zip
            pasta_zip= Path(root_dir, 'zip')
            # Representa a pasta onde sera movida, preservando o nome original do arquivo
            novo_caminho = pasta_zip / path.name
            #move para a pasta
            path.rename(novo_caminho)
        elif path.suffix == '.pdf':
            #amazena o caminho pdf
            pasta_pdf = Path(root_dir, 'pdf')
            # Representa a pasta onde sera movida, preservando o nome original do arquivo
            novo_caminho = pasta_pdf / path.name
            path.rename (novo_caminho)

        elif path.suffix == '.html':
            pasta_html = Path(root_dir, 'html')
            novo_caminho = pasta_html / path.name
            #Usei o replace para sobescrever nomes se tiver arquivos com nomes iguais
            path.replace(novo_caminho)

        
        #Apartir daqui acrescentei o mkdir para criar pastas com os nomes de extensoes se nao houver
        elif path.suffix == '.rar':
            #amazena o caminho rar
            pasta_rar = Path(root_dir, 'rar')
            #se a pasta rar nao existir, cria a pasta com esse nome
            pasta_rar.mkdir(exist_ok=True)
            # Representa a pasta onde sera movida, preservando o nome original do arquivo
            novo_caminho = pasta_rar / path.name
            path.rename (novo_caminho)
        
        elif path.suffix == '.png':
            #amazena o caminho rar
            pasta_png = Path(root_dir, 'png')
            #se a pasta rar nao existir, cria a pasta com esse nome
            pasta_png.mkdir(exist_ok=True)
            # Representa a pasta onde sera movida, preservando o nome original do arquivo
            novo_caminho = pasta_png / path.name
            path.rename (novo_caminho)
        
        elif path.suffix == '.jpeg':
            #amazena o caminho rar
            pasta_jpeg = Path(root_dir, 'jpeg')
            #se a pasta rar nao existir, cria a pasta com esse nome
            pasta_jpeg.mkdir(exist_ok=True)
            # Representa a pasta onde sera movida, preservando o nome original do arquivo
            novo_caminho = pasta_jpeg / path.name
            path.rename (novo_caminho)
        
        elif path.suffix == '.svg':
            #amazena o caminho rar
            pasta_svg = Path(root_dir, 'svg')
            #se a pasta rar nao existir, cria a pasta com esse nome
            pasta_svg.mkdir(exist_ok=True)
            # Representa a pasta onde sera movida, preservando o nome original do arquivo
            novo_caminho = pasta_svg / path.name
            path.rename (novo_caminho)
        
        elif path.suffix == '.jpg':
            #amazena o caminho rar
            pasta_jpg = Path(root_dir, 'jpg')
            #se a pasta rar nao existir, cria a pasta com esse nome
            pasta_jpg.mkdir(exist_ok=True)
            # Representa a pasta onde sera movida, preservando o nome original do arquivo
            novo_caminho = pasta_jpg / path.name
            path.rename (novo_caminho)
        
        elif path.suffix == '.mp4':
            #amazena o caminho rar
            pasta_mp4 = Path(root_dir, 'mp4')
            #se a pasta rar nao existir, cria a pasta com esse nome
            pasta_mp4.mkdir(exist_ok=True)
            # Representa a pasta onde sera movida, preservando o nome original do arquivo
            novo_caminho = pasta_mp4 / path.name
            path.rename (novo_caminho)
        
        elif path.suffix == '.docx':
            #amazena o caminho rar
            pasta_docx = Path(root_dir, 'docx')
            #se a pasta rar nao existir, cria a pasta com esse nome
            pasta_docx.mkdir(exist_ok=True)
            # Representa a pasta onde sera movida, preservando o nome original do arquivo
            novo_caminho = pasta_docx / path.name
            path.rename (novo_caminho)
        