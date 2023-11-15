from flask import Flask, jsonify, request
from flask_cors import CORS
import main

app = Flask(__name__)

# Change for production?
CORS(app) 


@app.route("/", methods=["GET"])
def main_page():
    return {}


@app.route("/send-playlist", methods=["POST"])
def send_playlist_link():
    data = request.get_json()
    data = data["link"]

    backend_response = main.run(data)
    return backend_response.json()



if __name__ == "__main__":
    app.run()
