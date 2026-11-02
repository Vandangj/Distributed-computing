import csv

# Read client clock records
with open(r"C:\Users\vandan\cristian_clocks.csv") as file:
    for r in csv.DictReader(file):

        t0 = int(r["t0_send_ms"])
        ts = int(r["t_server_ms"])
        t1 = int(r["t1_recv_ms"])

        # Calculate RTT
        rtt = t1 - t0

        # Estimate server time at client reception
        estimated_time = ts + rtt / 2

        # Calculate clock adjustment
        adjustment = estimated_time - t1

        print("Client:", r["client_id"])
        print("RTT:", rtt, "ms")
        print("Estimated Server Time:", estimated_time, "ms")
        print("Clock Adjustment:", adjustment, "ms")
        print()

  // code ends here 

CRISTIAN'S CLOCK SYNCHRONIZATION – VIVA

1. What is Cristian's Clock Synchronization Algorithm?
   It is an algorithm used to synchronize a client's clock
   with the time provided by a time server.

2. How does Cristian's Algorithm work?
   - The client sends a request to the time server.
   - The server sends its current time.
   - The client calculates the round-trip time (RTT).
   - It estimates the server time at reception.
   - The client adjusts its clock.

3. What is RTT?
   RTT (Round-Trip Time) is the total time taken for a request
   to reach the server and the response to return.

4. What is the formula for RTT?
   RTT = t1 - t0

5. Why do we divide RTT by 2?
   We assume the network delay is approximately equal in both
   directions. Therefore, one-way delay is RTT / 2.

6. How is the estimated server time calculated?
   Estimated Time = Server Time + (RTT / 2)

7. What is clock adjustment?
   It is the difference between the estimated server time
   and the client's current time.

8. What does positive clock adjustment mean?
   The client's clock is behind the estimated server time
   and needs to move forward.

9. What does negative clock adjustment mean?
   The client's clock is ahead of the estimated server time
   and needs to move backward.

10. What is the role of the time server?
    It provides the current time to clients for synchronization.

11. What is the main disadvantage of Cristian's Algorithm?
    It assumes network delays are approximately equal in both
    directions. Network delays can cause synchronization errors.

12. What happens if the time server fails?
    Clients may not be able to synchronize their clocks
    until another time server is available.

13. What is the difference between Cristian's and Berkeley Algorithm?

    Cristian's:
    - Uses a time server.
    - Clients adjust their clocks using server time.

    Berkeley:
    - Uses a master node.
    - The master collects clock times and calculates an average.

14. Is Cristian's Algorithm centralized or distributed?
    It is centralized because clients depend on a central
    time server.
