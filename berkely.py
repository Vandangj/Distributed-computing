import csv

nodes={}
with open(r'C:\users\vandan\requests.csv') as file:
    reader=csv.DictReader(file)

    for row in reader:
        if row["is_faulty"] == "FALSE":
            nodes[int(row["node_id"])] = int(row["clock_time_sec"])

    
    avg_time=0
    for node in nodes:
        avg_time+= nodes[node]
    avg_time/= len(nodes)

    print(f"Average Time: {avg_time}")
    for node in nodes:
        print(f"Node ID: {node}, adjusted Time: {nodes[node]-avg_time}")


/// code ends here 


BERKELEY CLOCK SYNCHRONIZATION – IMPORTANT VIVA QUESTIONS

1. What is the Berkeley Clock Synchronization Algorithm?
   It is a clock synchronization algorithm used in distributed
   systems to synchronize the clocks of multiple computers.

2. Why is clock synchronization required?
   Different computers may have different clock times.
   Synchronization helps maintain a common time across the system.

3. How does the Berkeley Algorithm work?
   - A master node polls the clocks of all other nodes.
   - It collects their clock times.
   - Faulty or outlier clocks are discarded.
   - It calculates the average time.
   - It sends adjustment values to the nodes.
   - All nodes adjust their clocks accordingly.

4. What is the role of the master node?
   It collects the clock times, calculates the average
   and coordinates clock adjustments.

5. What is a faulty clock?
   A clock that gives an incorrect or unreliable time.

6. What is an outlier?
   A value that is significantly different from the other values.

7. How is the average time calculated?
   By adding all valid clock times and dividing by the
   number of valid nodes.

8. What is time adjustment?
   It is the difference between the average time and
   a node's current clock time.

9. What does a positive adjustment mean?
   The node's clock is behind the average time, so it
   needs to move forward.

10. What does a negative adjustment mean?
    The node's clock is ahead of the average time, so it
    needs to move backward.

11. Is Berkeley Algorithm centralized or decentralized?
    It is centralized because one master node coordinates
    the synchronization process.

12. What happens if the master node fails?
    Another node may be selected as the new master.

13. What is the main advantage of the Berkeley Algorithm?
    It synchronizes clocks even when the computers do not
    have access to an accurate external time source.

14. What is the difference between Berkeley and Cristian's Algorithm?
    Berkeley Algorithm:
    - Uses a master node to collect and average clock times.
    - Sends adjustments to all nodes.

    Cristian's Algorithm:
    - Uses a time server.
    - Clients adjust their clocks using the time received
      from the server.

15. Does Berkeley Algorithm make every clock exactly equal?
    Ideally, it brings all participating clocks close to
    the same time, but network delays and clock errors
    may cause small differences.
