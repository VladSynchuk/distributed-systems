from flask import Flask, request
from hazelcast import HazelcastClient
import sys
import os
import threading
import subprocess


app = Flask(__name__)

port = sys.argv[1]
hazelcast = r"D:\hazelcast\bin;"
PATH = os.environ.get("PATH") + hazelcast
os.environ["PATH"] = PATH


@app.route("/logging_service", methods=["GET", "POST"])
def handler():
    client = HazelcastClient()
    messages = client.get_map("messages").blocking()
    if request.method == "GET":
        return ";".join(messages.values())
    elif request.method == "POST":
        uuid = request.form["id"]
        message = request.form["message"]
        messages.put(uuid, message)
        print("Received new message: {}".format(message))
        return "Message received"


if __name__ == "__main__":
    thread_service = threading.Thread(target=app.run, kwargs={"port": port})
    thread_hazelcast = threading.Thread(target=subprocess.run, args=["hz-start.bat"])
    thread_service.start()
    thread_hazelcast.start()
