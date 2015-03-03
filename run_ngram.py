import ngram_generator as ng
import numpy as np
import pickle

""" Realtime test """

""" === Intialization === """
#from nltk.book import text1
f = open('source_text.pkl')
text1 = pickle.load(f)
n_ngram = 2
num_words = 500
min_word_length = 4

punctuations = ng.get_punctuations()
# dict_words = ng.most_common_lowercase(text1,punctuations, num_words, min_word_length)
# dict_words = ["time", "person", "year", "way", "day", "thing", "man", "world", "life", "hand", "part", "child", "eye", "woman", "place",
#     "case", "point", "government", "company", "number", "group", "problem", "fact", "be", "have", "do", "say", "get", "go", "see", "come",
#     "want", "give", "use", "find", "tell", "seem", "feel", "try", "leave", "call", "good", "new", "first", "last", "long", "great", "little",
#     "own", "other", "old", "right", "big", "high", "different", "small", "large", "next", "early", "young", "important", "few", "public", "bad", "same", "able", "of", "in", "for", "with", "by", "from", "up", "about", "into",
#      "over", "after", "beneath", "under", "above", "the", "and", "that", "it", "not", "he", "you", "this", "but", "his", "they",
#      "her", "she", "will", "my", "one", "all", "would", "there", "their", "picgold", "shamet", "jvqxyz", "brownfox", "jumpsover", "lazydog"]
dict_words = ["diamond", "diomond", "constitution", "constitusion", "weather", "wether", "vacuum", "vacume", "calendar", "calender", "jewelry", "jewelery"]
print dict_words
dict_words = [ng.split_strokes(w) for w in dict_words] 

""" === Train === """
model = ng.train(dict_words, n_ngram)
print "There are", len(model), "words available."

""" === Excute the real time test === """
while True:
    print "================================"
    word = raw_input("Press Enter to a missspelled word according to the dictionary...\n")
    #pred = model.find(word)[0:len(word)]
    pred_strokes, pred_word = ng.predict(model, word)
    print "Prediction:", pred_strokes
    #print "From the possible word '" + str(pred_word) + "'"
