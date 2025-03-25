import os
import psycopg2
from flask import Flask, jsonify, request
from dotenv import load_dotenv

load_dotenv()  # Lädt .env (nur lokal; Render nutzt seine eigenen Vars)

app = Flask(__name__)

def get_db_connection():
    return psycopg2.connect(
        host=os.getenv("DB_HOST"),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        port=os.getenv("DB_PORT")
    )

@app.route('/')
def home():
    return "✅ Flask + PostgreSQL sind verbunden!"

@app.route('/appointments', methods=['GET'])
def get_appointments():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, start_date, end_date, title, color FROM appointments ORDER BY start_date;")
    rows = cur.fetchall()
    cur.close()
    conn.close()

    appointments = []
    for row in rows:
        appointments.append({
            "Id": row[0],
            "StartDate": row[1].isoformat(),
            "EndDate": row[2].isoformat(),
            "Title": row[3],
            "Color": row[4]
        })

    return jsonify(appointments)

@app.route('/appointments', methods=['POST'])
def create_appointment():
    data = request.get_json()

    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO appointments (start_date, end_date, title, color) VALUES (%s, %s, %s, %s) RETURNING id;",
        (data['StartDate'], data['EndDate'], data['Title'], data['Color'])
    )
    new_id = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()

    return jsonify({"message": "Termin gespeichert", "Id": new_id}), 201
