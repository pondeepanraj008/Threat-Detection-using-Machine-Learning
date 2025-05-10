from flask import Flask, jsonify
from detection_system import check_network_activity, check_process_activity  # Import functions directly

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Threat Detection API! Use /detect to check for threats."

@app.route('/detect', methods=['GET'])
def detect():
    threats = []
    if check_network_activity():  # No need for detection_system.check_network_activity()
        threats.append("Suspicious network activity detected.")
    if check_process_activity():
        threats.append("Keylogger process detected.")

    if threats:
        return jsonify({"status": "Threat detected", "details": threats})
    else:
        return jsonify({"status": "System secure"})
if __name__ == "__main__":
    app.run(debug=True)
