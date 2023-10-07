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


if __name__ == "__main__":
    funcionario = Funcionario("Artur", 1300)
    funcionario.aumento(500)
    funcionario.setNome("Artur Rodrigues")

    """
    1800
    Artur Rodrigues
    """
