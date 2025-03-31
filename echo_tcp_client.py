import socket
import sys

if len(sys.argv) < 2:
    print("Usage: python3 echo_tcp_client.py <your string>")
    sys.exit(1)

message = ' '.join(sys.argv[1:])
#HOST = "127.0.0.1" # Localhost for testing
HOST = "10.10.11.2"  # IP of R3
PORT = 5000          # Same port used in server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect((HOST, PORT))
    print(f"Sent: {message}")
    sock.sendall(message.encode())

    received = sock.recv(1024).decode()
    print(f"Received: {received}")
