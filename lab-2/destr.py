from hazelcast import HazelcastClient
from hazelcast.config import Config


config = Config()
config.cluster_name = 'dev'
config.cluster_members = ['127.0.0.1:5701', '127.0.0.1:5702', '127.0.0.1:5703']
config.client_name = 'MishaPy'
client = HazelcastClient(config=config)
m = client.get_map("map")
m.destroy()
client.shutdown()
