#Samiha Ashraf
#1884227

from collections import Counter

words = input().split()

word_freq = Counter(words)

for word in words:
    print(word, word_freq[word])
