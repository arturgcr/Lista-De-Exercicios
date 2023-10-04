class Quadrado():
    def __init__(self, lado):
        self.tamanhoLado = lado

    def setLado(self, novoLado):
        self.tamanhoLado = novoLado

    def getLado(self):
        return self.tamanhoLado
    
    def area(self):
        return (self.tamanhoLado * self.tamanhoLado)
