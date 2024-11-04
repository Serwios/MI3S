from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv1D, MaxPooling1D, Flatten, Dense, Dropout

import util.sample_reader as sr

# Model creation
model = Sequential([
    Conv1D(64, kernel_size=5, activation='relu', input_shape=(1000, 1)),
    MaxPooling1D(pool_size=2),
    Dropout(0.25),
    Conv1D(128, kernel_size=5, activation='relu'),
    MaxPooling1D(pool_size=2),
    Dropout(0.25),
    Flatten(),
    Dense(128, activation='relu'),
    Dropout(0.5),
    Dense(3, activation='softmax')
])

# Compilation
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Training
result = sr.read("training_data.txt")

seismograms = result[0]
labels = result[1]

history = model.fit(
    seismograms, labels,
    epochs=20,
    batch_size=3)

# Saving trained model
model.save('saved_model.h5')


