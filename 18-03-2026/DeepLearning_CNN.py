# import tensorflow as tf
# from tensorflow.keras import layers, models
#
#
# class cnn:
#     def __init__(self):
#         self.model = None
#         self.x_train = None
#         self.x_test = None
#         self.y_train = None
#         self.y_test = None
#
#     def load_data(self):
#         (self.x_train, self.y_train), (self.x_test, self.y_test) = tf.keras.datasets.mnist.load_data()
#
#         # Normaalize pixel values (0-255 -> 0-1)
#         self.x_train = self.x_train / 255.0
#         self.x_test = self.x_test / 255.0
#
#         # Add channel dimension for CNN
#         self.x_train = self.x_train.reshape(-1, 28, 28, 1)
#         self.x_test = self.x_test.reshape(-1, 28, 28, 1)
#
#         print("Train Shape:", self.x_train.shape)
#         print("Test Shape:", self.x_test.shape)
#
#     # Build CNN Model
#     def build_model(self):
#         self.model = models.Sequential([
#             layers.Conv2D(32, (3, 3), activation="relu", input_shape=(28, 28, 1)),
#             layers.MaxPooling2D((2, 2)),
#
#             layers.Conv2D(64, (3, 3), activation="relu"),
#             layers.MaxPooling2D((2, 2)),
#
#             layers.Flatten(),
#
#             layers.Dense(64, activation="relu"),
#
#             layers.Dense(10, activation="softmax")
#         ])
#
#         self.model.compile(
#             optimizer="adam",
#             loss="sparse_categorical_crossentropy",
#             metrics=["accuracy"]
#         )
#         self.model.summary()
#
#     # Train Model
#     def train_model(self):
#         self.model.fit(
#             self.x_train,
#             self.y_train,
#             epochs=5,
#             validation_data=(self.x_test, self.y_test)
#         )
#
#     # Evaluate Model
#     def evaluate_model(self):
#         loss, accuracy = self.model.evaluate(self.x_test, self.y_test)
#         print("Test Accuracy:", accuracy)
#
#
# cnn = cnn()
# cnn.load_data()
# cnn.build_model()
# cnn.train_model()
# cnn.evaluate_model()
