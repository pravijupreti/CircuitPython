import wifi
import socketpool
import time

print("Connecting to Wi-Fi...")

wifi.radio.connect("Rock-the-house", "Passw0rd")

print("Connected! IP address:", wifi.radio.ipv4_address)

# Resolve domain
pool = socketpool.SocketPool(wifi.radio)
addr_info = pool.getaddrinfo("example.com", 80)[0]
addr = addr_info[4]

# Create a socket and connect
sock = pool.socket()
sock.connect(addr)

# Send HTTP GET request
request = "GET / HTTP/1.1\r\nHost: example.com\r\nConnection: close\r\n\r\n"
sock.send(request.encode("utf-8"))

# Receive response
response = b""
buffer = bytearray(1024)

while True:
    size = sock.recv_into(buffer)
    if size == 0:
        break
    response += buffer[:size]

sock.close()
# Print the HTTP response
print("Response from server:")
print(response.decode("utf-8"))
