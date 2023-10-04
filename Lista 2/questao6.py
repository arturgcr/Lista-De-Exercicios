class TV:
    def __init__(self):
        self.volume = 50
        self.canal = 1

    def mudaCanal(self, numeroCanal):
        self.canal = numeroCanal
    
    def aumentaVolume(self):
        self.volume += 1
        if self.volume > 100:
            self.volume = 100

    def diminuirVolume(self):
        self.volume -= 1
        if self.volume < 0:
            self.volume = 0