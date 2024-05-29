from flask import Flask, request
from hazelcast import HazelcastClient
import sys
import os
import threading
import subprocess
import uuid
import consul

app = Flask(__name__)

port = int(sys.argv[1])
if len(sys.argv) > 2:
    address = sys.argv[2]
else:
    address = "127.0.0.1"

hazelcast = r"D:\hazelcast\bin;"
PATH = os.environ.get("PATH") + hazelcast
os.environ["PATH"] = PATH


def register_service():
    c.agent.service.register(name="logging service",
                             service_id=str(uuid.uuid4()),
                             address=address,
                             port=port)


@app.route("/logging_service", methods=["GET", "POST"])
def handler():
    client = HazelcastClient()
    messages = client.get_map(c_map).blocking()
    if request.method == "GET":
        return ";".join(messages.values())
    elif request.method == "POST":
        uid = request.form["id"]
        message = request.form["message"]
        messages.put(uid, message)
        print("Received new message: {}".format(message))
        return "Message received"


if __name__ == "__main__":
    c = consul.Consul()
    register_service()
    c_map = c.kv.get("map")[1]["Value"].decode()
    thread_service = threading.Thread(target=app.run, kwargs={"port": port, "host": address})
    thread_hazelcast = threading.Thread(target=subprocess.run, args=["hz-start.bat"])
    thread_service.start()
    thread_hazelcast.start()
