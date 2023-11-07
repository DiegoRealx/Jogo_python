import random

numero_secreto = random.randint(1, 100)
tentativas = 0
ranking = []

nome = input('Olá! Qual é o seu nome? ')
print(f'Olá {nome}! Bem-vindo ao jogo de adivinhação!')
print('Tente adivinhar o número secreto entre 1 e 100!')

while True:
    try:
        tentativa = int(input('Digite um numero: '))
    except ValueError:
        print('Digite um numero valido')
            
    tentativas += 1

    if tentativa < numero_secreto:
        print('O número é maior do que o que você tentou.')
    elif tentativa > numero_secreto:
        print('O número é menor do que o que você tentou.')
    else:
        print(f'Parabéns, {nome}! Você adivinhou o número corretamente: {numero_secreto} em {tentativas} tentativas.')

        ranking.append((nome, tentativas))
        with open('ranking.txt', 'a') as file:
            file.write(f'{nome}: {tentativas} tentativas\n')

        print('== RANKING ==')
        ranking.sort(key=lambda x: x[1])
        for i, (jogador, tentativas) in enumerate(ranking, start=1):
            print(f'{i}. {jogador}: {tentativas} tentativas')
        break

try:
    with open('ranking.txt', 'r') as file:
        ranking = file.readlines()
        
        if len(ranking) == 0:
            print('O ranking está vazio.')
        else:
            total_tentativas = 0
            total_jogadores = 0

            for linha in ranking:
                jogador, tentativas_str = linha.split(":")
                tentativas = int(tentativas_str.split()[0])
                total_tentativas += tentativas
                total_jogadores += 1
                print(linha.strip())

            media = total_tentativas / total_jogadores
            print(f'A média de tentativas foi: {media:.2f}')
            ranking.sort(key=lambda x: int(x.split(":")[1].split()[0]))

            print('== RANKING FINAL ==')
            for i, linha in enumerate(ranking, start=1):
                print(f'{i}. {linha.strip()}')

except FileNotFoundError:
    print('Arquivo não encontrado.')






#Jogo de adivinhação em que o jogador tenta adivinhar um número secreto escolhido aleatoriamente pelo computador usando a biblioteca random entre 1 e 100. O jogo começa solicitando ao jogador que insira seu nome e, em seguida, exibe uma mensagem de boas vidas personalizada.
#Dentro de um loop principal, o jogo continua até que o jogador adivinhe o número correto. O jogador é solicitado a fazer palpite, e o número de tentativas é contado e selecionado conforme o jogador for errando. O jogador recebe dicas para adivinhar se o número secreto é maior ou menor que o palpite atual.
#O jogo também mantém um ranking de jogadores, armazenando seus nomes e o número mínimo de tentativas possíveis para adivinhar o número. O ranking é atualizado após cada jogo.
#No final do jogo mostra o ranking junto com a media de cada jogador