import string

with open("sample.txt") as opened_file:
    book = (opened_file.read()).lower()

for p in string.punctuation:
    book = book.replace(p, " ")
    book = book.replace('\n', " ")
    book = book.replace("  ", " ")
#print(book.split(" "))

histogram = {}

for word in book.split(" "):
    if word in histogram.keys():
        histogram[word] += 1
    else:
        histogram[word] = 1

#print(histogram)
#hist_list = []
#for key, value in histogram.items():
#    temp = (key, value)
#    hist_list.append(temp)
#    print(hist_list[:-20:-1])

import operator
sorted_hist = sorted(histogram.items(), key=operator.itemgetter(1))
sorted_hist = sorted_hist[:-20:-1]

for item in sorted_hist:
    print(key, )


