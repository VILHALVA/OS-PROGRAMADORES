def main():
    print("Solução do Desafio 03 - imprimir todos os números palindrômicos entre dois outros!")

    palindromo()

def palindromo():
    num1 = 1
    num2 = 200

    for i in range(num1, num2 + 1):
        if e_palindromo(i):
            print("Palindromo:", i)

def e_palindromo(num):
    if not num:
        return False

    num_str = str(num)
    return num_str == num_str[::-1]

main()
