class Macaco:
    def __init__(self, nome):
        self.nome = nome
        self.bucho = []
    
    def comer(self, item):
        self.bucho.append(item)

    def digerir(self, item):
        self.bucho.clear()

    def verBucho(self):
        return self.bucho