import numpy as np
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# Example dataset (keystroke time, mouse_x, mouse_y, label)
X = np.array([
    [0.12, 450, 320], [0.15, 460, 330], [0.10, 440, 310],  # Genuine
    [0.02, 30, 20], [0.03, 40, 25], [0.05, 35, 30]  # Fraudulent
])
y = np.array([1, 1, 1, 0, 0, 0])  # 1 = Verified, 0 = Fraudulent

# Train the model
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Save the model
joblib.dump(model, "behavior_model.pkl")