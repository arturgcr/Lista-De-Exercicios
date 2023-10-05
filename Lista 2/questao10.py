class BombaCombustivel:
    def __init__(self, tipoCombustivel, valorLitro, quantidadeCombustivel):
        self.quantidadeCombustivel = quantidadeCombustivel
        self.tipoCombustivel = tipoCombustivel
        self.valorLitro = valorLitro

    def abastecerPorValor(self, valor):
        return round((valor // self.valorLitro)-0.5)
    
    def abastecerPorLitro(self, litro):
        return litro * self.valorLitro
    
    def alterarValor(self, novoValor):
        self.valorLitro = novoValor

    def alterarCombustivel(self, novoCombustivel):
        self.tipoCombustivel = novoCombustivel 

    def alterarQuantidadeCombustivel(self, qtdCombustivel):
        self.quantidadeCombustivel = qtdCombustivel