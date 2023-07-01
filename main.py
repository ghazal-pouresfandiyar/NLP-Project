from itertools import tee, islice
import re
from collections import Counter
import json
import numpy

# extract ngrams from a text
def ngrams(lst, n):
  tlst = lst
  while True:
    a, b = tee(tlst)
    l = tuple(islice(a, n))
    if len(l) == n:
      yield l
      next(b)
      tlst = b
    else:
      break

# change (tuple as key ---> value) to (srt as key ---> value) for unigram
def change_unigram_format(unigrams):
    keys = unigrams.keys()
    values = unigrams.values()
    new_keys = []
    new_values = []
    for i in keys:
        new_keys.append(i[0])
    for i in values:
        new_values.append(i)

    new_unigrams = dict(zip(new_keys, new_values))
    return new_unigrams

# main oart of the code
words = re.findall('\w+', open('a.txt').read())

print("------------------Unigram values------------------")
unigrams = change_unigram_format(dict(Counter(ngrams(words, 1))))
keys = unigrams.keys()
values = unigrams.values()
for i in keys:
    print(15*" " + i + " ---> "+str(unigrams[i]))

print("------------------Bigram  values------------------")
bigrams = dict(Counter(ngrams(words, 2)))
keys = bigrams.keys()
values = bigrams.values()
for i in keys:
    print(10*" " ,i , " ---> "+str(bigrams[i]))