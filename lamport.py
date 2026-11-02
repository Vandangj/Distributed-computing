import csv

clock = {}
messages = {}
events = []

with open(r"C:\Users\vandan\events.csv") as file:
    for r in csv.DictReader(file):

        p = r["process_id"]
        event = r["event_type"]

        if p not in clock:
            clock[p] = int(r["initial_clock"])

        # Receive event
        if event == "RECEIVE" and p in messages:
            clock[p] = max(clock[p], messages[p])

        # Increment logical clock
        clock[p] += 1

        # Send event
        if event == "SEND":
            messages[r["message_to"]] = clock[p]

        events.append((clock[p], p, r["event_id"]))

        print(r["event_id"], p, event, "Logical Clock:", clock[p])

# Print total order
events.sort()

print("\nTotal Causal Order:")
for e in events:
    print(e[2], "(L =", e[0], ",", e[1], ")")

// code ends here 

LAMPORT'S LOGICAL CLOCK – VIVA

1. What is a Lamport Logical Clock?
   It is a technique used in distributed systems to order events
   without requiring synchronized physical clocks.

2. Why do we use logical clocks?
   To determine the ordering of events in a distributed system.

3. What are the three types of events?
   - Send event
   - Receive event
   - Internal (local) event

4. What are the rules of Lamport's Clock?
   - Before every event, increment the process clock by 1.
   - When sending a message, attach the current timestamp.
   - When receiving a message, set the clock to the maximum
     of the local clock and received timestamp, then add 1.

5. What is the formula for a receive event?
   C = max(local clock, received timestamp) + 1

6. What is a logical timestamp?
   A number assigned to an event to represent its logical order.

7. What is the Happened-Before relationship?
   It represents the causal relationship between two events.
   If event A influences event B, then A happened before B.

8. What is the difference between physical and logical clocks?
   Physical clocks show actual time.
   Logical clocks represent the order of events.

9. Can two events have the same Lamport timestamp?
   Yes. Events in different processes can have the same timestamp.

10. How do we break ties between events?
    By using process IDs as a secondary sorting criterion.

11. What is the main limitation of Lamport Clocks?
    They cannot identify whether two events are concurrent.

12. What is a concurrent event?
    Two events are concurrent when neither event causally
    affects the other.

13. What is the main advantage of Lamport Clocks?
    They provide a simple way to maintain event ordering
    in distributed systems.

14. Does Lamport Clock require synchronized physical clocks?
    No. It uses logical counters instead of actual clock time.

15. What does A → B mean?
    It means event A happened before event B.
