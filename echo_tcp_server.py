import socketserver
import re

class TCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        data = self.request.recv(1024).decode().strip()
        print(f"Received: {data}")

        if "SECRET" in data:
            digits = ''.join(re.findall(r'\d', data))
            response = f"Digits: {digits} Count: {len(digits)}"
        else:
            response = "Secret code not found."

        self.request.sendall(response.encode())

if __name__ == "__main__":
    #HOST, PORT = "127.0.0.1", 5001 #For local testing
    HOST, PORT = "0.0.0.0", 5000 
    with socketserver.TCPServer((HOST, PORT), TCPHandler) as server:
        print(f"Server listening on {HOST}:{PORT}")
        server.serve_forever()
