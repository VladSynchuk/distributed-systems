from flask import Flask, request
import requests
import uuid
from random import randint
from hazelcast import HazelcastClient

app = Flask(__name__)


@app.route("/facade_service", methods=["GET", "POST"])
def handler():
    logging_url = "http://localhost:{}/logging_service".format(randint(5001, 5003))
    messages_url = "http://localhost:{}/messages_service".format(randint(5004, 5005))
    if request.method == "GET":
        logging_response = requests.get(logging_url).text
        messages_response = requests.get(messages_url).text
        return "Logging: {} Messages: {}".format(logging_response, messages_response)
    elif request.method == "POST":
        client = HazelcastClient()
        queue = client.get_queue("messages").blocking()
        uid = uuid.uuid4()
        message = request.form["message"]
        data = {"id": uid,  "message": message}
        response = requests.post(logging_url, data=data).text
        queue.offer(message)
        return response


if __name__ == "__main__":
    app.run(port=5000)
