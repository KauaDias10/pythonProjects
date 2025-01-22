#sintaxe para criar uma lista baseado em uma lista ja existente
#Sintaxe: novaLista = [expressao for item in interable if condition == true]

#animais = ['cat', 'dog', 'turtle', 'bird'] 
#novaLista = []

#for animal in animais:
#    if 't' in animal:
#        novaLista.append(animal)
#
#print(novaLista)

#novaLista = [animal for animal in animais if 't' in animal]

#animais = ['cat', 'dog', 'turtle', 'bird'] 
#novaLista = [animal.upper() for animal in animais]
#print(novaLista)

#animais = ['cat', 'dog', 'turtle', 'bird'] 
#novaLista = [animal if animal != 'dog' else 'horse' for animal in animais] #se é diferente de dog ele lista o animal, se é dog ele troca por horse
#print(novaLista)