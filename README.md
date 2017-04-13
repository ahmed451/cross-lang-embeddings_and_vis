# cross-lang-embeddings_and_vis


## Build data
Paste your parallel collection and reshuffle the data for each sentence. 
paste ../data/corpus.ar ../data/corpus.en | python shuffle_sentences.py > ../data/all_ar-en.mix.txt

### Train embeddings using Word2Vec
Build your embeddings and write them to a text file -binary flag set to 0

word2vec -train ../data/all_ar-en.mix.txt -output ../data/cross_Ar-En_vectors.txt -cbow 1 -size 200 -window 5 -negative 0 -hs 1 -sample 1e-3 -threads 12 -binary 0

### Plot the embeddings


python plot_embs.py ../data/cross_Ar-En_vectors.txt.head1k


