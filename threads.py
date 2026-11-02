import csv
import threading
import time

lock = threading.Lock()
done = []

# Worker function
def work(r):
    time.sleep(int(r["burst_ms"]) / 1000)

    with lock:
        print(r["thread_name"], "processing", r["task_id"])
        done.append(r["task_id"])

# Read tasks from CSV
with open(r"C:\Users\vandan\tasks.csv") as file:
    rows = list(csv.DictReader(file))

# Create threads
threads = []

for r in rows:
    t = threading.Thread(target=work, args=(r,))
    threads.append(t)
    t.start()

# Wait for all threads
for t in threads:
    t.join()

print("Completed tasks:", done)
/// code ends here 

MULTITHREADING AND MUTEX – IMPORTANT VIVA

1. What is a thread?
   A thread is the smallest unit of execution within a process.

2. What is multithreading?
   It is the execution of multiple threads within a program.

3. What is a Mutex?
   Mutex stands for Mutual Exclusion. It is a lock that allows
   only one thread at a time to access a shared resource.

4. Why do we use locks?
   To prevent multiple threads from modifying shared data
   simultaneously.

5. What is a race condition?
   A race condition occurs when multiple threads access and
   modify shared data at the same time, causing unpredictable results.

6. What is a critical section?
   It is the part of the program where shared resources
   are accessed or modified.

7. What is the purpose of threading.Lock()?
   It creates a lock that controls access to the critical section.

8. What is the purpose of join()?
   It makes the main program wait until a thread finishes execution.

9. What is the purpose of start()?
   It starts the execution of a thread.

10. What is the purpose of sleep()?
    It pauses a thread for a specified amount of time.

11. What is a deadlock?
    A deadlock occurs when two or more threads wait indefinitely
    for resources held by each other.

12. What happens if we don't use a lock?
    Multiple threads may access shared data simultaneously,
    potentially causing race conditions.

13. What is the difference between a process and a thread?
    Process:
    - An independent program in execution.
    - Has its own memory space.

    Thread:
    - A unit of execution within a process.
    - Threads share the process's memory.

14. What is mutual exclusion?
    It ensures that only one thread can enter a critical
    section at a time.

15. What is the advantage of multithreading?
    It allows multiple tasks to make progress concurrently.
