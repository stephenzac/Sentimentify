import main
from flask import Flask, jsonify, request
from flask_cors import CORS

PORT = 5000


app = Flask(__name__)

CORS(app) 


@app.route("/", methods=["GET"])
def main_page():
    return {}


@app.route("/send-playlist", methods=["POST"])
def send_playlist_link():
    data = request.get_json()
    data = data["link"]

    backend_response = main.run(data)

    # return status code 400 for invalid playlist links
    if backend_response == None:
        return jsonify({"reason": "invalid playlist link"}), 400
    
    return jsonify(backend_response)



if __name__ == "__main__":
    app.run(port=PORT)
