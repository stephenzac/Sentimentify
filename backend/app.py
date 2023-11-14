from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)

# Change for production?
CORS(app) 


@app.route("/", methods=["GET"])
def main_page():
    data = {
        "Hello": "World"
    }
    return jsonify(data)


if __name__ == "__main__":
    app.run()
