from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/appointments', methods=['GET'])
def get_appointments():
    return jsonify([{"Id": 1, "Title": "Testtermin"}])
