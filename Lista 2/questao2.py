class Quadrado():
    def __init__(self, lado):
        self.tamanhoLado = lado

    def mudarLado(self, novoLado):
        self.tamanhoLado = novoLado

    def retornaLado(self):
        return self.tamanhoLado
    
    def area(self):
        return (self.tamanhoLado * self.tamanhoLado)
