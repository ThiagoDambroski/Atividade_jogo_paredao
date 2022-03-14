from Jogo import Jogo
from jogador import Jogador

x = int(input("numero de rodadas: "))
y = int(input("numero de jogadores: "))
jogadores = []
for c in range(y):
    jogadores.append(Jogador(str(input(f"digite o nome do jogador {c + 1}: "))))

jogo = Jogo(jogadores,x)
jogo.jogando()
jogo.posicoes()

x = int(input("numero de rodadas da segunda jogada"))
jogo.segunda_rodada(x)





