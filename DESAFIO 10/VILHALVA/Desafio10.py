import sys

def ler_programa(arquivo_programa):
    programa = list()
    try:
        file = open(arquivo_programa, "r")
    except IOError:
        return -1

    linhas = file.readlines()

    for linha in linhas:
        dados = linha.split(";")
        sem_comentarios = dados[0].strip()
        if sem_comentarios != "":
            comando = sem_comentarios.split(" ")
            if len(comando) < 5:
                return -2
            programa.append(comando)

    return programa

def buscar_comando(estado_atual, leitura, programa):
    ret = []
    ret2 = []

    ret = [i for i in programa if i[0] == estado_atual or i[0] == "*"]

    if not ret:
        return -1

    ret2 = [i for i in ret if i[1] == leitura or i[1] == "*"]

    if not ret2:
        return -1

    for i in ret2:
        if i[0] == estado_atual and i[1] == leitura:
            return i
    return ret2[0]

def turing(programa, dado):
    posicao_cabeca = 0
    estado_atual = "0"

    while True:
        leitura = dado[posicao_cabeca]
        comando = buscar_comando(estado_atual, leitura, programa)
        if comando == -1:
            return "ERR"
        if comando[2] != "*":
            dado[posicao_cabeca] = comando[2]
        estado_atual = comando[4]
        if "halt" in estado_atual:
            break
        if comando[3] == "l":
            posicao_cabeca = posicao_cabeca - 1
            if posicao_cabeca == -1:
                dado = ["_"] + dado
                posicao_cabeca = 0
        elif comando[3] == "r":
            posicao_cabeca = posicao_cabeca + 1
            if posicao_cabeca == len(dado):
                dado = dado + ["_"]

    return dado

def main():
    if len(sys.argv) < 2:
        print("Erro ! Sintaxe: python Desafio10.py nome_do_arquivo")
        sys.exit(0)

    try:
        file = open(sys.argv[1], "r")
    except IOError:
        print("Não consegui abrir o arquivo", sys.argv[1])
        sys.exit(0)

    linhas = file.readlines()

    for linha in linhas:
        dados = linha.split(",")
        try:
            arquivo_programa = dados[0].rstrip()
            dados = dados[1].rstrip()
            dados = dados.replace(" ", "_")

        except IndexError:
            print("Arquivo de entrada", sys.argv[1], "inválido !")
            sys.exit(0)

        dado = list(dados)
        programa = ler_programa(arquivo_programa)

        if programa == -1:
            print("Erro na leitura do arquivo!", arquivo_programa)
            sys.exit(0)
        elif programa == -2:
            print("ERRO: Comandos inválidos!!!", arquivo_programa)
            sys.exit(0)

        ret = turing(programa, dado)
        ret = "".join(ret)
        ret = ret.replace("_", " ").strip()
        dados = dados.replace("_", " ")
        print(arquivo_programa, dados, ret, sep=',')
    file.close()

if __name__ == "__main__":
    main()
