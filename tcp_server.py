import socket
import threading

HOST = "0.0.0.0"
PORT = 5001


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


def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")

    try:
        while True:
            data = conn.recv(1024).decode().strip()
            if not data:
                break

            print(f"[RECEIVED from {addr}] {data}")

            response = process_message(data)
            conn.sendall(response.encode())

    except:
        pass

    print(f"[DISCONNECTED] {addr}")
    conn.close()


def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()

    print(f"[TCP SERVER LISTENING] on port {PORT}")

    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()


if __name__ == "__main__":
    start_server()
