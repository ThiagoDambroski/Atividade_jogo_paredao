from Jogo import Jogo
from jogador import Jogador

numero_de_rodadas_round_1 = int(input("numero de rodadas: "))
numero_de_jogadores = int(input("numero de jogadores: "))
jogadores = []
for c in range(numero_de_jogadores):
    jogadores.append(Jogador(str(input(f"digite o nome do jogador {c + 1}: "))))

jogo = Jogo(jogadores,numero_de_rodadas_round_1)
jogo.jogando()
jogo.posicoes()

numero_de_rodadas_round_2 = int(input("numero de rodadas da segunda jogada"))
jogo.segunda_rodada(numero_de_rodadas_round_2)





