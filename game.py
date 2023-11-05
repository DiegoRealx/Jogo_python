import random

# Gera um número secreto aleatório
numero_secreto = random.randint(1, 100)


tentativas = 0

# Lista para armazenar os resultados do jogo
ranking = []


nome = input('Olá! Qual é o seu nome? ')
print(f'Olá {nome}! Bem-vindo ao jogo de adivinhação!')
print('Tente adivinhar o número secreto entre 1 e 100!')

# Loop do jogo que continua até o jogador adivinhar o número
while True:
    # Pede para o jogador fazer uma tentativa e soma ela
    tentativa = int(input('Digite um número: '))
    tentativas += 1

    # Fornecendo feedback ao jogador com base na tentativa em relação ao número secreto
    if tentativa < numero_secreto:
        print(f'O número é maior do que {tentativa}')
    elif tentativa > numero_secreto:
        print(f'O número é menor do que {tentativa}')
    else:
        print(f'Parabéns, {nome}! Você adivinhou o número corretamente: {numero_secreto} em {tentativas} tentativas.')

        # Adiciona o resultado atual à lista de ranking
        ranking.append((nome, tentativas))

        # Escreve no arquivo de ranking os resultados do jogador atual
        with open('ranking.txt', 'a') as file:
            file.write(f'{nome}: {tentativas} tentativas\n')

        # mostra o ranking atual de forma ordenada 
        print('== RANKING ==')
        ranking.sort(key=lambda x: x[1])
        for i, (jogador, tentativas) in enumerate(ranking):
            print(f'{i + 1}. {jogador}: {tentativas} tentativas')

        break 
# Calculando a média de todas as pontuações dos jogadores
try:
    with open('ranking.txt', 'r') as file:
        ranking = file.readlines() # Lê as linhas do arquivo e armazena na lista 'ranking'
        
        if len(ranking) == 0:
            print('O ranking está vazio.')
        else:
            print('== RANKING ==')
            
            # variáveis para calcular a média
            total_tentativas = 0
            total_jogadores = 0
            
            # Itera sobre cada linha no ranking
            for linha in ranking: 
                jogador, tentativas_str = linha.split(":") # Divide a linha em jogador e tentativas
                tentativas = int(tentativas_str.split()[0]) # Converte as tentativas para um número inteiro
                total_tentativas += tentativas # Soma as tentativas ao total de tentativas
                #  o contador de jogadores
                total_jogadores += 1
                # Exibe a linha do ranking
                print(linha.strip())

            # Calcula a média das tentativas
            media = total_tentativas / total_jogadores

            # Mostra a média formatada com duas casas decimais
            print(f'A média de tentativas foi: {media:.2f}')

except FileNotFoundError:
    print('Arquivo não encontrado.')



#Jogo de adivinhação em que o jogador tenta adivinhar um número secreto escolhido aleatoriamente pelo computador usando a biblioteca random entre 1 e 100. O jogo começa solicitando ao jogador que insira seu nome e, em seguida, exibe uma mensagem de boas vidas personalizada.
#Dentro de um loop principal, o jogo continua até que o jogador adivinhe o número correto. O jogador é solicitado a fazer palpite, e o número de tentativas é contado e selecionado conforme o jogador for errando. O jogador recebe dicas para adivinhar se o número secreto é maior ou menor que o palpite atual.
#O jogo também mantém um ranking de jogadores, armazenando seus nomes e o número mínimo de tentativas possíveis para adivinhar o número. O ranking é atualizado após cada jogo.
#No final do jogo mostra o ranking junto com a media de cada jogador