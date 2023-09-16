# Questão 11.
def numeroInteiroReal():
    verifica = True

    primeiroNumeroInteiro = input("Insira um número inteiro: ")
    while not (primeiroNumeroInteiro.isdigit()):
        primeiroNumeroInteiro = input("Erro, insira novamente: ")

    segundoNumeroInteiro = input("Insira outro número inteiro: ")
    while not (segundoNumeroInteiro.isdigit()):
        segundoNumeroInteiro = input("Erro, insira novamente: ")

    numeroReal = input("Insira um número real: ")

    excessao = False
    while verifica:
        if not numeroReal.isdigit():
            try:
                numeroReal = float(numeroReal)
                verifica = False
            except:
                excessao = True
                numeroReal = input("Erro, insira novamente: ")

        if verifica and not excessao:
            numeroReal = input("Erro, insira novamente: ")
    

    print(str(int(primeiroNumeroInteiro)*int(segundoNumeroInteiro)))
    print(str((3*int(primeiroNumeroInteiro)) + float(numeroReal)))
    print(str(float(numeroReal)**3))

#Questão 12
def pesoIdeal():
    altura = input("Insira sua altura: ")
    sair = False
    while not sair:
        try:
            print("Seu peso ideal é: " + str(round((float(altura)*72.7)-58, 1)))
            sair = True
        except:
            altura = input("Erro, insira novamente: ")

#Questão 13
def pesoIdealPorGenero():
    verifica = True
    genero = input("Insira seu gênero: ")

    while verifica:
        if genero.lower() in ['homem', 'mulher', "h", "m"]:
            verifica = False
        
        else:
            genero = input("Erro, insira novamente: ")

    altura = input("Insira sua altura: ")
    sair = False
    while not sair:
        try:
            altura = float(altura)
            sair = True
        except:
            altura = input("Erro, insira novamente: ")

    if genero in ["homem", "h"]:
        print(str(72.7*float(altura) - 58))
    else:
        print(str(62.1*float(altura) - 44.7))

#Questão 14
def calculoDeMulta(peso):
    if peso > 50:
        excesso = peso - 50
        multa = excesso * 4
        print("O limite foi excedido por " + str(excesso) + "Kg, a multa será de: " + str(multa) + " reais.")
    
    else:
        print("Tudo dentro do limite :)")


if __name__ == "__main__":
    calculoDeMulta(80)

