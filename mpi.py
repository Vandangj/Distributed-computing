import csv
from multiprocessing.pool import ThreadPool

# Read matrix from CSV
with open(r"C:\Users\vandan\matrix.csv") as file:
    A = []
    for r in csv.DictReader(file):
        A.append([int(v) for v in list(r.values())[1:]])

# Scatter rows to workers
for i in range(len(A)):
    print("Master sends row", i, "to Worker", i)

# Worker performs multiplication
def multiply(i):
    result = []
    for col in A:
        total = 0
        for x, y in zip(A[i], col):
            total += x * y
        result.append(total)
    return result

# Execute workers in parallel
pool = ThreadPool(len(A))
res = pool.map(multiply, range(len(A)))

# Gather results
for i in range(len(res)):
    print("Worker", i, "result:", res[i])

print("Final Matrix A x A^T:", res)

/// code ends here 

PARALLEL MATRIX MULTIPLICATION – IMPORTANT VIVA

1. What is parallel computing?
   It is the process of dividing a large task into smaller
   tasks and executing them simultaneously.

2. What is MPI?
   MPI stands for Message Passing Interface. It is a standard
   used for communication between processes in parallel computing.

3. What is Scatter?
   Scatter distributes data from the master process
   among multiple worker processes.

4. What is Gather?
   Gather collects the results from worker processes
   and combines them at the master process.

5. What is matrix multiplication?
   It is the process of multiplying rows of one matrix
   with columns of another matrix.

6. What is a dot product?
   It is the sum of the products of corresponding elements
   of two vectors.

7. What is A × Aᵀ?
   It means multiplying matrix A by its transpose.

8. What is a ThreadPool?
   It manages multiple threads and distributes tasks
   among them.

9. What is the role of the master?
   It distributes rows to workers and collects their results.

10. What is the role of workers?
    Each worker calculates the dot products for its assigned row.

11. Why is parallel processing used?
    To reduce execution time by performing tasks concurrently.

12. What is the difference between multiprocessing and multithreading?
    Multiprocessing uses multiple processes.
    Multithreading uses multiple threads within a process.

13. What is the advantage of parallel matrix multiplication?
    It can speed up computation for large matrices.

14. Is this actual MPI?
    No. It simulates the Scatter-Gather pattern using Python
    threads. It does not use an actual MPI library.
