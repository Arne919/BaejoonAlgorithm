def generate_sequence(N, M, sequence):
    if len(sequence) == M:
        print(' '.join(map(str, sequence)))
        return
    for i in range(1, N + 1):
        sequence.append(i)
        generate_sequence(N, M, sequence)
        sequence.pop()

N, M = map(int, input().split())
generate_sequence(N, M, [])
