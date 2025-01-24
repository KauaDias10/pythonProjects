#a) Dada uma lista de números, filtre os números ímpares, eleve-os ao quadrado e crie um conjunto com esses valores. Use lambda e list comprehension.

#numeros impares
#listaNum = [num for num in range(1 , 21) if num % 2 != 0]
#potencia = list(map(lambda x: x**2, listaNum))
#conjunto = set(potencia)
#print(potencia)

#b) Crie uma função que receba uma lista de nomes e retorne uma lista de tuplas. Cada tupla deve conter o nome e o número de caracteres do nome.

#def receba(lista):
#    resultado = [(item, len(item)) for item in lista]  # Cria uma lista de tuplas
#    return resultado  # Retorna a lista de tuplas
#
#nomes = ['Kaua', 'Kauazum', 'Kauazao', 'Kauazon', 'Kauazin']
#
#resultado = receba(nomes)  # Chama a função
#print(resultado)  # Imprime o resultado
    