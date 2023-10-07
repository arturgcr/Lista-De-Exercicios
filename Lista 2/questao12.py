class contaInvestimento:
    def __init__(self, numero, nome, saldo = 0):
        self.nome = nome
        self.numeroConta = numero
        self.saldo = saldo
        self.taxaDeJuros = 0

    def adicioneJuros(self, juros):
        self.taxaDeJuros = juros

    def poupanca(self, meses):
        self.saldo = self.taxaDeJuros * meses
        print(str(self.saldo))