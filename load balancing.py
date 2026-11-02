import csv

# Initial load of workers
load = {
    "W1": 0,
    "W2": 0,
    "W3": 0
}

# Read jobs from CSV
with open(r"C:\Users\vandan\workload.csv") as file:
    for r in csv.DictReader(file):

        # Select worker with minimum load
        worker = min(load, key=load.get)

        # Assign job to worker
        load[worker] += int(r["compute_units"])

        print(r["job_id"], "->", worker, "| Load:", load)

print("Final Load:", load)

/// code ends here 

DYNAMIC LOAD BALANCING – IMPORTANT VIVA

1. What is Load Balancing?
   It is the process of distributing incoming jobs among
   multiple worker nodes to avoid overloading one worker.

2. What is Dynamic Load Balancing?
   It distributes jobs based on the current workload of
   available workers.

3. What is a worker node?
   A worker node is a computer or server that performs
   assigned tasks.

4. What is the Least-Load algorithm?
   It assigns the next job to the worker having the
   minimum current workload.

5. What is the purpose of load balancing?
   To improve performance, resource utilization and
   response time.

6. What is compute_units?
   It represents the amount of processing work required
   by a particular job.

7. How does the program select a worker?
   It uses min(load, key=load.get) to find the worker
   with the smallest current load.

8. What happens after assigning a job?
   The assigned worker's load is increased by the job's
   compute units.

9. What is the difference between Least-Connections
   and Least-Load?

   Least-Connections:
   Assigns a new request to the worker with the fewest
   active connections.

   Least-Load:
   Assigns a new job to the worker with the lowest
   current workload.

10. What happens if two workers have the same load?
    The program selects the first worker encountered
    in the dictionary.

11. What are the advantages of Load Balancing?
    - Prevents overloading.
    - Improves resource utilization.
    - Distributes work efficiently.

12. Where is Load Balancing used?
    Cloud computing, web servers, distributed systems
    and large-scale applications.

13. What is the main objective of Dynamic Load Balancing?
    To distribute work according to the current load
    of each worker.
