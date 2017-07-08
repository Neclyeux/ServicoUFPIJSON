import os

#executando o primeiro script que busca o link das noticias
os.chdir('/home/neclyeux/Documentos/UFPINews')
os.system('scrapy crawl crawlerufpi -o output.json')

#excutando o segundo script que gera o json com o conteudo de cada noticia
os.chdir('/home/neclyeux/Documentos/UFPINews2')
os.system('scrapy crawl crawlernews -o output.json')

#executando o script que formara os acentos no JSON
os.chdir('/home/neclyeux/Documentos')
os.system('python formatarJSON.py')
