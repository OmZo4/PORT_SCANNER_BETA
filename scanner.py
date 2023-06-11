#!/usr/bin/python3

import sys
import socket
import subprocess
from datetime import datetime


target = input("Enter your target IP to find open ports: _")
port_x = int(input("Which port interval do u wanna work on?(A-B)  A: _"))
port_y = int(input("B: _"))


subprocess.call('clear',shell=True)
print("-" * 60)
print("            OMZO PORT SCANNER BETA0.1")
print(f"Scanning target: {target} from port {port_x} to port {port_y}")
print("Time started " + str(datetime.now()))
print("-" * 60)

try:
    for port in range(port_x, port_y + 1):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target, port))
        if (result == 0):
           print(f"port {port} is open")
        else:
           print(f"port {port} is closed")


except KeyboardInterrupt:
    print("\nExiting program")
    sys.exit()
except socket.gaierror:
    print("\nHostname could not be resolved.")
    sys.exit()
except socket.error:
    print("\nCould not connect to server.")
    sys.exit()
