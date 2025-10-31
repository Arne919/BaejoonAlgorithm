L, C = map(int, input().split())
letters = sorted(input().split())

vowels = {'a', 'e', 'i', 'o', 'u'}

def backtrack(start, path):
    if len(path) == L:
        vowel_cnt = sum(1 for ch in path if ch in vowels)
        consonant_cnt = L - vowel_cnt
        if vowel_cnt >= 1 and consonant_cnt >= 2:
            print(''.join(path))
        return
    
    for i in range(start, C):
        backtrack(i + 1, path + [letters[i]])

backtrack(0, [])
