from flask import Flask


app = Flask(__name__)


@app.route("/messages_service", methods=["GET"])
def handler():
    return "Messages service static"


if __name__ == "__main__":
    app.run(port=5001)
