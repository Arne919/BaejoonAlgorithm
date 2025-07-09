word = input()

croatian = ['dz=', 'c=', 'c-', 'd-', 'lj', 'nj', 's=', 'z=']

for char in croatian:
    word = word.replace(char, '*')

print(len(word))
