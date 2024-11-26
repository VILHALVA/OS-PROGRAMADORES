def knight_tour(start_position):
    visits = [[0 for _ in range(8)] for _ in range(8)]
    start = [8 - ord(start_position[0]) + 97, int(start_position[1]) - 1]
    visits[start[0]][start[1]] = 1
    print(start_position)

    for move in range(2, 65):
        start, visits = next_move(start, visits, move)

def next_move(current_position, visits, move):
    board = [(x, y) for x in range(1, 9) for y in range(1, 9)]
    moves_offset = [(2, 1), (2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2), (-2, 1), (-2, -1)]
    possible_moves = []

    for m in range(8):
        candidate = (current_position[0] + moves_offset[m][0], current_position[1] + moves_offset[m][1])
        if candidate in board and visits[candidate[0]-1][candidate[1]-1] == 0:
            possible_moves.append(candidate)

    num_moves = [0] * len(possible_moves)

    for a in range(len(possible_moves)):
        for m in range(8):
            next_candidate = (possible_moves[a][0] + moves_offset[m][0], possible_moves[a][1] + moves_offset[m][1])
            if next_candidate in board and visits[next_candidate[0]-1][next_candidate[1]-1] == 0:
                num_moves[a] += 1

    i = num_moves.index(min(num_moves))
    new_position = possible_moves[i]
    print(chr(105 - new_position[0]) + str(new_position[1]))
    visits[new_position[0]-1][new_position[1]-1] = move

knight_tour('a1')
