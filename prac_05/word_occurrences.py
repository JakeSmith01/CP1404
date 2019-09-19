words_in_string = {}
string = input('Text:')
words = string.split()

for word in words:
    try:
        words_in_string[word] += 1
    except KeyError:
        words_in_string[word] = 1

words = list(words_in_string.keys())
words.sort()

words_length = max((len(word) for word in words))
for word in words:
    print('{:{}}:{}'.format(word, words_length, words_in_string[word]))
