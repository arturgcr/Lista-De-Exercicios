class Pessoa:
    def __init__(self, nome,idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self):
        self.idade += 1
        
        if self.idade < 21:
            self.altura += 0.5

    def engordar(self):
        self.peso += 1

    def crescer(self):
        self.altura += 1