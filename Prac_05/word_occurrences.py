text = input("Text: ")
words = text.split()
words.sort()
word_count = {}
for word in words:
    word_count[word] = word_count.get(word, 0) + 1
for key, value in word_count.items():
    print("{}  {}".format(key,value))
