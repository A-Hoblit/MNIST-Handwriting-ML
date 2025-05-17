from tensorflow import keras
from keras.datasets import mnist
from keras.utils import to_categorical
from keras.models import Sequential
from keras.layers import Dense, Input

# Data
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

img_train = train_images / 255
img_test = test_images / 255

ibl_train = to_categorical(train_labels, 10)
ibl_test = to_categorical(test_labels, 10)

num_samples_train, img_rows, img_cols = img_train.shape
img_train = img_train.reshape(num_samples_train, img_rows * img_cols)

#Model
model = Sequential([
    Input(shape=(img_rows * img_cols,)),
    Dense(128, activation='relu'),
    Dense(10, activation='softmax')
])
model.compile(optimizer='adam',
             loss='categorical_crossentropy')
model.fit(img_train, ibl_train, epochs=8, batch_size=32)

#Results
num_samples_test, _, _ = img_test.shape
img_test = img_test.reshape(num_samples_test, img_rows * img_cols)

evaluation = model.evaluate(img_test, ibl_test)
print(evaluation)

#Example predictions
predictions = model.predict(img_test[:20,:])
predictions_idx = predictions.argmax(1)
print(predictions_idx)
print(test_labels[:20])