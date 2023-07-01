from itertools import tee, islice
import re
from collections import Counter
import random

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
    words = re.findall('\w+|<s>|</s>', open(file).read().lower())
    unigrams = change_unigram_format(dict(Counter(ngrams(words, 1))))
    return unigrams

def print_unigrams(unigrams):
    print("------------------Unigram values------------------")  
    keys = unigrams.keys()
    values = unigrams.values()
    for i in keys:
        print(15*" " + i + " ---> "+str(unigrams[i]))

def extract_bigrams(file):
    words = re.findall('\w+|<s>|</s>', open(file).read().lower())
    bigrams = dict(Counter(ngrams(words, 2)))
    del bigrams[("</s>", "<s>")]
    return bigrams

def print_bigrams(bigrams):
    print("------------------Bigram  values------------------")
    keys = bigrams.keys()
    values = bigrams.values()
    for i in keys:
        print(10*" " ,i , " ---> "+str(bigrams[i]))
        
# probability of hapenning "b a" in sentence
def p(a, b, unigrams, bigrams):
    # add 1 to numerator for smoothing
    # add |v| to denominator for smoothing
    # numerator = cba(b,a,bigrams)+1
    # denominator = cb(b,unigrams)+len(unigrams.keys())
    numerator = cba(b,a,bigrams)
    denominator = cb(b,unigrams)
    return numerator/denominator

# count "b a" in corpus
def cba(b, a, bigrams):
    t = (b, a)
    result = 0
    try:
        result = bigrams[t]
    except:
        result = 0
    return result

# count b in corpus
def cb(b, unigrams):
    return unigrams[b]

def random_sentence(n, unigrams):
    length = random.randint(1,n)
    test = []
    test.append("<s>")
    for i in range(length):
        rand_word = "<s>"
        while(rand_word == "<s>" or rand_word == "</s>"):
            rand_word = random.choice(list(unigrams.keys()))
        test.append(rand_word)
    test.append("</s>")
    print("The test sentences is :", end=" ")
    for i in test:
        print(i, end = " ")
    print()
    return test

def calculate_p(test, unigrams, bigrams):
    total = 1
    for i in range(len(test)-1):
        temp_p = p(test[i], test[i+1], unigrams, bigrams)
        total = total * temp_p
        print("p("+test[i+1]+"|"+test[i]+") = ", temp_p)
    print("total =",total)

# main
file = "corpus.txt"

unigrams = extract_unigrams(file)
bigrams = extract_bigrams(file)

# part 1
print_unigrams(unigrams)
print_bigrams(bigrams)

# part2
test = random_sentence(5, unigrams)
calculate_p(test, unigrams, bigrams)




