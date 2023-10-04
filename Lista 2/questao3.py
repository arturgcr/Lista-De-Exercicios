

class Retangulo():
    def __init__(self, lA, lB):
        self.ladoA = lA
        self.ladoB = lB

    def setLado(self, novoLadoA, novoLadoB):
        self.ladoA = novoLadoA
        self.ladoB = novoLadoB

    def getLados(self):
        return self.ladoA, self.ladoB
    def calculaArea(self):
        return self.ladoA * self.ladoB
    def calculaPerimetro(self):
        return (self.ladoA * 2) + (self.ladoB * 2)

novoLadoA = input("Insira um valor para o peimeiro lado: ")
novoLadoB = input("Insira um valor para o segundo lado: ")

retangulo = Retangulo(novoLadoA, novoLadoB)

print("área: " + str(retangulo.calculaArea))

print("considerando um piso de 1 m2 você precisará de " + str(round(retangulo.calculaArea() + 0.5)) + " pisos para cobrir seu chão")
print("também precisará de um comprimento de " + str(round(retangulo.calculaPerimetro() + 0.5)) + " para o rodapé")