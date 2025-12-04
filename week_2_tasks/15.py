def words(sentence):
    freq = {}
    for word in sentence.split():
        freq[word] = freq.get(word, 0) + 1

    return freq

sentence = input('enter a sentence: ')
print(words(sentence))