class Cliente:
    def __init__(self, nome):
        self.nome = nome

class ClienteEmpresa(Cliente):
    def __init__(self, nome, cnpf):
        self.cnpf = cnpf
        super().__init__(nome)

    def __repr__(self):
        return 'Nome: {} CNPJ:{}  '.format(
                self.nome,
                self.cnpf,
        )

class ClienteFisica(Cliente):
    def __init__(self, nome, cpf):
        self.cpf = cpf
        super().__init__(nome)

    def __repr__(self):
        return 'Nome: {} CPF:{}  '.format(
            self.nome,
            self.cpf,
        )

class Conta:
    def __init__(self, agencia, numero, cliente):
        self.agencia = agencia
        self.numero = numero
        self.cliente = cliente
        self.saldo = 0
        self.extrato = ExtratoConta()

    def __repr__(self):
        return 'Agencia: {} Número:{} Titular: {}'.format(
            self.agencia,
            self.numero,
            self.titular
        )

    def sacar(self, valor):
        self.saldo = self.saldo - valor
        self.extrato.movimentacoes.append('saque de {}'.format(valor))

    def deposito(self, valor):
        self.saldo = self.saldo + valor
        self.extrato.movimentacoes.append('deposito de {}'.format(valor))


class ExtratoConta:
    def __init__(self):
        self.movimentacoes = []

    def imprime(self):
        print('transacoes')
        for item in  self.movimentacoes:
            print(item)