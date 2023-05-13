import random
import time
import uuid

class Service_Registry:
    def __init__(self):
        self.nodes = []

    def register(self, node_id):
        self.nodes.append(node_id)
        print(f"Node {node_id} registered")

def nodeRegister(service_registry):
    node_id = create_node_id()
    service_registry.register(node_id)
    print(f"Node {node_id} registered")
    return node_id

def create_node_id():
    node_id = str(uuid.uuid4())
    return node_id
