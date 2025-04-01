import socket

SERVER_IP = "10.10.11.2"  #R3's IP
PORT = 5001
FILENAME = "file_to_send.txt"  # File you want to send

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    client_socket.connect((SERVER_IP, PORT))

    with open(FILENAME, "rb") as f:
        data = f.read()
        client_socket.sendall(data)

    print("[+] File sent successfully.")
