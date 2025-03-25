from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/appointments')
def get_appointments():
    return jsonify([
        {"id": 1, "title": "Termin 1"},
        {"id": 2, "title": "Termin 2"},
        {"id": 3, "title": "Termin 3"}
    ])

if __name__ == "__main__":
    app.run()