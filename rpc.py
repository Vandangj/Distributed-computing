# Q: Simulate an RPC/RMI client-server procedure dispatcher that reads method calls from a CSV, marshals arguments, executes the remote function and prints the result.

import csv

# ---------------- SERVER SIDE ----------------

# Remote functions available on the server
remote = {
    "processData": lambda x: x * 2,
    "square": lambda x: x * x,
    "increment": lambda x: x + 1
}

# Function to receive and execute client requests
def server(method, param):

    print(f"[SERVER] Received request: {method}({param})")

    # Dispatch the requested method
    if method in remote:

        print(f"[SERVER] Executing {method}...")

        result = remote[method](param)

        print(f"[SERVER] Sending result: {result}")

        return result

    else:
        return "Method not found"


# ---------------- CLIENT SIDE ----------------

# Read requests from CSV file
for r in csv.DictReader(open("rpc_calls.csv"), skipinitialspace=True):

    client = r["client_name"]
    method = r["method_name"]
    param = int(r["param_value"])

    print(f"\n[CLIENT] {client} sending request: {method}({param})")

    # Marshalling: preparing arguments for transmission
    print(f"[CLIENT] Marshalling parameter: {param}")

    # Send request to server and receive result
    result = server(method, param)

    # Display returned result
    print(f"[CLIENT] Received result: {result}")

//// code ends here 




for viva :

RPC/RMI CLIENT-SERVER PROCEDURE DISPATCHER

1. RPC (Remote Procedure Call):
   Allows a client to call a function located on a remote computer (server).

2. RMI (Remote Method Invocation):
   Allows a client to invoke methods of an object located on a remote computer.

3. Working:
   - Client sends a request to the server.
   - Marshalling converts arguments into a format suitable for transmission.
   - Dispatcher identifies the requested function.
   - Server executes the requested function.
   - Result is returned to the client.

4. CSV:
   CSV stands for Comma-Separated Values.
   It stores client requests in tabular format.

5. csv.DictReader():
   Reads each CSV row as a dictionary using column names as keys.

6. skipinitialspace=True:
   Ignores spaces immediately after delimiters.

7. open("rpc_calls.csv"):
   Opens the CSV file for reading.

8. lambda:
   A lambda is a small anonymous function.
   Example:
       lambda x: x * 2

   Equivalent to:
       def processData(x):
           return x * 2

9. Dictionary:
   Maps method names to their corresponding functions.
   Example:
       remote["square"](4) = 16

10. int():
    Converts a string into an integer because CSV values
    are read as strings by default.

11. Dispatch:
    Identifies the requested function and directs the request
    to the appropriate function.

12. Marshalling:
    Converts arguments and data into a format suitable
    for transmission over a network.

13. Unmarshalling:
    Converts received data back into its original usable form.

14. Server Stub:
    Handles remote method requests and communication with
    the server-side implementation.

15. Client Stub:
    Acts as a local representative of the remote procedure
    and helps the client communicate with the server.

16. Dispatcher:
    Selects the appropriate function based on the method name.

17. Difference between RPC and RMI:
    RPC invokes remote procedures or functions.
    RMI invokes methods on remote objects.

18. Role of Dictionary:
    Stores method names and their corresponding functions,
    allowing dynamic function selection.

19. Role of int():
    Converts CSV string values into integers for mathematical
    operations.

20. Important Note:
    This Python program SIMULATES RPC/RMI locally.
    It does not establish actual network communication,
    serialization, or data transmission.

EXECUTION FLOW:

Client Request
      |
      v
Marshalling of Arguments
      |
      v
Dispatcher Selects Method
      |
      v
Server Executes Function
      |
      v
Result Returned to Client
