from hazelcast import HazelcastClient


def on_message(message):
    print("Received message {}".format(message.message))


client = HazelcastClient()

topic = client.get_topic("topic").blocking()
topic.add_listener(on_message=on_message)
input("Topic reader 2\n")

client.shutdown()

