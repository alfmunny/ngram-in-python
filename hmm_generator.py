import nltk
from nltk.corpus import brown
import numpy as np

def hmm():
    data_set = brown.words(categories='news')
    symbols = list(set([ss[0] for sss in data_set for ss in sss]))
    states = range(len(symbols))
    train_seq = [[(l, '') for l in w] for w in data_set]
    trainer = nltk.tag.hmm.HiddenMarkovModelTrainer(states=states, symbols=symbols)
    m = trainer.train_unsupervised(train_seq)
    print m
    return m

def letters_behind(list_words, letter):
    '''
    Append all letters behind the target letter which be focused on to a list_letters_behind

    params:
    list_words: list : a list of words
    letter: string : the target letter
    '''
    list_letters_behind = []
    for word in list_words:
        for i in range(len(word)):
            if word[i] is letter and i is not len(word)-1:
                list_letters_behind.append(word[i+1])

    return list_letters_behind

def generator_transition_matrix_letter(list_letters, letters):
    '''
    Calculate the transition matrix for just one letter

    params:
    list_letters: list : all letters in list, which are behind the target letter.
        ['a', 'a', 'a', 'c', 'd', 'a', 'd', 'c', 'b']
    letters: list : definition letters to be used.
        ['a', 'b', 'c', 'd']
    '''
    letters_counter = []
    freq_letters = []
    sorted_letters = list(letters)
    sorted_letters.sort()
    for l in sorted_letters:
        freq_letters.append(list_letters.count(l))

    letters_counter = np.array(freq_letters)
    #print letters_counter

    #print letters_counter.sum()
    if letters_counter.sum() != 0:
        freq_letters = [float(x)/letters_counter.sum() for x in letters_counter]
    if letters_counter.sum() == 0:
        freq_letters = [0 for x in letters_counter]
    #print freq_letters
    return sorted_letters, freq_letters

def generator_transition_matrix(list_words, letters):
    '''
    Calculate the full transition matrix for all letters

    params:
    list_words: list : all sequences which is the transition matrix computed for
    letters: list : definition letters to be used

    '''
    sorted_letters = list(letters)
    sorted_letters.sort()
    transition_matrix = []
    for l in sorted_letters:
        list_letters_behind = letters_behind(list_words, l)
        list_letters, freq_letters = generator_transition_matrix_letter(list_letters_behind, letters)
        transition_matrix.append(freq_letters)

    transition_matrix = np.array(transition_matrix)

    return sorted_letters, transition_matrix

def generator_distribution_matrix(confusion_matrix, labels):
    '''
    params:
    confusion_matrix: list : a two-level list
    labels: list : definition of label
    '''
    reuslt = []
    confusion_matrix = np.array(confusion_matrix)
    distribution_matrix = []

    for i in range(len(labels)):
        distribution_matrix.append([])
        if confusion_matrix[i] != 0:
            for j in confusion_matrix[i]:
                distribution_matrix[i].append(float(j)/confusion_matrix[i].sum())

    return labels, distribution_matrix

def main():
    hmm()

if __name__ == '__main__':
    main()
