import socket
import json
import datetime
import math


now = datetime.datetime.now()

sock = socket.socket()
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

m = {"id": "Kalinka George", "value": math.sin(now.second)}
data = json.dumps(m)

try:
    sock.connect(('192.168.0.108', 5268))

    print("Connect ok")
    sock.sendall(bytes(data,encoding="utf-8"))

finally:
    sock.close()

print ("Sent: {}".format(data))