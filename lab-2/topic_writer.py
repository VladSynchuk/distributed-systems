<<<<<<< HEAD
from hazelcast import HazelcastClient


client = HazelcastClient()

topic = client.get_topic("topic").blocking()
for message in range(100):
    topic.publish(message)

client.shutdown()

=======
from hazelcast import HazelcastClient


client = HazelcastClient()

topic = client.get_topic("topic").blocking()
for message in range(100):
    topic.publish(message)

client.shutdown()

>>>>>>> master
