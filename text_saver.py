from nltk.book import text1 
import pickle

f = open('source_text.pkl', 'wb')
pickle.dump(text1, f)
