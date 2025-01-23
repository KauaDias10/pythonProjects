#LAMBDA
#uma pequena função anonima, porem só pode executar uma expressao
#lamba argumentos : expressão

#a) Crie uma função lambda que multiplica um número por 3 e aplique em uma lista de números de 1 a 10 usando map.

#numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#mult = list(map(lambda x: x*3, numeros))
#print(mult)

#b) Use filter com uma função lambda para retornar apenas os números pares de uma lista.

#numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#numPares = list(filter(lambda x: x % 2 == 0, numeros))
#print(numPares)

#c) Ordene uma lista de dicionários com base em um campo específico usando lambda.

#pessoas = [{'nome': 'João', 'idade': 25}, {'nome': 'Ana', 'idade': 30}, {'nome': 'Carlos', 'idade': 25}]
#maiorIdade = list(map(lambda x: x ['idade'] > 18, pessoas))
#print(f"Adultos: {maiorIdade}")