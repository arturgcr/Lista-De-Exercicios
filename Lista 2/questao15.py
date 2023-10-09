class BichoVirtual:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.fome = 1000
        self.saude = 100

    def alterarNome(self, novoNome):
        self.nome = novoNome

    def alterarIdade(self, novaIdade):
        self.idade = novaIdade
    
    def alterarSaude(self, novaSaude):
        self.saude = novaSaude

    def alterarFome(self, novaFome):
        self.alterarFome = novaFome

    def retornaNome(self):
        return self.nome
    
    def retrnaFome(self):
        return self.fome
    
    def retornaSaude(self):
        return self.saude
    
    def retornaIdade(self):
        return self.idade
    
    def humor(self):
        return self.fome + self.idade

    def alimentarPorQtd(self, comida):
        self.fome += comida

    def brincarPorTempo(self, tempo):
        self.saude += tempo