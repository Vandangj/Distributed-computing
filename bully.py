import csv

# Read alive nodes from CSV
alive = []

with open(r"C:\Users\vandan\bully_cluster.csv") as file:
    for r in csv.DictReader(file):
        if r["is_alive"].strip().upper() == "TRUE":
            alive.append(int(r["node_id"]))


# Detect coordinator failure
print("Coordinator failed!")
print("Node", alive[0], "starts election")


# Election process
for i in alive:
    for j in alive:
        if j > i:
            print("Node", i, "sends ELECTION to node", j)
            print("Node", j, "replies OK to node", i)


# Highest ID becomes leader
leader = max(alive)

print("New Leader is Node", leader)


# Announce new coordinator
for i in alive:
    if i != leader:
        print("Node", leader, "sends COORDINATOR to node", i)

/// code ends here 

Q1. What is a coordinator?

A coordinator is a node responsible for managing or coordinating activities in a distributed system.

Q2. Why is it called the Bully Algorithm?

Because the node with the highest ID among active nodes takes over leadership.

Q3. What is an ELECTION message?

A message sent by a node to higher-ID nodes to initiate a leader election.

Q4. What is an OK message?

A response indicating that a higher-ID node is alive and can participate in the election.

Q5. What is a COORDINATOR message?

A message sent by the newly elected leader to announce its leadership.

Q6. Which node becomes the leader?

The alive node with the highest ID.

Q7. What happens if the highest-ID node fails?

The next highest-ID active node becomes the leader.
