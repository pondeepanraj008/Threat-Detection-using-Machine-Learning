import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder
import joblib

# Load dataset
data = pd.read_csv("cybersecurity_attacks.csv")  # Ensure the dataset is in the project folder

# Preview dataset structure
print("Dataset Preview:")
print(data.head())

# Handling missing values (fill or drop)
data = data.dropna()  # Remove rows with missing values

# Selecting Features (Drop non-relevant columns)
X = data.drop(["Attack Type", "Timestamp", "Source IP Address", "Destination IP Address"], axis=1, errors='ignore')

# Convert categorical labels (Attack Type) into numeric values
y = data["Attack Type"].astype('category').cat.codes  # Encode attack types as numbers

# Convert categorical features to numerical using LabelEncoder
label_encoders = {}  # Dictionary to store encoders
for column in X.select_dtypes(include=['object']).columns:  # Find categorical columns
    le = LabelEncoder()
    X[column] = le.fit_transform(X[column])  # Convert text to numbers
    label_encoders[column] = le  # Store encoder for future use

# Split dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the Random Forest model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate model accuracy
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy:.2f}")

# Save the trained model
joblib.dump(model, "threat_detection_model.pkl")
print("Model saved as 'threat_detection_model.pkl'")

# Save label encoders for future decoding (if needed)
joblib.dump(label_encoders, "label_encoders.pkl")
print("Label encoders saved as 'label_encoders.pkl'")

# Save training feature names
joblib.dump(list(X.columns), "training_features.pkl")
print("Feature names saved as 'training_features.pkl'")
