import csv

# READ CSV
nodes = []

with open(r"C:\Users\vandan\requests.csv") as file:
    for r in csv.DictReader(file):
        if r["is_active"].strip().upper() == "TRUE":
            nodes.append(int(r["node_id"]))

# START ELECTION
print("Coordinator failed!")
print("Election started by Node", nodes[0])

token = []

# PASS TOKEN THROUGH ACTIVE NODES
for i in range(len(nodes)):
    token.append(nodes[i])
    print("Token passed to Node", nodes[i], ":", token)

# ELECT LEADER
leader = max(token)

print("New Coordinator is Node", leader)

// code ends here 

RING LEADER ELECTION – IMPORTANT VIVA QUESTIONS

1. What is the Ring Election Algorithm?
   It is a distributed algorithm used to elect a new coordinator
   when the current coordinator fails.

2. Why is it called the Ring Algorithm?
   Because nodes are logically connected in a circular structure.

3. How does the Ring Election Algorithm work?
   - A node detects coordinator failure.
   - It starts an election by passing a token.
   - The token circulates through active nodes.
   - The node with the highest ID is elected coordinator.

4. How is the new coordinator selected?
   The active node with the highest ID becomes the coordinator.

5. What happens if a node is inactive?
   The election process skips that node and moves to the next
   active node.

6. What happens after a new coordinator is elected?
   The new coordinator announces its election to all active nodes.

7. What is an election token?
   It is a message passed between nodes containing information
   about the participating nodes.

8. What is the advantage of the Ring Algorithm?
   It provides an organized way to elect a coordinator through
   circular communication.

9. What is the disadvantage of the Ring Algorithm?
   The token may need to pass through many nodes, making the
   election process time-consuming.

10. What is the difference between Ring and Bully Algorithm?

    Ring Algorithm:
    - Uses circular communication.
    - Passes an election token between nodes.

    Bully Algorithm:
    - Sends election messages to nodes with higher IDs.
    - The highest active ID becomes the coordinator.

11. What is a distributed system?
    A collection of independent computers or nodes that
    communicate and work together.

12. Can the election happen again?
    Yes. If the new coordinator fails, another election
    can be started.
