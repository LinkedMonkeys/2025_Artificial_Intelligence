import csv
import tensorflow as tf
import sys
import numpy

from sklearn.model_selection import train_test_split

# Read data in from file
with open("iris.data") as f:
    reader = csv.reader(f)
    # next(reader)

    data = []
    for row in reader:
        if row[4] == 'Iris-setosa':
            label = [0, 0, 1]
        elif row[4] == 'Iris-versicolor':
            label = [0, 1, 0]
        else: # Iris-virginica
            label = [1, 0, 0]
        data.append({
            "evidence": [float(cell) for cell in row[:4]],
            "label": label
        })


# Separate data into training and testing groups
evidence = [row["evidence"] for row in data]
labels = [row["label"] for row in data]
X_training, X_testing, y_training, y_testing = train_test_split(
    evidence, labels, test_size=0.2
)

X_training = numpy.array(X_training)
y_training = numpy.array(y_training)

X_testing = numpy.array(X_testing)
y_testing = numpy.array(y_testing)

# Create a neural network
model = tf.keras.models.Sequential()

# Add a hidden layer with 8 units, with ReLU activation
model.add(tf.keras.layers.Dense(8, input_shape=(4,), activation="relu"))

model.add(tf.keras.layers.Dropout(.5))

# Add output layer with 1 unit, with sigmoid activation
model.add(tf.keras.layers.Dense(3, activation="sigmoid"))

# Train neural network
model.compile(
    optimizer="adam",
    loss="binary_crossentropy",
    metrics=["accuracy"]
)
model.fit(X_training, y_training, epochs=500)

# Evaluate how well model performs
model.evaluate(X_testing, y_testing, verbose=2)
