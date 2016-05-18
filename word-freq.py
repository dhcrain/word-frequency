
import string

with open("sample.txt") as opened_file:
    book = (opened_file.read()).lower()

for p in string.punctuation:
    book = book.replace(p, "")
    book = book.replace('\n', " ")
#print(book.split(" "))

histogram = {}

for word in book.split(" "):
    if word in histogram.keys():
        histogram[word] += 1
    else:
        histogram[word] = 1

print(histogram)

#for key, value in histogram.items():
#    print(key, value)