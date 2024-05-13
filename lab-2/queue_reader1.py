from hazelcast import HazelcastClient
import time


client = HazelcastClient()

items = []
queue = client.get_queue("queue").blocking()
while True:
    item = queue.poll()
    if item is None:
        break
    items.append(item)
    time.sleep(0.5)
print("Reader 1\n{}".format(items))

client.shutdown()

