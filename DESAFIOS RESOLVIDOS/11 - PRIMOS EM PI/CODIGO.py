import sys
import math
import os
import concurrent.futures
import itertools

def generate_primes(n):
    flags = [True] * n
    flags[0] = False
    flags[1] = False

    for i in range(2, math.isqrt(n) + 1):
        if flags[i]:
            for j in range(i * i, n, i):
                flags[j] = False

    return flags

def find_sequences(start_pos, word, position, sequence, data, max_len_sequence, prime_flags):
    result = []

    new_word = word + [data[position]]

    if position >= len(data) or len(new_word) > 4:
        if len(sequence) >= max_len_sequence:
            result.append((sequence, start_pos))
        return result

    r = find_sequences(start_pos, new_word, position + 1, sequence, data, max_len_sequence, prime_flags)
    result.extend(r)

    if prime_flags[palindrome_to_int(new_word)]:
        r = find_sequences(start_pos, [], position + 1, sequence + ''.join(map(str, new_word)), data, max_len_sequence, prime_flags)
        result.extend(r)

    return result

def palindrome_to_int(word):
    num = 0
    for ch in word:
        ch -= ord('0')
        num = num * 10 + int(ch)
    return num

def start_workers(workers, batch_size, data):
    sequences = []
    batch_results = []

    max_len_sequence = 1
    prime_flags = generate_primes(10000)
    jobs = []

    for a in range(2, len(data)):
        if a + batch_size >= len(data):
            batch_size = len(data) - a

        for b in range(batch_size):
            job = {
                'start_pos': a + b,
                'word': [],
                'position': a + b,
                'sequence': '',
                'data': data,
                'max_len_sequence': max_len_sequence,
                'prime_flags': prime_flags
            }
            jobs.append(job)

        with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as executor:
            results = list(executor.map(find_sequences_wrapper, jobs))

        batch_results = list(itertools.chain.from_iterable(results))

        for seq, pos in batch_results:
            seq_len = len(seq)
            if seq_len > max_len_sequence:
                max_len_sequence = seq_len
                sequences = [(seq, pos)]
            elif seq_len == max_len_sequence:
                sequences.append((seq, pos))

    return sequences

def find_sequences_wrapper(job):
    return find_sequences(**job)

def main():
    if len(sys.argv) != 2:
        print("Uso: python CODIGO.py <arquivo>")
        sys.exit(1)

    batch_size = 1000
    data = []

    try:
        with open(sys.argv[1], "rb") as file:
            data = list(file.read())

    except IOError:
        print("Erro! Não foi possível ler o arquivo!")
        sys.exit(1)

    len_data = len(data)
    extras = [0, 0, 0, 0]
    data.extend(extras)

    sequences = start_workers(os.cpu_count(), batch_size, data)

    min_position = len_data
    min_sequence = ""

    for seq, pos in sequences:
        if pos < min_position:
            min_position = pos
            min_sequence = seq

    print(min_sequence)

if __name__ == "__main__":
    main()
