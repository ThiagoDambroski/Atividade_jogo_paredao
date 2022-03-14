from jogador import Jogador


class Jogo():

    def __init__(self, jogadores : list[Jogador], rodadas):
        self.jogadores = jogadores
        self.rodadas = rodadas
        self.ganhador = False
        self.primeiro_lugar = ''
        self.ultimo_lugar = ''

    def jogando(self):
        for c in range(self.rodadas):
            if self.ganhador == False:
                for c in self.jogadores:
                    pontos = int(input(f"Digite os pontos do jogador {c.nome}: "))
                    c.ganha_pontos(pontos)
                    if c.pontos_jogador >= 200:
                        c.pontos_jogador = 200
                        self.ganhador = True


    def posicoes(self):
        maior = 0
        menor = 201
        for c in self.jogadores:
            if c.pontos_jogador > maior:
                maior = c.pontos_jogador
                self.primeiro_lugar = c.nome
            if c.pontos_jogador < menor:
                menor = c.pontos_jogador
                self.ultimo_lugar = c.nome

        self.jogadores = sorted(self.jogadores, key=lambda Jogador: Jogador.pontos_jogador,reverse= True)
        for c in self.jogadores:
            if c == self.jogadores[-1]:
                print(f"{c.nome} ficou em ultimo lugar e ja esta confirmado no paredao")
                self.jogadores[-1].paredao = True
            else:
                print(f"{c.nome} ficou em {self.jogadores.index(c) + 1}")

    def segunda_rodada(self,x):
        for c in self.jogadores:
            c.limpar_pontos()
        for c in range(x):
            for c in self.jogadores:
                if not c.paredao:
                    pontos = int(input(f"Digite os pontos do jogador {c.nome}: "))
                    c.ganha_pontos(pontos)

        self.jogadores = sorted(self.jogadores, key=lambda Jogador: Jogador.pontos_jogador, reverse= True )

        print(f"o jogador {self.jogadores[-1].nome} esta no paredao e o jogador {self.jogadores[-2].nome} tambem esta")

