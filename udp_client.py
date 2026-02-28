import socket

HOST = "127.0.0.1"
PORT = 5000

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    message = input("Enter message (or 'exit'): ")
    if message.lower() == "exit":
        break

    client.sendto(message.encode(), (HOST, PORT))
    data, _ = client.recvfrom(1024)

    print("Server response:", data.decode())

client.close()
