import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

# Load Data
try:
    keystroke_df = pd.read_csv("keystroke_data.csv")
except Exception as e:
    print(f"Error loading keystroke_data.csv: {e}")
    keystroke_df = pd.DataFrame(columns=['key', 'time_diff'])
    
try:
    mouse_df = pd.read_csv("mouse_data.csv")
except Exception as e:
    print(f"Error loading mouse_data.csv: {e}")
    mouse_df = pd.DataFrame(columns=['x', 'y', 'timestamp'])

# Feature Selection
# For keystroke, use 'time_diff'. For mouse, use 'x' and 'y'.
keystroke_features = keystroke_df[['time_diff']].values if not keystroke_df.empty else np.empty((0, 1))
mouse_features = mouse_df[['x', 'y']].values if not mouse_df.empty else np.empty((0, 2))

# Determine the number of samples: use the maximum count from the two sources or a default of 10 if both are empty
n_keystroke = keystroke_features.shape[0]
n_mouse = mouse_features.shape[0]
n_samples = max(n_keystroke, n_mouse, 10)

# Pad or truncate keystroke_features to have n_samples rows, with 1 column.
if n_keystroke < n_samples:
    pad = np.zeros((n_samples - n_keystroke, 1))
    keystroke_features = np.vstack([keystroke_features, pad])
else:
    keystroke_features = keystroke_features[:n_samples]

# Pad or truncate mouse_features to have n_samples rows, with 2 columns.
if n_mouse < n_samples:
    pad = np.zeros((n_samples - n_mouse, 2))
    mouse_features = np.vstack([mouse_features, pad])
else:
    mouse_features = mouse_features[:n_samples]

# Combine Features horizontally (Resulting shape will be [n_samples, 3])
X = np.hstack((keystroke_features, mouse_features))

# Generate Labels (1 = Legit User, 0 = Anomalous Behavior)
y = np.ones((X.shape[0],))  # Assume all collected data is normal user behavior

# Reshape X for LSTM: each sample will have 3 timesteps with 1 feature each (shape: [n_samples, 3, 1])
X = X.reshape((X.shape[0], X.shape[1], 1))

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Define LSTM Model
model = Sequential([
    LSTM(32, return_sequences=True, input_shape=(X_train.shape[1], 1)),
    LSTM(16),
    Dense(1, activation='sigmoid')
])

# Compile Model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# Train Model
model.fit(X_train, y_train, epochs=10, batch_size=32, validation_data=(X_test, y_test))

# Save Model
model.save("ai_behavior_model.keras")

print("Model training complete. Saved as 'ai_behavior_model.h5'.")