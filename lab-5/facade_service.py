from flask import Flask, request
import requests
import uuid
import random
from hazelcast import HazelcastClient
import consul
import sys

app = Flask(__name__)

port = int(sys.argv[1])
if len(sys.argv) > 2:
    address = sys.argv[2]
else:
    address = "127.0.0.1"


def register_service():
    c.agent.service.register(name="facade service",
                             service_id=str(uuid.uuid4()),
                             address=address,
                             port=port)


@app.route("/facade_service", methods=["GET", "POST"])
def handler():
    log_service = random.choice(c.catalog.service("logging service")[1])
    msg_service = random.choice(c.catalog.service("messages service")[1])
    logging_url = "http://{host}:{port}/logging_service".format(host=log_service["ServiceAddress"],
                                                                port=log_service["ServicePort"])
    messages_url = "http://{host}:{port}/messages_service".format(host=msg_service["ServiceAddress"],
                                                                  port=msg_service["ServicePort"])
    if request.method == "GET":
        logging_response = requests.get(logging_url).text
        messages_response = requests.get(messages_url).text
        return "Logging: {} Messages: {}".format(logging_response, messages_response)
    elif request.method == "POST":
        client = HazelcastClient()
        queue = client.get_queue(c_queue).blocking()
        uid = uuid.uuid4()
        message = request.form["message"]
        data = {"id": uid,  "message": message}
        response = requests.post(logging_url, data=data).text
        queue.offer(message)
        return response


if __name__ == "__main__":
    c = consul.Consul()
    register_service()
    if not c.kv.get("map")[1]:
        c.kv.put("map", "messages")
    if not c.kv.get("queue")[1]:
        c.kv.put("queue", "messages")
    c_queue = c.kv.get("queue")[1]["Value"].decode()
    app.run(port=port, host=address)
