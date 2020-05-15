text = input('Input some words: ')
words = text.split()
print(words)

index_word = 0 #длина каждого слова

for word in range(len(words)):
    if len(words[index_word]) < len(words[word]):
        index_word = word

print(words[index_word])
