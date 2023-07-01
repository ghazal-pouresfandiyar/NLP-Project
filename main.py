from itertools import tee, islice
import re
from collections import Counter
from random import *

# calculate ngrams
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


def extract_unigrams(file):
    words = re.findall('\w+', open(file).read())
    unigrams = change_unigram_format(dict(Counter(ngrams(words, 1))))
    return unigrams

def print_unigrams(unigrams):
    print("------------------Unigram values------------------")  
    keys = unigrams.keys()
    values = unigrams.values()
    for i in keys:
        print(15*" " + i + " ---> "+str(unigrams[i]))

def extract_bigrams(file):
    words = re.findall('\w+', open(file).read())
    bigrams = dict(Counter(ngrams(words, 2)))
    return bigrams

def print_bigrams(bigrams):
    print("------------------Bigram  values------------------")
    keys = bigrams.keys()
    values = bigrams.values()
    for i in keys:
        print(10*" " ,i , " ---> "+str(bigrams[i]))


# main
# part 1
unigrams = extract_unigrams('a.txt')
bigrams = extract_bigrams('a.txt')
print_unigrams(unigrams)
print_bigrams(bigrams)

length = randint(1,5)


