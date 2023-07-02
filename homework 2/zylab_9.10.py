#Samiha Ashraf
#1884227

import csv

input_file = input()

with open(input_file, 'r') as csvfile:
    words = csvfile.readline().split(',')

words_counts = {}
for word in words:
    word = word.strip()
    if word in words_counts:
        words_counts[word] += 1
    else:
        words_counts[word] = 1

for word, count in words_counts.items():
    print(word, count)