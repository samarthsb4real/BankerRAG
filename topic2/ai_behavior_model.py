import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM
import numpy as np
import pandas as pd

import time

user_behavior = []

def log_keystroke(key):
    timestamp = time.time()
    user_behavior.append({'key': key, 'time': timestamp})

# Example: Call `log_keystroke('A')` when a user presses 'A'


# Load dataset
data = pd.read_csv("behavior_data.csv").values
X_train, y_train = data[:, :-1], data[:, -1]

# Define Model
model = Sequential([
    LSTM(32, return_sequences=True, input_shape=(10, 3)),  
    LSTM(16),
    Dense(1, activation='sigmoid')  
])

# Train
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
model.fit(X_train, y_train, epochs=10, batch_size=32)

# Save Model
model.save("ai_behavior_model.h5")