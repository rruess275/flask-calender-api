from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "✅ Flask läuft auf Render!"

@app.route('/appointments', methods=['GET'])
def get_appointments():
    return jsonify([
        {
            "Id": 1,
            "StartDate": "2025-04-01T09:00:00",
            "EndDate": "2025-04-01T10:00:00",
            "Title": "Testtermin",
            "Color": "#00FFAA"
        }
    ])
