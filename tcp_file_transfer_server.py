import socket

HOST = "0.0.0.0"  # Listen on all interfaces
PORT = 5001
FILENAME = "received_file.txt"

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((HOST, PORT))
    server_socket.listen(1)
    print(f"[+] Server listening on {HOST}:{PORT}...")

    conn, addr = server_socket.accept()
    print(f"[+] Connection from {addr}")

    with open(FILENAME, "wb") as f:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            f.write(data)

    print(f"[+] File received and saved as '{FILENAME}'")
    conn.close()
