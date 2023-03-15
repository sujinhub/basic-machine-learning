# https://wikidocs.net/21698


""" [Word Tokenization] """
from nltk.tokenize import word_tokenize
from nltk.tokenize import WordPunctTokenizer # conda install nltk && pip install konlpy
from tensorflow.keras.preprocessing.text import text_to_word_sequence
from nltk.tokenize import TreebankWordTokenizer

# import nltk
# nltk.download('punkt')

sample_text = "Starting a home-based restaurant may be an ideal. it doesn't have a food chain or restaurant of their own."

print('단어 토큰화1 :', word_tokenize(sample_text))
print('단어 토큰화2 :', WordPunctTokenizer().tokenize(sample_text))
print('단어 토큰화3 :', text_to_word_sequence(sample_text))

""" Penn Treebank Tokenization """
# Rule 1: Hyphenated words should be kept as one word.
# Rule 2: Words that include a clitic with an apostrophe, such as "doesn't", should be separated into their constituent parts.

print('단어 토큰화4 :',TreebankWordTokenizer().tokenize(sample_text))


""" [Sentence Tokenization] """
from nltk.tokenize import sent_tokenize

sample_text1 = "His barber kept his word. But keeping such a huge secret to himself was driving him crazy. Finally, the barber went up a mountain and almost to the edge of a cliff. He dug a hole in the midst of some reeds. He looked about, to make sure no one was near."
print('문장 토큰화1 :',sent_tokenize(sample_text1))
sample_text2 = "I am actively looking for Ph.D. students. and you are a Ph.D student."
print('문장 토큰화2 :',sent_tokenize(sample_text2))