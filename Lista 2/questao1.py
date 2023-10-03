class Bola():
    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material
    
    def trocaCor(self, cor):
        self.cor = cor

    def mostraCor(self):
        return "A cor da bola é:" + str(self.cor)

