from math import gcd

class Fracao:
    def __init__(self, numerador, denominador):
        self.numerador = numerador
        self.denominador = denominador

    def simplificar(self):
        mdc = gcd(self.numerador, self.denominador)
        return Fracao(self.numerador // mdc, self.denominador // mdc)

    def __str__(self):
        if self.denominador == 0:
            return "ERR"

        if self.numerador < self.denominador:
            return f"{self.numerador}/{self.denominador}"

        resto = self.numerador % self.denominador
        novo_numerador = self.numerador // self.denominador

        if resto == 0:
            return f"{novo_numerador}"

        return f"{novo_numerador} {resto}/{self.denominador}"

def main():
    import sys

    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue

        splitted = line.split("/")
        numerador = int(splitted[0])
        denominador = int(splitted[1]) if len(splitted) == 2 else 1

        print(Fracao(numerador, denominador).simplificar())

if __name__ == "__main__":
    main()
