<<<<<<< HEAD
from flask import Flask, request
import requests
import uuid
import random


app = Flask(__name__)


messages_url = "http://localhost:5001/messages_service"


@app.route("/facade_service", methods=["GET", "POST"])
def handler():
    port = random.randint(5002, 5004)
    logging_url = "http://localhost:{}/logging_service".format(port)
    if request.method == "GET":
        logging_response = requests.get(logging_url).text
        messages_response = requests.get(messages_url).text
        return "Logging: {} Messages: {}".format(logging_response, messages_response)
    elif request.method == "POST":
        uid = uuid.uuid4()
        message = request.form["message"]
        data = {"id": uid,  "message": message}
        response = requests.post(logging_url, data=data).text
        return response


if __name__ == "__main__":
    app.run(port=5000)
=======
from flask import Flask, request
import requests
import uuid
import random


app = Flask(__name__)


messages_url = "http://localhost:5001/messages_service"


@app.route("/facade_service", methods=["GET", "POST"])
def handler():
    port = random.randint(5002, 5004)
    logging_url = "http://localhost:{}/logging_service".format(port)
    if request.method == "GET":
        logging_response = requests.get(logging_url).text
        messages_response = requests.get(messages_url).text
        return "Logging: {} Messages: {}".format(logging_response, messages_response)
    elif request.method == "POST":
        uid = uuid.uuid4()
        message = request.form["message"]
        data = {"id": uid,  "message": message}
        response = requests.post(logging_url, data=data).text
        return response


if __name__ == "__main__":
    app.run(port=5000)
>>>>>>> master
