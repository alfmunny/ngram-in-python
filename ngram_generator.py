__author__ = 'Yuanchen ZHANG'

import ngram
import numpy as np
import random
import sys

'''

'''

def get_punctuations():
    punctuations = ['.', ',', '-', '"', '!', '--', ';', '."', '!"', '?"', "'", '?', ',"']
    return punctuations

def get_splitted_letters():
    strokes = {'i': 'i1i2', 't': 't1t2', 'x': 'x1x2', 'f': 'f1f2', 'z': 'z1z2', 'j': 'j1j2'}
    return strokes

def get_splitted_strokes():
    strokes = ['i1', 'i2', 'f1', 'f2', 'z1', 'z2', 'x1', 'x2', 'j1', 'j2']
    return strokes

def get_characters():
    characters = 'qwertyuioplkjhgfdsazxcvbnm'
    return characters

def stroke_counter(word):
    strokes = get_splitted_strokes()
    len_word = len(word)
    for s in strokes:
        len_word = len_word - word.count(s)
    return len_word

def splitted_stroke_counter(word):
    strokes = get_splitted_strokes()
    len_word = len(word)
    for s in strokes:
        len_word = len_word - word.count(s)
    return len_word

def misspeller(word):
    characters = get_characters()
    #rand_word_position = random.randint(-1,len(word))
    #rand_characters_position = random.randint(0,len(characters)-1)
    rand_word_position = random.randint(0,len(word)-1)
    rand_characters_position = random.randint(0,len(characters)-1)
   # if rand_word_position == -1:
   #     misspelled_word = characters[rand_characters_position] + word
   # elif rand_word_position == len(word):
   #     misspelled_word = word + characters[rand_characters_position]
   # else:
    if True:
        misspelled_word = list(word)
        misspelled_word[rand_word_position] = characters[rand_characters_position]
        misspelled_word = ''.join(misspelled_word)
    return misspelled_word

def most_common(text, punctuations, num_words, word_length):
    vocab = text.vocab()
    most_common_words = [w[0] for w in vocab.items()[0:num_words] if w[0] not in punctuations and len(w[0])>word_length]
    return most_common_words

def most_common_lowercase(text, punctuations, num_words, word_length):
    vocab = text.vocab()
    most_common_words = list(set([w[0].lower() for w in vocab.items()[0:num_words] if w[0] not in punctuations and len(w[0])>word_length]))
    return most_common_words

def split_strokes(word):
    strokes = get_splitted_letters()
    for s in strokes:
        word = word.replace(s, strokes[s])
    return word

def missspelled_words_generator(words_list, num):
    m_words_list = list(words_list)
    for i in range(num):
        for index in range(len(m_words_list)):
            w = m_words_list[index]
            m_words_list[index] = misspeller(w)
    return m_words_list

def test_ngram(text, n_ngram, num_words, word_length, n_wrong_letter):
    #dict_words = ['the', 'of', 'and', 'a', 'to', 'in', 'that', 'his', 'it', 'I', 'is', 'he', 'with', 'was', 'as', 'all', 'for', 'this', 'at', 'by', 'but', 'not', 'him', 'from', 'be', 'on', 'so', 'whale', 'one', 'you', 'had', 'have', 'there', 'But', 'or', 'were', 'now', 'which', 'me', 'like', 'The', 'their', 'are', 'they', 'an', 'some', 'then', 'my', 'when', 'upon', 'out', 'into', 'man', 'ship', 'up', 'Ahab', 'more', 'no', 'them', 'ye', 'what', 'old', 'sea', 'if', 'would', 'been', 'we', 'other', 'over', 'these', 'will', 'its', 'And', 'down', 'only', 'such', 'head', 'though', 'boat', 'her', 'time', 'any', 'who', 'long', 'very', 'It', 'than', 'about', 'said', 'yet', 'still', 'those', 'before', 'great', 'has', 'two', 'seemed', 'must', 'last']
    punctuations = get_punctuations()

    dict_words = most_common_lowercase(text, punctuations, num_words, word_length)
    print len(dict_words)
    G = ngram.NGram(dict_words, N=n_ngram)
    #misspelled_words = [misspeller(w) for w in dict_words]
    misspelled_words = missspelled_words_generator(dict_words, n_wrong_letter)
    #print misspelled_words
    word_pairs = [(dict_words[index], misspelled_words[index]) for index in range(len(dict_words))]

    result_pairs = []
    miss_words = []
    counter = 0

    for word in word_pairs:
        pred = G.find(word[1])
        result_pairs.append((word[0], pred))
        if word[0] != pred:
            miss_words.append([word[0], word[1], pred])
        if word[0] == pred:
            counter += 1
    accuracy = float(counter)/len(word_pairs)
    #print "======= Result Pairs ========="
    #print result_pairs
#    print "======= Missed Words ========="
#    print miss_words
    print "======= Accuracy ========="
    print accuracy
    return result_pairs, accuracy

def word_calibrator(word, num_strokes):
    splitted_letters = get_splitted_letters()
    letters = list(word)
    letters.reverse()
    new_letters = []
    while len(letters) != 0:
        if letters[-1] not in splitted_letters:
            new_letters.append(letters.pop())
        else:
            tmp = letters.pop()
            tmp = tmp + letters.pop()
            new_letters.append(tmp)
    return new_letters[0:num_strokes]

def train(words, n_ngram):
    n_model = ngram.NGram(words, N=n_ngram)
    # print "======= The Ngram model was trained========="
    # print "Ngram with", len(words), "words with n =", n_ngram
    return n_model

def predict(model, word):
    num_strokes = stroke_counter(word)
    pred_word = model.find(word)

    pred_strokes = []
    # strokes_list = word_calibrator(pred_word, num_strokes)
    # pred_strokes = strokes_list
    return pred_strokes, pred_word
