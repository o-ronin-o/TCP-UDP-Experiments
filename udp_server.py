import socket

HOST = "0.0.0.0"
PORT = 5000


def process_message(message):
    if not message:
        return message

    command = message[0]
    data = message[1:]

    if command == 'A':
        return ''.join(sorted(data, reverse=True))
    elif command == 'C':
        return ''.join(sorted(data))
    elif command == 'D':
        return data.upper()
    else:
        return message


def start_udp_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server.bind((HOST, PORT))

    print(f"[UDP SERVER LISTENING] on port {PORT}")

    while True:
        data, addr = server.recvfrom(1024)
        message = data.decode().strip()

        print(f"[RECEIVED from {addr}] {message}")

        response = process_message(message)
        server.sendto(response.encode(), addr)


if __name__ == "__main__":
    start_udp_server()
