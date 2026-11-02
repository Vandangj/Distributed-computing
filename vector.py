import csv

# Three processes with initial clocks [0, 0, 0]
P = ["P1", "P2", "P3"]
clock = {p: [0, 0, 0] for p in P}
messages = {}
events = {}

with open(r"C:\Users\vandan\vector_events.csv") as file:
    for r in csv.DictReader(file):

        p = r["process_id"]
        action = r["event_action"]

        # Receive event
        if action == "RECEIVE" and p in messages:
            for i in range(3):
                clock[p][i] = max(clock[p][i], messages[p][i])

        # Increment own process clock
        clock[p][P.index(p)] += 1

        # Send event
        if action == "SEND":
            messages[r["target_process"]] = clock[p][:]

        events[r["event_id"]] = clock[p][:]
        print(r["event_id"], p, action, ":", clock[p])

# Check causal relationship
print("\nCausal Relationships:")

ids = list(events)

for i in range(len(ids)):
    for j in range(i + 1, len(ids)):

        a = events[ids[i]]
        b = events[ids[j]]

        if all(x <= y for x, y in zip(a, b)) and a != b:
            print(ids[i], "happened before", ids[j])

        elif all(x <= y for x, y in zip(b, a)) and a != b:
            print(ids[j], "happened before", ids[i])

        else:
            print(ids[i], "and", ids[j], "are concurrent")


  // code ends here 

VECTOR CLOCKS – IMPORTANT VIVA

1. What is a Vector Clock?
   It is a logical clock used in distributed systems to track
   the ordering and causal relationship between events.

2. Why do we use Vector Clocks?
   To determine whether events are causally related or concurrent.

3. What does a vector [1, 0, 0] represent?
   It represents the logical clock values of P1, P2 and P3.
   P1 has a timestamp of 1, while P2 and P3 have 0.

4. How many values does a vector clock contain?
   One value for each process in the distributed system.

5. What are the rules of Vector Clocks?
   - Increment the process's own clock for every event.
   - On SEND, attach the current vector to the message.
   - On RECEIVE, take the maximum of the local and received
     vectors, then increment the receiving process's own clock.

6. How do we identify causality?
   If every component of vector A is less than or equal to
   the corresponding component of B, and at least one is
   strictly smaller, then A happened before B.

7. What are concurrent events?
   Events where neither happened before the other.
   Neither vector is component-wise less than or equal to
   the other.

8. What is the difference between Lamport and Vector Clocks?
   Lamport Clock:
   - Uses a single integer per process.
   - Cannot identify concurrent events accurately.

   Vector Clock:
   - Uses an array of logical clock values.
   - Can identify causal and concurrent events.

9. What is the advantage of Vector Clocks?
   They provide more accurate information about event causality.

10. What is the disadvantage of Vector Clocks?
    They require more storage and communication because
    every message carries a vector.

11. What is the purpose of the maximum operation?
    It merges the local and received logical clock information.

12. What does [1, 0, 0] || [0, 1, 0] mean?
    The two events are concurrent because neither vector
    is less than or equal to the other.

13. Where are Vector Clocks used?
    Distributed databases, version control and conflict detection.

14. Does Vector Clock use actual physical time?
    No. It uses logical counters to track event ordering.
