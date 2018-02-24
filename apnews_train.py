import gensim
from dataset_loader import load_all_sentences

if __name__ == "__main__":
	sentences = load_all_sentences("corpus/") 
	print(len(sentences))
