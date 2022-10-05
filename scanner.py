#!/bin/python3

import sys
import socket
from datetime import datetime

# Define a target
if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1]) # Translate hostname to IPv4
else:
    print("Invalid amount of arguments.")

print("Syntax: python3 scanner.py <ip>")

# Banner
print ("-" * 50)
print(f"Scanning target {target}")
print(f"Time started: {str(datetime.now() )}")
print("-" * 50)

try:
    for port in range(1, 65536):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target, port)) # Return error indicator
        if result == 0:
            print(f"Port {port} is open")
        s.close()

except KeyboardInterrupt:
    print("\nExiting Program...")
    sys.exit()

except socket.gaierror:
    print("Hostname could not be resolved.")

except socket.error:
    print("Could not connect to server.")
    sys.exit()