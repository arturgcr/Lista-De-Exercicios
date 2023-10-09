class Bichinho:
    def __init__(self, nome, fome=0, saude=100, idade=0):
        self.nome = nome
        self.fome = fome
        self.saude = saude
        self.idade = idade

    def alimentar(self):
        self.fome -= 10
        if self.fome < 0:
            self.fome = 0

    def brincar(self):
        self.saude += 10
        self.fome += 10
        self.idade += 1

    def envelhecer(self):
        self.idade += 1

    def __str__(self):
        return f'Nome: {self.nome}\nFome: {self.fome}\nSaúde: {self.saude}\nIdade: {self.idade}'


if __name__ == "__main__":
    nome_bichinho = input("Digite o nome do bichinho: ")
    bichinho = Bichinho(nome_bichinho)

    while True:
        print("\nMenu:")
        print("1 - Alimentar o bichinho")
        print("2 - Brincar com o bichinho")
        print("3 - Envelhecer o bichinho")
        print("4 - Mostrar status secreto")
        print("5 - Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            bichinho.alimentar()
        elif escolha == "2":
            bichinho.brincar()
        elif escolha == "3":
            bichinho.envelhecer()
        elif escolha == "4":
            print("\nStatus secreto do bichinho:")
            print(bichinho)
        elif escolha == "5":
            break
        else:
            print("Opção inválida. Escolha novamente.")
