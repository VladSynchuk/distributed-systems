from flask import Flask, request


app = Flask(__name__)

messages = {}


@app.route("/logging_service", methods=["GET", "POST"])
def handler():
    if request.method == "GET":
        return ";".join(messages.values())
    elif request.method == "POST":
        uuid = request.form["id"]
        message = request.form["message"]
        messages[uuid] = message
        print("Received new message: {}".format(message))
        return "Message received"


if __name__ == "__main__":
    app.run(port=5002)
