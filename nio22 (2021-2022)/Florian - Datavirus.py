key = input()
l = input()
word = input()

print(''.join([key[key.index(letter)-1] for letter in word]))