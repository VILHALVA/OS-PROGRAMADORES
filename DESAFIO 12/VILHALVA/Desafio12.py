import sys
import math

def check_number(s):
    p = 0
    n = int(s)
    while True:
        if n == 0:
            print(s, "false")
            break
        if n & 1 == 1:
            if n == 1:
                print(s, "true", p)
            else:
                print(s, "false")
            break
        n = n >> 1
        p += 1

def main():
    if len(sys.argv) != 2:
        print("Uso: python Desafio12.py <arquivo>")
        sys.exit(1)

    try:
        with open(sys.argv[1], "r") as file:
            for line in file:
                s_number = line.strip()
                check_number(s_number)

    except IOError as e:
        print("Erro! Não foi possível ler o arquivo:", e)
        sys.exit(1)

if __name__ == "__main__":
    main()
