from hazelcast import HazelcastClient


client = HazelcastClient()

dist_map = client.get_map("map").blocking()
for key in range(1000):
    dist_map.put(key, str(key))

client.shutdown()

