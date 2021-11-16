# Серверный
import time
import socket
import network

sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.active()

sta_if.connect("WIFIFORESP", "123esp321!")

time.sleep(5)

print("\n", sta_if.ifconfig())

s = socket.socket()
s.bind(("", 5268))
s.listen(2)

while True:
    client, addr = s.accept()

    data = client.recv(1024)

    print(data.decode())
    print(addr)
    # client.send(b"1")
    client.close()