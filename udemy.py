def compare(txt, list):
    for item in list:
        if txt == item:
            return True
    return False

class Cliente():
    def __init__(self, nome, telefone, idade):
        self.nome= nome
        self.telefone= telefone
        self.idade=idade

    def mudarNome(self, novoNome):
        self.nome = novoNome
        print(novoNome)

c = Cliente("Carol","88888","18 anos")
print(c.nome, c.telefone, c.idade)
c.mudarNome("Stefani")
print(c.nome, c.telefone, c.idade)