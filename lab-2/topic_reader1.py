from hazelcast import HazelcastClient
import time


def on_message(message):
    time.sleep(3)
    print("Received message {}".format(message.message))


client = HazelcastClient()

topic = client.get_topic("topic").blocking()
topic.add_listener(on_message=on_message)
input("Topic reader 1\n")

client.shutdown()
