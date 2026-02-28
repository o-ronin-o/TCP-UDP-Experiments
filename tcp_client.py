import socket

HOST = "127.0.0.1"
PORT = 5001

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

while True:
    message = input("Enter message (or 'exit'): ")
    if message.lower() == "exit":
        break

    client.sendall(message.encode())
    response = client.recv(1024).decode()

    print("Server response:", response)

client.close()
