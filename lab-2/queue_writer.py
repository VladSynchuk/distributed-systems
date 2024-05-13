from hazelcast import HazelcastClient


client = HazelcastClient()

queue = client.get_queue("queue").blocking()
for value in range(100):
    queue.put(value)

client.shutdown()

