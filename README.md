# Threat-Detection-using-Machine-Learning
A real-time cybersecurity threat detection system using machine learning. Detects suspicious network activity and keylogger processes via a Flask API.

🔍 Features

- Detects keylogger processes running on the system.
- Scans active network ports (e.g., port 4444 used by Metasploit).
- Trained machine learning model using real cybersecurity attack datasets.
- Exposes a simple Flask API to trigger threat detection via `/detect` endpoint.

📊 Technologies Used

| Layer             | Technology                            |
|-------------------|----------------------------------------|
| **Language**      | Python                                 |
| **ML Model**      | Random Forest (via scikit-learn)       |
| **Web Framework** | Flask                                  |
| **Data Handling** | pandas, LabelEncoder                   |
| **System Access** | psutil, subprocess, re (regex)         |
| **Model I/O**     | joblib                                 |
| **Dataset**       | `cybersecurity_attacks.csv`            |

🧠 How it Works

1. **Training Phase** (`train_model.py`):
   - Loads the dataset
   - Cleans and encodes data
   - Trains a Random Forest model
   - Saves the trained model, encoders, and features

2. **Detection Phase** (`detection_system.py`):
   - Checks system processes and ports
   - Flags suspicious activity based on fixed rules

3. **API Layer** (`app.py`):
   - Simple Flask server exposing `/detect`
   - Combines both rule-based and ML-based threat checks

🚀 Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Run the Flask app:

bash
Copy
Edit
python app.py
Access in browser:

http://localhost:5000/ → Welcome message

http://localhost:5000/detect → Runs detection system

🗃️ Project Structure
bash
Copy
Edit
.
├── app.py                         # Flask server
├── detection_system.py           # System scanning logic
├── train_model.py                # ML model training
├── threat_detection_model.pkl    # Trained ML model
├── label_encoders.pkl            # Encoded label references
├── training_features.pkl         # Features used in training
├── cybersecurity_attacks.csv     # Dataset
├── /lib                          # Support libraries (if any)
└── /scripts                      # Additional utilities/scripts

📌 Notes
Make sure to run this with appropriate system privileges to access process and network data.

This is an educational project — for real-world deployment, consider adding better security handling, logging, and deployment strategy.
