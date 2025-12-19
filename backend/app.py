from flask import Flask, request, jsonify
from flask_cors import CORS
from matcher import find_solution
import datetime
from auth import verify_google_token
from database import setup_database, save_user

setup_database()

app = Flask(__name__)
CORS(app)

@app.route("/query", methods=["POST"])
def query_code():
    data = request.json
    user_query = data.get("query", "").strip()

    result = find_solution(user_query)

    with open("logs/queries.log", "a") as log:
        log.write(f"{datetime.datetime.now()} | {user_query} | {bool(result)}\n")

    if result:
        return jsonify(result)
    return jsonify({"message": "No response"}), 404


@app.route("/auth/login", methods=["POST"])
def google_login():
    data = request.json
    token = data.get("token")

    user = verify_google_token(token)

    if not user:
        return jsonify({"error": "Invalid token"}), 401

    save_user(user)

    return jsonify({
        "message": "Login successful",
        "user": user
    })


if __name__ == "__main__":
    app.run(debug=True)
