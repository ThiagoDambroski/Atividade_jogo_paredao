
class Jogador():

    def __init__(self,nome):
        self.nome = nome
        self.pontos_jogador = 0
        self.paredao = False
        self.ganhador = False

    def ganha_pontos(self,x):
        self.pontos_jogador += x

    def limpar_pontos(self):
        self.pontos_jogador = 0