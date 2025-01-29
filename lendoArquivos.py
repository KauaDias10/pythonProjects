#read(n), read(), readline(), readlines() usados para leitura

letra = open('letra.txt','r')

#print(letra.read(5)) #retorna os 5 primeiros caracteres
#print(letra.read()) #retorna todo o texto do arquivo
#print(letra.readline()) #retorna a primeira linha
#print(letra.readlines()) #retorna uma lista contendo cada uma das linhas
#print(len(letra.readlines())) #retorna quantas linhas tem o arquivo

#contando as palavras
#print(lista_palavras.count('timeless'))#


palavras = letra.read() #lendo todo o arquivo
lista_palavras = palavras.split() ##transformando as palavras em lista
print(len(lista_palavras))#contando as palavras
set_palavras = set(lista_palavras)#contando as palavras sem repetir 
print(len(set_palavras))

