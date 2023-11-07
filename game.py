import json
import random

def ler_json(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as arquivo:
            dados = json.load(arquivo)
            return dados
    except:
        return { "jogadores": [], "pontuacao_media": 0 }

def armazenar_ranking_json(ranking):
    with open(nome_arquivo, "w") as arquivo:
        jsonStr = json.dumps(ranking, indent = 4)
        arquivo.write(jsonStr)
        
def inserir_ranking_jogador(rank_jogador, ranking):
    tentativas_jogador = rank_jogador['tentativas']
    possui_ranking = False
    
    if 'jogadores' in ranking == False: ranking['jogadores'] = []
    
    for rank in ranking['jogadores']:
        if rank['nome'] == rank_jogador['nome']:
            possui_ranking = True
            if rank['tentativas'] > tentativas_jogador:
                    rank['tentativas'] = tentativas_jogador
    
    if possui_ranking == False:
        ranking['jogadores'].append(rank_jogador)
              
def calcular_media_tentativas(ranking):
    total_tentativas = 0
    
    for rank in ranking['jogadores']: 
        total_tentativas += rank['tentativas']
    
    total_jogadores = len(ranking['jogadores'])
    media = total_tentativas / total_jogadores
    return round(media, 2) 
    
nome_arquivo = 'ranking.json'

numero_secreto = random.randint(1, 100)

ranking = ler_json(nome_arquivo)

nome = input('Olá! Qual é o seu nome? ')
print(f'Olá {nome}! Bem-vindo ao jogo de adivinhação!')
print('Tente adivinhar o número secreto entre 1 e 100!')

tentativas = 0

while True:
    try:
        tentativa = int(input('Digite um numero: '))
    except ValueError:
        print('Digite um numero valido')

    tentativas += 1

    if tentativa == numero_secreto:
        print(f'Parabéns! Você acertou o número {numero_secreto} em {tentativas} tentativa(s).')
        
        inserir_ranking_jogador({"nome": nome, "tentativas": tentativas}, ranking)
        
        jogadores_ordenados = sorted(ranking['jogadores'], key=lambda x: x['tentativas'])
        ranking['jogadores'] = jogadores_ordenados
        
        media_pontuacao = calcular_media_tentativas(ranking)
        ranking['pontuacao_media'] = media_pontuacao
        
        armazenar_ranking_json(ranking)
        
        print('=== RANKING ===')
        for i, jogador in enumerate(ranking['jogadores']): 
            print(f'{i + 1}. {jogador["nome"]}: {jogador["tentativas"]} tentativa(s)')

        print(f'A pontuação média das tentativas dos jogadores é de: {media_pontuacao:}')
                
        break
    elif tentativa < numero_secreto:
        print(f'O número é maior do que {tentativa}.')
    else:
        print(f'O número é menor do que {tentativa}.')






#Jogo de adivinhação em que o jogador tenta adivinhar um número secreto escolhido aleatoriamente pelo computador usando a biblioteca random entre 1 e 100. O jogo começa solicitando ao jogador que insira seu nome e, em seguida, exibe uma mensagem de boas vidas personalizada.
#Dentro de um loop principal, o jogo continua até que o jogador adivinhe o número correto. O jogador é solicitado a fazer palpite, e o número de tentativas é contado e selecionado conforme o jogador for errando. O jogador recebe dicas para adivinhar se o número secreto é maior ou menor que o palpite atual.
#O jogo também mantém um ranking de jogadores, armazenando seus nomes e o número mínimo de tentativas possíveis para adivinhar o número. O ranking é atualizado após cada jogo.
#No final do jogo mostra o ranking junto com a media de cada jogador