from flask import Flask, request, jsonify
from flask_cors import CORS
from matcher import find_solution
import datetime

app = Flask(__name__)
CORS(app)

@app.route("/query", methods=["POST"])
def query_code():
    data = request.json
    user_query = data.get("query", "")

    result = find_solution(user_query)

    with open("logs/queries.log", "a") as log:
        log.write(f"{datetime.datetime.now()} | {user_query} | {bool(result)}\n")

    if result:
        return jsonify(result)
    return jsonify({"message": "No response"}), 404

if __name__ == "__main__":
    app.run(debug=True)
