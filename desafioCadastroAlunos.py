#Crie um programa em Python que utilize dicionários para gerenciar um sistema de cadastro de alunos. O programa deve oferecer as seguintes funcionalidades:

def exibirMenu():
    print("Escolha uma opção:")
    print("1. Cadastrar novo aluno")
    print("2. Exibir todos os alunos")
    print("3. Atualizar informações de um aluno")
    print("4. Remover um aluno")
    print("5. Sair")

#função para cadastro de alunos
def cadastroAlunos():
    nome = input("Digite o nome do aluno: ")
    idade = int(input("Digite a idade do aluno: "))
    nota = float(input("Digite a nota do aluno: "))
    alunos[nome] = [idade, nota] 
    print(f"Aluno {nome} Cadastrado com sucesso!")

def exibirAlunos():
        if alunos:
            for nome, info in alunos.items():
                print(f"{nome}: Idade: {info[0]}, Nota: {info[1]}")
            else:
                print("Não há alunos cadastrados.")

def atualizarAlunos(nome,idade,nota):
    if nome in alunos:
        alunos.update({nome: {"idade": idade, "nota": nota}})
        print(f'Alunos Atualizados{alunos}')
    else:
        print('Aluno não foi Criado')            
    
def deletarAlunos(nome):
    if nome in alunos:
        del alunos[nome]
    else:
        print('Esse aluno não EXISTE')   

alunos = {}

#loop principal

print("Bem vindo ao Sistema de Cadastro de Alunos!")
while True:
    
    exibirMenu()
    opcao = input("Escolha uma opção (1-5)")
    
    if opcao == '1':
        cadastroAlunos()
    elif opcao == '2':
        exibirAlunos()
    elif opcao == '3':
        atualizarAlunos()
    elif opcao == '4':
        deletarAlunos()
    elif opcao == '5':
        print("Saindo do programa...")
        break  # Encerra o loop e o programa
    else:
        print("Opção inválida! Tente novamente.")


