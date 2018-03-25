import os
import ngram
import pickle

build = True
rawPath = '/Users/trinley/github/bo-pos/models/ngram/entries.txt'
ngramPath = "/Users/trinley/github/bo-pos/models/ngram/ngram.pickled"

if build or not os.path.isfile("ngram.pickled"):
    with open(rawPath, mode='r', encoding='utf-8') as f:
        G = ngram.NGram(f.read().splitlines(), N=2)
    pickle.dump(G, open(ngramPath, "wb"), -1)

N = pickle.load(open(ngramPath, "rb"))


print(N.search('བཀྲ་ས་', threshold=0.54))

