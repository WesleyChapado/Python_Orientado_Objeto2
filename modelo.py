#Classe mãe
class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

    def dar_like(self):
        self._likes += 1

    #Método / polimorfia
    def __str__(self):
        return f"{self.nome} - Ano: {self.ano} - Likes:{self.likes}"

#Herança da classe Programa
class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    #Método / polimorfia
    def __str__(self):
        return f"{self.nome} - Ano: {self.ano} - Duração: {self.duracao} - Likes:{self.likes}"

#Herança da classe Programa
class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    #Método / polimorfia
    def __str__(self):
        return f"{self.nome} - Ano: {self.ano} - Temporadas: {self.temporadas} - Likes:{self.likes}"

#Heranca da classe list
class Playlist():
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas= programas

    def __getitem__(self, item):
        return self._programas[item]

    @property
    def listagem(self):
        return self._programas

    def __len__(self):
        return len(self._programas)

#Cria objeto "Filme"
vingadores = Filme('Vingadores - guerra infinita', 2018, 160)
#Da 1 like
vingadores.dar_like()

#Cria objeto "Serie"
atlanta = Serie('atlanta', 2018, 2)
#Da 2 likes
atlanta.dar_like()
atlanta.dar_like()

#Cria lista com 2 objetos
lista = [vingadores, atlanta]

#Cria objeto play list
playlist_fim_de_semana = Playlist('fim de semana', lista )

print(f'Tamanho da Playlist: {len(playlist_fim_de_semana)}')

#Imprime o conteudo da lista
for programa in playlist_fim_de_semana:
    print(programa)