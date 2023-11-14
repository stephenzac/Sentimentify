from flask import Flask

app = Flask(__name__)


@app.route("/")
def main_page():
    data = {
        "Hello": "World"
    }
    return data


if __name__ == "__main__":
    app.run()
