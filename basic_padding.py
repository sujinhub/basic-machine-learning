# https://wikidocs.net/83544

import numpy as np
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences


preprocessed_sentences = [['barber', 'person'], ['barber', 'good', 'person'], ['barber', 'huge', 'person'], ['knew', 'secret'], ['secret', 'kept', 'huge', 'secret'], ['huge', 'secret'], ['barber', 'kept', 'word'], ['barber', 'kept', 'word'], ['barber', 'kept', 'secret'], ['keeping', 'keeping', 'huge', 'secret', 'driving', 'barber', 'crazy'], ['barber', 'went', 'huge', 'mountain']]

""" Padding with numpy """

tokenizer = Tokenizer()
tokenizer.fit_on_texts(preprocessed_sentences)
encoded = tokenizer.texts_to_sequences(preprocessed_sentences)
# print(encoded)

max_len = max(len(item) for item in encoded)
# print(max_len)

for sentence in encoded:
   while len(sentence) < max_len:
      sentence.append(0)

padded_np = np.array(encoded)
# print(padded_np)


""" Padding with keras """

padded = pad_sequences(encoded, padding='post', maxlen=5)
# print(padded)

padded = pad_sequences(encoded, padding='post', truncating='post', maxlen=5)
# print(padded)


""" Padding with another number """

last_value = len(tokenizer.word_index) + 1
# print(last_value)

padded = pad_sequences(encoded, padding='post', value=last_value)
print(pad_sequences(encoded, padding='post', value=last_value, maxlen=10))
