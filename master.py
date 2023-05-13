import random
import time
from node import Service_Registry, nodeRegister


def distribute_workload(nodes, passwords):
    workload_schedule = {}
    num_nodes = len(nodes)
    num_passwords = len(passwords)
    passwords_per_node = num_passwords // num_nodes
    remaining_passwords = num_passwords % num_nodes

    start_idx = 0
    for node in nodes:
        end_idx = start_idx + passwords_per_node
        if remaining_passwords > 0:
            end_idx += 1
            remaining_passwords -= 1
        workload_schedule[node] = (start_idx, end_idx)
        start_idx = end_idx

    return workload_schedule


def distribute_password_ranges(nodes, workload_schedule):
    for node, (start_idx, end_idx) in workload_schedule.items():
        # Implement code to communicate password ranges to each node
        print(f"Send password range {start_idx}-{end_idx} to Node {node}")


def fetch_passwords_from_file(file_path):
    with open(file_path, "r") as file:
        passwords = file.read().splitlines()
    return passwords


def validate_passwords(cracked_passwords, passwords, workload_schedule):
    for node, cracked_password in cracked_passwords.items():
        if node in workload_schedule:
            password_index = workload_schedule[node][0]
            if password_index < len(passwords):
                expected_password = passwords[password_index]
                if cracked_password == expected_password:
                    print(f"Node {node} cracked the password correctly: {cracked_password}")
                else:
                    print(f"Node {node} cracked the password incorrectly")
            else:
                print(f"Node {node} has no more passwords to crack")
        else:
            print(f"Node {node} is not in the workload schedule")




def determine_master_node(nodes):
    # Implement Bully algorithm logic to elect a master node
    return random.choice(nodes)  # Placeholder for demonstration


def run_master_node():
    nodes = []
    passwords = fetch_passwords_from_file("passwords.txt")
    workload_schedule = {}

    # Register nodes and assign node IDs
    service_registry = Service_Registry()
    for i in range(5):  # Placeholder for demonstration (5 nodes)
        node_id = nodeRegister(service_registry)
        nodes.append(node_id)

    if not nodes:
        print("No nodes available")
        return

    print("Registered nodes:", nodes)

    # Elect a master node
    master_node = determine_master_node(nodes)
    print("Elected master node:", master_node)

    # Create workload schedule
    workload_schedule = distribute_workload(nodes, passwords)
    print("Workload schedule:", workload_schedule)

    # Communicate password ranges to nodes
    distribute_password_ranges(nodes, workload_schedule)

    # Continue with other master node responsibilities
    for password_index in range(len(passwords)):
        expected_password = passwords[password_index]

        # Read the first password from the file and wait for responses
        print("Verifying password:", expected_password)

        # Placeholder logic for demonstration
        cracked_passwords = {node: "abcdef" for node in nodes}

        # Verify cracked passwords
        validate_passwords(cracked_passwords, passwords, workload_schedule)


        # Send completion message to other nodes
        for node in nodes:
            if node != master_node:
                # Implement code to send completion message to other nodes
                print(f"Send completion message to Node {node}")

        # Move to the next password

run_master_node()
