# import numpy as np
# import tensorflow as tf
# from tensorflow.keras.preprocessing.text import Tokenizer
# from tensorflow.keras.preprocessing.sequence import pad_sequences
# from tensorflow.keras.models import Sequential
# from tensorflow.keras.layers import Dense,Embedding,SimpleRNN,Dense
#
#
# class SimpleRNNModel:
#     def __init__(self):
#         self.sentences = []
#         self.labels = []
#         self.tokenizer = Tokenizer()
#         self.padded_sequences = None
#         self.model = None
#
#     def load_data(self):
#         self.sentences=[
#           "movie was good",
#           "movie was bad",
#           "i like this film",
#           "i hate this film",
#           "this movie is amazing",
#           "this movie is terrible",
#           "film was nice",
#           "film was boring",
#           "good acting",
#           "bad acting"
#         ]
#         self.labels = np.array([1,0,1,0,1,0,1,0,1,0])
#
#     def preprocess_data(self):
#         self.tokenizer.fit_on_texts(self.sentences)
#
#         sequences = self.tokenizer.texts_to_sequences(self.sentences)
#
#         self.padded_sequences = pad_sequences(sequences, padding="post")
#
#         print("Word Index:")
#         print(self.tokenizer.word_index)
#
#         print("Sequences:")
#         print(sequences)
#
#         print("Padded sequences:")
#         print(self.padded_sequences)
#
#     def build_model(self):
#         vocab_size = len(self.tokenizer.word_index) + 1
#         self.model = Sequential([
#             Embedding(input_dim=vocab_size, output_dim=8, input_shape=(10,)),
#             SimpleRNN(16),
#             Dense(1,activation="sigmoid")
#         ])
#         self.model.compile(
#             optimizer="adam",
#             loss="binary_crossentropy",
#             metrics=["accuracy"]
#         )
#         self.model.summary()
#
#     def train_model(self):
#         self.model.fit(
#             self.padded_sequences,
#             self.labels,
#             epochs=20
#             )
#
#     def predict(self):
#         test=["Movie Was Amazing"]
#
#         seq = self.tokenizer.texts_to_sequences(test)
#
#         padded = pad_sequences(seq,maxlen=self.padded_sequences.shape[1],padding="post")
#
#         prediction = self.model.predict(padded)
#
#         print("Prediction:",prediction)
#
#
# rnn = SimpleRNNModel()
# rnn.load_data()
# rnn.preprocess_data()
# rnn.build_model()
# rnn.train_model()
# rnn.predict()