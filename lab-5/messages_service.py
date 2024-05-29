from flask import Flask
import sys
from hazelcast import HazelcastClient
import consul
import uuid

app = Flask(__name__)

port = int(sys.argv[1])
if len(sys.argv) > 2:
    address = sys.argv[2]
else:
    address = "127.0.0.1"

messages = []


def register_service():
    c.agent.service.register(name="messages service",
                             service_id=str(uuid.uuid4()),
                             address=address,
                             port=port)


def get_message(message):
    message = message.item
    messages.append(message)
    queue.remove(message)
    print("Received new message: {}".format(message))


@app.route("/messages_service", methods=["GET"])
def handler():
    return messages


if __name__ == "__main__":
    c = consul.Consul()
    register_service()
    c_queue = c.kv.get("queue")[1]["Value"].decode()
    client = HazelcastClient()
    queue = client.get_queue(c_queue)
    queue.add_listener(include_value=True, item_added_func=get_message)
    app.run(port=port, host=address)
