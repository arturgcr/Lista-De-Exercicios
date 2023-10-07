class Carro:
    def __init__(self, kmPorLitro):
        self.tanque = 0
        self.kmPorLitro = kmPorLitro
        
    def andar(self, distancia):
        """distância em kilometros"""
        self.tanque -= (distancia/self.kmPorLitro)

    def obterGasolina(self):
        return self.tanque

    def adicionarGasolina(self, gasolinaReabastecida):
        self.tanque += gasolinaReabastecida