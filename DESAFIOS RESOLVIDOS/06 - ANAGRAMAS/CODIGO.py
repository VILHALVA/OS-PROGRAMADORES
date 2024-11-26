import sys

def read_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        print(f"ERRO: O arquivo '{file_path}' não foi encontrado.")
        sys.exit(1)

def validate_user_input(user_word):
    if not all(char.isalpha() or char == '_' for char in user_word):
        print('ERRO: Palavra inválida: contém caracteres não permitidos!')
        return False
    
    user_word = [char.upper() for char in user_word if char != '_']
    
    if len(user_word) > 16:
        print('ERRO! Palavra inválida: limite de caracteres excedido!')
        return False
    
    return user_word

def remove_invalid_words(user_word, words_list):
    valid_words_list = []
    for word in words_list:
        new_user_word = user_word[:]
        word_chars = list(word)

        for letter in word_chars:
            if letter not in new_user_word:
                break
            new_user_word.remove(letter)
        else:
            valid_words_list.append(word)
    
    return valid_words_list

def remove_word_from_user_input(user_word, word):
    for letter in word:
        if letter in user_word:
            user_word.remove(letter)

def build_anagrams(user_word, words_list, anagram):
    if not user_word:
        print(' '.join(anagram))
        return

    for i in range(len(words_list)):
        word = words_list[i]
        if all(user_word.count(letter) >= word.count(letter) for letter in word):
            new_user_word = user_word[:]
            new_anagram = anagram + [word]
            remove_word_from_user_input(new_user_word, word)
            build_anagrams(new_user_word, words_list[i + 1:], new_anagram)

def solve_anagrams(user_word, words_list):
    words_list = remove_invalid_words(user_word, words_list)
    build_anagrams(user_word, words_list, [])

def main():
    if len(sys.argv) != 3:
        print("Uso: python CODIGO.py <caminho_para_arquivo> <palavra_usuario>")
        sys.exit(1)

    file_path = sys.argv[1]
    user_input = sys.argv[2]

    words_file_content = read_file(file_path)
    valid_words = [word.upper() for word in words_file_content.split('\n') if word]

    user_word = validate_user_input(user_input)
    if user_word:
        solve_anagrams(user_word, valid_words)

if __name__ == "__main__":
    main()
