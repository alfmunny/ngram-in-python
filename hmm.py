import nltk
from nltk.corpus import brown

def hmm():
    data_set = brown.words(categories='news')
    symbols = list(set([ss[0] for sss in data_set for ss in sss]))
    states = range(len(symbols))
    train_seq = [[(l, '') for l in w] for w in data_set]
    trainer = nltk.tag.hmm.HiddenMarkovModelTrainer(states=states, symbols=symbols)
    m = trainer.train_unsupervised(train_seq)
    print m
    return

def transition_matrix(list_of_sequences):
    
    return

def main():
    hmm()

if __name__ == '__main__':
    main()
