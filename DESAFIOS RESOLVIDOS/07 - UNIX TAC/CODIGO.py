import sys
from collections import deque

def read_array(char_chunk, impressao):
    for byte in reversed(char_chunk):
        if chr(byte) == '\n':
            print_string(impressao)
        impressao.appendleft(byte)

def print_string(lista):
    bytes_content = bytearray(lista)
    lista.clear()
    print(bytes_content.decode('utf-8'), end='')

def main():
    if len(sys.argv) != 2:
        print("Digite python3 CODIGO.py <nome-arquivo>")
        return

    size_array = 1000000

    try:
        file_name = sys.argv[1]
        with open(file_name, 'rb') as file:
            pos_ptr = file.seek(0, 2)
            pos_atual = 0
            impressao = deque()

            while pos_ptr > 0:
                pos_atual = max(pos_ptr - size_array, 0)
                file.seek(pos_atual)
                char_chunk = file.read(pos_ptr - pos_atual)
                read_array(char_chunk, impressao)
                pos_ptr = pos_atual

            print_string(impressao)

    except Exception as e:
        raise RuntimeError("Ocorreu algum erro") from e

if __name__ == "__main__":
    main()
