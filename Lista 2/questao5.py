class Conta:
    def __init__(self, numero, nome, saldo = 0):
        self.nome = nome
        self.numeroConta = numero
        self.saldo = saldo

    def alterarNome(self, nomeAlterado):
        self.nome = nomeAlterado

    def deposito(self, valor):
        self.saldo += valor
    
    def saque(self, valor):
        self.saldo -= valor
    
