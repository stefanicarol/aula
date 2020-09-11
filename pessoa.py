class Pessoa:

    def __init__(self, nome, data, sexo, peso):
        self.nome = nome
        self.data = data
        self.sexo = sexo
        self.peso = peso
        self.filhos = []

    def imprimir(self):
        print(self.filhos)

    def imprimirPessoa(self):
        print(self.nome)
        print(self.data)
        print(self.sexo)
        print(self.peso)

    def addFilho(self, filho):
        if filho in self.filhos:
            pass
        self.filhos.append(filho)

    def __str__(self):
        return self.nome
