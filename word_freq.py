import operator
import string

with open("sample.txt") as opened_file:
    book = (opened_file.read()).lower()

for p in string.punctuation:
    book = book.replace(p, "").replace('\n', " ").replace("  ", " ")

histogram = {}

for word in book.split(" "):
    if word in histogram.keys():
        histogram[word] += 1
    else:
        histogram[word] = 1

sorted_hist = sorted(histogram.items(), key=operator.itemgetter(1))

for idx, item in enumerate(sorted_hist[:-21:-1]):
    word, count = item
    print('{:<2}:  {:<4}  {:>1}'.format(idx + 1, word, count))
