# Q: Simulate an RPC/RMI client-server procedure dispatcher that reads method calls from a CSV, marshals arguments, executes the remote function and prints the result.
import csv
remote = {"processData": lambda x: x * 2,
          "square": lambda x: x * x,
          "increment": lambda x: x + 1}

for r in csv.DictReader(open("rpc_calls.csv"), skipinitialspace=True):
    m, p = r["method_name"], int(r["param_value"])
    print(f"[DISPATCH] {r['client_name']} invoking {m}({p})")
    print(f"[SERVER EXECUTION] Processing parameter {p}")
    print(f"[RETURN] Result = {remote[m](p)}")
