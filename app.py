from flask import Flask, request, jsonify, send_from_directory
import sqlite3

app = Flask(__name__, static_folder='static')

# DB init
def init_db():
    with sqlite3.connect("reviews.db") as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS reviews (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                course TEXT,
                professor TEXT,
                rating INTEGER,
                comment TEXT
            );
        """)

@app.route("/")
def index():
    return send_from_directory("static", "index.html")

@app.route("/add_review", methods=["POST"])
def add_review():
    data = request.json
    with sqlite3.connect("reviews.db") as conn:
        conn.execute("INSERT INTO reviews (course, professor, rating, comment) VALUES (?, ?, ?, ?)",
                     (data["course"], data["professor"], data["rating"], data["comment"]))
    return jsonify({"message": "Review added!"})

@app.route("/search", methods=["GET"])
def search_reviews():
    query = request.args.get("query", "")
    with sqlite3.connect("reviews.db") as conn:
        cursor = conn.execute("SELECT course, professor, rating, comment FROM reviews WHERE course LIKE ? OR professor LIKE ?",
                              (f"%{query}%", f"%{query}%"))
        results = cursor.fetchall()
    return jsonify([{"course": r[0], "professor": r[1], "rating": r[2], "comment": r[3]} for r in results])

if __name__ == "__main__":
    init_db()
    app.run(debug=True)

import os

if __name__ == "__main__":
    init_db()
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)

