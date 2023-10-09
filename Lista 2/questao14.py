class Funcionario:
    def __init__(self, nome, salario):
        self.salario = salario
        self.nome = nome

    def aumento(self, aumento):
        self.salario += aumento
        print(str(self.salario))

    def setNome(self, novoNome):
        self.nome = novoNome
        print(str(self.nome))

    def aumentoPercentual(self, aumento):
        self.salario += (self.salario*aumento/100)
        print(str(self.salario))