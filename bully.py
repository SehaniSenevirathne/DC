import random
from datetime import datetime
from time import sleep

def initiate_election(nodes):
    # Generate a random node ID
    node_id = create_node_id()

    # Wait for a random period of time
    wait_time = random.randint(1, 5)
    sleep(wait_time)

    # Check if there is already a leader
    leader = determine_leader(nodes)
    if leader is None:
        # No leader exists, current node starts the election
        print(f"Node {node_id} starts the election")
        nodes[node_id] = "Elected"  # Mark current node as elected

        # Send election message to higher priority nodes
        higher_priority_nodes = find_higher_priority_nodes(node_id, nodes)
        for higher_priority_node in higher_priority_nodes:
            forward_election_message(node_id, higher_priority_node)

        # Wait for response from higher priority nodes
        sleep(2)

        # Check if the current node is still elected
        if nodes.get(node_id) == "Elected":  # Check if the key exists
            # Current node becomes the leader
            nodes["leader"] = node_id
            print(f"Node {node_id} becomes the leader")
            return True  # Leader elected, return True
        else:
            # Current node lost the election
            nodes[node_id] = "Lost"  # Update node state to "Lost"
            print(f"Node {node_id} lost the election")
    else:
        # Leader exists, current node participates in ongoing election
        print(f"Node {node_id} participates in the ongoing election")

        # Send election message to higher priority nodes
        higher_priority_nodes = find_higher_priority_nodes(node_id, nodes)
        for higher_priority_node in higher_priority_nodes:
            forward_election_message(node_id, higher_priority_node)

        # Wait for response from higher priority nodes
        sleep(2)

        # Check if the current node is still elected
        if nodes.get(node_id) == "Elected":  # Check if the key exists
            # Current node becomes the leader
            nodes["leader"] = node_id
            print(f"Node {node_id} becomes the leader")
            return True  # Leader elected, return True
        else:
            # Current node lost the election
            nodes[node_id] = "Lost"  # Update node state to "Lost"
            print(f"Node {node_id} lost the election")

    return False  # No leader elected, return False


def create_node_id():
    timestamp = datetime.now().timestamp()
    random_num = random.randint(1, 100)
    return int(timestamp + random_num)


def determine_leader(nodes):
    return nodes.get("leader")


def find_higher_priority_nodes(node_id, nodes):
    higher_priority_nodes = []
    for node in nodes:
        if node != node_id and nodes[node] == "Elected":
            higher_priority_nodes.append(node)
    return higher_priority_nodes


def forward_election_message(source_node, destination_node):
    print(f"Node {source_node} sends an election message to Node {destination_node}")
    # Simulate message receiving by the destination node
    print(f"Node {destination_node} receives an election message from Node {source_node}")



def main():
    nodes = {}  # Dictionary to store node IDs and their states
    node_id = create_node_id()
    nodes[node_id] = "Elected"  # Add current node ID to the dictionary

    while True:
        if initiate_election(nodes):
            break  # Leader elected, break out of the loop
        sleep(5)


if __name__ == "__main__":
    main()
