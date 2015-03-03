import ngram_generator as ng
import numpy as np

""" Test Exsamples """
from nltk.book import text1
n_ngram = 3
num_words = 500
min_word_length = 4
wrong_letters = 1
results = np.array([ng.test_ngram(text1, n_ngram, num_words, min_word_length, wrong_letters)[1] for i in range(50)])
ng.test_ngram(text1, n_ngram, num_words, min_word_length, wrong_letters)

print "======== Average Accuracy ========"
print results.mean()
