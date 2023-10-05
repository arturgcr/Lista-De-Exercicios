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
        centro = Ponto(self.largura/2, self.altura/2)
        return centro
    
    def alteraRetanguloImprimeCentro(self, novaLargura, novaAltura):
        self.largura = novaLargura
        self.altura = novaAltura
        centro = Ponto(self.largura/2, self.altura/2)
        print(str(centro))
    
retangulo1 = Retangulo(1,1)
verticeRetangulo1 = Ponto(0,0)
retangulo2 = Retangulo(2,2)
verticeRetangulo2 = Ponto(0,0)
