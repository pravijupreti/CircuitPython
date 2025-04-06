import wifi
import socketpool
import time
import usb_hid
import json
from RequestHandler import ServerManager
from string_generator import StringGenerator
from KeyCode import KeyCodeMapper
from adafruit_hid.keyboard import Keyboard

# Set up Wi-Fi
wifi.radio.connect("Rock-the-house", "Passw0rd")
print("Connected to Wi-Fi, IP address:", wifi.radio.ipv4_address)

# Set up the keyboard HID
keyboard = Keyboard(usb_hid.devices)

# Create the keycode mapper once
mapper = KeyCodeMapper()

# Create a socket pool for HTTP server
pool = socketpool.SocketPool(wifi.radio)

def start_server():
    server = pool.socket()
    server.settimeout(None)
    server.bind(("0.0.0.0", 80))
    server.listen(1)
    print("HTTP server is listening...")
    return server

server = start_server()

while True:
    try:
        client, addr = server.accept()
        print("Client connected from", addr)
        
        manager = ServerManager(client)
        headers,body = manager.handle_request()
        # Step 4: Parse JSON and type text
        try:
            data = json.loads(body)
            text = data.get("text", "")
            print("Parsed text:", text)

            # Step 5: Send keypresses for each character
            try:
                if keycode is not None:
                    string_gen.type_string(text, delay=0.1)
            except Exception as e:
                    print(f"Error pressing key '{text}")
        except json.JSONDecodeError as json_err:
            print("Failed to parse JSON:", json_err)

        # Step 6: Send response
        response = "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\nRequest Processed"
        client.send(response.encode())
        client.close()

    except Exception as e:
        print(f"Error: {e}")
        try:
            client.close()
        except:
            pass
        server.close()
        server = start_server()
