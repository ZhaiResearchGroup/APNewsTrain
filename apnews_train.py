import gensim
from dataset_loader import load_all_sentences

if __name__ == "__main__":
	sentences = load_all_sentences("corpus/") 

	training_corpus = [gensim.models.doc2vec.TaggedDocument(sen, [i]) for (i, sen) in enumerate(sentences)]
	
	model = gensim.models.doc2vec.Doc2Vec()
	model.build_vocab(training_corpus)
	model.train(training_corpus, total_examples=model.corpus_count, epochs=model.iter)

	model.save("apnews_sen_model.model")