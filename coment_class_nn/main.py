import tensorflow as tf
import pandas as pd
from sklearn.model_selection import train_test_split
from keras.layers import TextVectorization
import numpy as np

data = pd.read_csv('reviews.csv') # 41319 value, max_length = 4542
x = data['content'].astype(str)
y = data['score']
y = np.array((int(float(rating)) if rating > 5 else 5) for rating in y)

data = data.dropna(subset=['score'])   

x = data['content'].astype(str)
y = data['score'].astype(int)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.1, random_state=42)

vectorize_layer = TextVectorization(
    max_tokens=450,
    output_mode='int',
    output_sequence_length=350
)

vectorize_layer.adapt(x)

x_train_vectorized = vectorize_layer(x_train)
x_test_vectorized = vectorize_layer(x_test)

model = tf.keras.models.Sequential()
model.add(tf.keras.layers.Input(shape=(350,)))
model.add(tf.keras.layers.Embedding(input_dim=450, output_dim=64, name="embedding"))
model.add(tf.keras.layers.SimpleRNN(64))
model.add(tf.keras.layers.Dense(6))

model.compile(loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
            optimizer='adam', metrics=['accuracy'])

model.fit(x_train_vectorized, y_train, epochs=2, validation_data=(x_test_vectorized, y_test))
loss, accuracy = model.evaluate(x_test_vectorized, y_test)

data = np.array(vectorize_layer(["GOOD", "it is bad", "cool", "i hate it"]))
data = model.predict(data)
print(data)