import random

class Bichinho:
    def __init__(self, nome):
        self.nome = nome
        self.fome = random.randint(0, 50)
        self.saude = random.randint(50, 100)
        self.tedio = random.randint(0, 50)

    def alimentar(self):
        self.fome -= 10
        if self.fome < 0:
            self.fome = 0

    def brincar(self):
        self.saude += 10
        self.tedio -= 10
        if self.saude > 100:
            self.saude = 100
        if self.tedio < 0:
            self.tedio = 0

    def falar(self):
        if self.fome > 50 or self.tedio > 50:
            return f"{self.nome}: Estou com fome e entediado!"
        else:
            return f"{self.nome}: Estou bem!"

def main():
    fazenda = []
    num_bichinhos = int(input("Quantos bichinhos você deseja criar na fazenda? "))

    for i in range(num_bichinhos):
        nome = input(f"Digite o nome do bichinho {i+1}: ")
        bichinho = Bichinho(nome)
        fazenda.append(bichinho)

    while True:
        print("\nMenu:")
        print("1 - Alimentar todos os bichinhos")
        print("2 - Brincar com todos os bichinhos")
        print("3 - Ouvir todos os bichinhos")
        print("4 - Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            for bichinho in fazenda:
                bichinho.alimentar()
        elif escolha == "2":
            for bichinho in fazenda:
                bichinho.brincar()
        elif escolha == "3":
            for bichinho in fazenda:
                print(bichinho.falar())
        elif escolha == "4":
            break
        else:
            print("Opção inválida. Escolha novamente.")

if __name__ == "__main__":
    main()
