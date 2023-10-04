class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getPonto(self):
        print((self.x,self.y))
    
class Retangulo:
    def __init__(self, altura, largura):
        self.largura = largura
        self.altura = altura
    
    def centroRetangulo(self):
        return [(self.largura/2, self.altura/2)]
    
    