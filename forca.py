import csv
import random

# Importando palavras do csv e gerando uma lista
arquivo = 'teams.csv'

listaTimes = []

with open(arquivo, mode='r', encoding='utf-8') as file:
    leitor = csv.reader(file)
    for linha in leitor:
        listaTimes.append(linha[0].strip().lower())  # Adiciona cada time à lista a partir da primeira coluna do CSV

###################################################################

# Gerando time aleatório e salvando progresso
palavraEscolhida = random.choice(listaTimes)  
print(f'A palavra escolhida tem {len(palavraEscolhida)} letras.')

progresso = ['_' for _ in palavraEscolhida] 
print(f'Progresso Inicial: {" ".join(progresso)}')

letrasUsadas = [] 
tentativasErradas = 0  
limiteTentativas = 6 

# Loop principal do jogo
while tentativasErradas < limiteTentativas:  
    print(f"Tentativas restantes: {limiteTentativas - tentativasErradas}")
    letra = input("Digite uma letra: ").strip().lower()  # Lê a entrada do usuário e converte para minúsculo

    # Verifica se a entrada é válida (apenas uma letra)
    if len(letra) != 1 or not letra.isalpha():
        print("Entrada inválida! Digite apenas uma letra.") 
        continue

    # Verifica se a letra já foi usada
    if letra in letrasUsadas:
        print("Você já digitou essa letra. Tente outra.")
        continue

    letrasUsadas.append(letra)  # Adiciona a letra à lista de letras usadas

    # Verifica se a letra está na palavra escolhida
    if letra in palavraEscolhida:
        print(f"Boa! A letra '{letra}' está na palavra.")
        for i, char in enumerate(palavraEscolhida):  # Atualiza o progresso para cada ocorrência da letra
            if char == letra:
                progresso[i] = char
    else:
        print(f"A letra '{letra}' não está na palavra.")
        tentativasErradas += 1  
        
    # Exibe o progresso atual da palavra
    print(f"Progresso: {' '.join(progresso)}")
    print(f"Letras usadas: {''.join(letrasUsadas)}")

    # Verifica se o jogador completou a palavra
    if '_' not in progresso:
        print(f"Parabéns! Você acertou a palavra: {' '.join(progresso)}")
        break
else:
    # Executado se o jogador atingir o limite de tentativas sem acertar a palavra
    print(f"Você perdeu! A palavra era: {palavraEscolhida}")
