from flask import Flask
import sys
from hazelcast import HazelcastClient

app = Flask(__name__)

port = int(sys.argv[1])

messages = []


def get_message(message):
    message = message.item
    messages.append(message)
    queue.remove(message)
    print("Received new message: {}".format(message))


@app.route("/messages_service", methods=["GET"])
def handler():
    return messages


if __name__ == "__main__":
    client = HazelcastClient()
    queue = client.get_queue("messages")
    queue.add_listener(include_value=True, item_added_func=get_message)
    app.run(port=port)
