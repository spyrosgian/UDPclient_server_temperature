# Importing necessary Python packages:
import socket

# Converting Centigrade temperature into a Fahrenheit:
def convert(cent):
    fahr = (9*cent)/5 + 32
    return str(fahr)

# Defining Constants:
SERVER = ""
PORT = 5000
ADDR = (SERVER, PORT)
FORMAT = "utf-8"

# UDP receiving and sending messages from and to the client:
print(f"[STARTING] Starting server with IP {SERVER} on port {PORT}...")

# Creating UDP server socket:
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Binding server socket to Local IP and selected port:
server.bind(ADDR)
print(f"[STARTED] Server with IP {SERVER} is up and running on port {PORT}.")

try:
    while True:
        # Receiving from client:
        dataclient, addr = server.recvfrom(8192)
        print(f"[NEW CONNECTION] {addr} connected.")
        print(f"[RECEIVING] Receiving from client: {addr} - Message received:", dataclient.decode(FORMAT))
        cent = float(dataclient.decode(FORMAT))
        
        # Sending to client:
        dataserver = convert(cent)
        server.sendto(dataserver.encode(FORMAT), addr)
        print(f"[SEDNING] Sending to client: {addr} - Message sent:", dataserver)
finally:
    # Closing server socket:
    server.close()
