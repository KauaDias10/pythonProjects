#a) Crie uma lista de números pares de 1 a 20 usando list comprehension.
#numPares = [num for num in range(1, 21) if num % 2 == 0]
#print(numPares)

#b) Dada a lista ['python', 'java', 'c++', 'go'], crie outra lista que contenha o tamanho de cada string.
#lista = ['python', 'java', 'c++', 'go']
#tamString = [len(palavra) for palavra in lista]
#print(tamString)

#c)Gere uma matriz 3x3 usando list comprehension (uma lista de listas com valores de 1 a 9).
#matriz = [[coluna + linha * 3 for coluna in range(1,4)] for linha in range(3)]
# print(matriz)

#d) Combine duas listas ([1, 2, 3] e [4, 5, 6]) em pares ordenados, formando uma lista como [(1, 4), (2, 5), (3, 6)].

lista1 = [1,2,3]
lista2 = [4,5,6]
pares = [(a,b) for a, b in zip(lista1, lista2)]
print(pares)