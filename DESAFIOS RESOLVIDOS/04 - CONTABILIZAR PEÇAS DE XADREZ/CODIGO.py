resultado = {
    "peao": 0,
    "bispo": 0,
    "cavalo": 0,
    "torre": 0,
    "rainha": 0,
    "rei": 0
}

def identificaralphanum(entrada):
    tamanhoentrada = len(entrada)
    for indice in range(0, tamanhoentrada):
        while entrada[indice].isalpha():
            return True
    return False

def validarvalor(entrada):
    while entrada < 0:
        return True
    while entrada > 6:
        return True
    return False

def identificarnumeroslinha(entrada):
    while len(entrada) != 8:
        return True
    return False

def contabiliza(entrada):
    while entrada == 1:
        resultado["peao"] += 1
        break
    while entrada == 2:
        resultado["bispo"] += 1
        break
    while entrada == 3:
        resultado["cavalo"] += 1
        break
    while entrada == 4:
        resultado["torre"] += 1
        break
    while entrada == 5:
        resultado["rainha"] += 1
        break
    while entrada == 6:
        resultado["rei"] += 1
        break


def validarlinha(entrada):
    entradaarray = entrada.split(" ")

    while identificaralphanum(entradaarray):
        print("Por favor, digite apenas números.")
        return False

    while identificarnumeroslinha(entradaarray):
        print("Por favor, digite 8 números entre 0 e 6 com um espaço entre cada número!")
        return False

    tamanhoentradaarray = len(entradaarray)

    for indice in range(0, tamanhoentradaarray):
        valor = int(entradaarray[indice])
        while validarvalor(valor):
            print("Por favor, digite apenas números entre 0 e 6!")
            return False

    for indice in range(0, tamanhoentradaarray):
        valor = int(entradaarray[indice])
        contabiliza(valor)

    return True


print("{}SOFTWARE PARA CONTABILIZAR PEÇAS{}".format(12*"=", 12*"="))
print("{}EM UM TABULEIRO DE XADREZ{}".format(15*"=", 15*"="))
print("{}Cada entrada representa uma linha do tabuleiro.{}".format(2*"*", 2*"*"))
print("{}Cada linha do tabuleiro possui 8 peças.{}".format(2*"*", 2*"*"))
print("{}As peças são representadas por números entre 0 e 6.{}".format(2*"*", 2*"*"))
print("{}Em cada linha os números devem ter um espaço entre eles.{}\n".format(2*"*", 2*"*"))
for i in range(0, 8):
    linha = input('Digite os dados da linha {}:\n>>> '.format(i + 1))
    while not validarlinha(linha):
        linha = input('Digite os dados da linha {}:\n>>> '.format(i + 1))


print("\nPeão: {} peça(s)".format(resultado["peao"]))
print("\nBispo: {} peça(s)".format(resultado["bispo"]))
print("\nCavalo: {} peça(s)".format(resultado["cavalo"]))
print("\nTorre: {} peça(s)".format(resultado["torre"]))
print("\nRainha: {} peça(s)".format(resultado["rainha"]))
print("\nRei: {} peça(s)".format(resultado["rei"]))
