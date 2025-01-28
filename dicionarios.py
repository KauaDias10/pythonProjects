#DICIONARIOS  
#  listas usamos []
#  tuplas usamos ()
#  strings usamos '' ou ""
#  dicionario {chave:valor} -> chave podera ser uma string ou int
#o valor pode ser lista,string

empregados = {'01':['João Silva'], 
              '02':['Maria','das Graças'],
              '03':['Pedro','Silva']}

#print(empregados['01'])
#empregados['04'] = ['kaua','santos']
#
#del empregados['01']
#print(empregados)

#num = input("Digite o numero do funcionario: ")
#nome = input("Digite o nome: ")
#
#if empregados.get(num):
#    print('Funcionario ja cadastrado!')
#else:
#    empregados[num]=[nome]
#
#print(empregados)

#empregados.setdefault('03 ','kauazao')
#print(empregados)

#dias = {'sex':'Sexta','seg':'Segunda'}
#
#chaves = dias.keys()
#print(type(chaves)) 

import copy

dias_copy = copy.deepcopy(dias)
dias_copy['Dom'] = 'Domingo'