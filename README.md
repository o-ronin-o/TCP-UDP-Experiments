# Echo Server Project (TCP & UDP)

## Overview

This project implements a network-based echo service using Python socket programming.
It supports both:

* **TCP (multi-threaded, connection-oriented)**
* **UDP (connectionless, datagram-based)**

The server processes client messages according to specific rules and returns a transformed response.

The project demonstrates practical implementation of:

* Socket programming
* TCP vs UDP behavior
* Multi-threading in network servers
* Network packet inspection using Wireshark

---

## Features

* Multi-threaded TCP server (concurrent client handling)
* UDP server (connectionless communication)
* Interactive client programs
* Deterministic message processing rules
* Makefile for simplified execution
* Network traffic inspection support

---

## Project Structure

```
.
├── tcp_server.py
├── udp_server.py
├── tcp_client.py
├── udp_client.py
├── Makefile
└── README.md
```

---

## Requirements

* Python 3.8+
* Make (optional but recommended)
* Wireshark (for traffic inspection)

Install Python if needed from:
[https://www.python.org/](https://www.python.org/)

---

## Message Processing Logic

Each message must follow this format:

```
<COMMAND><STRING>
```

Where:

| Command | Behavior                            |
| ------- | ----------------------------------- |
| `A`     | Sort characters in descending order |
| `C`     | Sort characters in ascending order  |
| `D`     | Convert string to uppercase         |
| Other   | Return message unchanged            |

### Example

Input:

```
Ahello
```

Output:

```
ollhe
```

---

# TCP Implementation

## Characteristics

* Uses `socket.SOCK_STREAM`
* Connection-oriented
* Reliable, ordered communication
* Multi-threaded design
* One thread per client connection

## Architecture

1. Server binds to a port
2. Server listens for incoming connections
3. When a client connects:

   * `accept()` returns a new socket
   * A new thread is created
4. Each thread handles its client independently

This design allows multiple clients to interact with the server concurrently.

---

# UDP Implementation

## Characteristics

* Uses `socket.SOCK_DGRAM`
* Connectionless
* Message boundaries preserved
* No reliability guarantees
* Single-threaded (sufficient for datagram model)

## Architecture

1. Server binds to a port
2. Receives datagrams using `recvfrom()`
3. Processes message
4. Sends response using `sendto()`

No connection establishment phase is required.

---

# How To Run

## Using Makefile (Recommended)

### Start TCP server

```
make tcp-server
```

### Start TCP client (in another terminal)

```
make tcp-client
```

---

### Start UDP server

```
make udp-server
```

### Start UDP client (in another terminal)

```
make udp-client
```

---

## Manual Execution (Without Make)

### TCP

Terminal 1:

```
python3 tcp_server.py
```

Terminal 2:

```
python3 tcp_client.py
```

---

### UDP

Terminal 1:

```
python3 udp_server.py
```

Terminal 2:

```
python3 udp_client.py
```

---

# Network Traffic Inspection

To inspect communication:

1. Open Wireshark
2. Select the correct interface:

   * Loopback (`lo`, `lo0`, or `Npcap Loopback Adapter`) if testing locally
3. Start capture before sending messages

## Filters

For TCP:

```
tcp.port == 5001
```

For UDP:

```
udp.port == 5000
```

You should observe:

### TCP

* Three-way handshake (SYN, SYN-ACK, ACK)
* Data packets
* FIN/ACK connection termination

### UDP

* Independent request datagram
* Independent response datagram

---

# Design Considerations

## Threading Model (TCP)

The TCP server creates one thread per connected client.
Threads terminate when clients disconnect.

This model:

* Enables concurrency
* Is simple to implement
* May not scale to extremely high loads
* Is appropriate for moderate workloads

## Blocking Behavior

The implementation uses blocking sockets:

* `accept()` blocks until a client connects
* `recv()` blocks until data arrives

This simplifies logic and avoids busy-waiting.

---

# TCP vs UDP Comparison

| Feature     | TCP                    | UDP                                    |
| ----------- | ---------------------- | -------------------------------------- |
| Connection  | Yes                    | No                                     |
| Reliability | Guaranteed             | Not guaranteed                         |
| Ordering    | Preserved              | Not guaranteed                         |
| Speed       | Moderate               | Fast                                   |
| Use Case    | Reliable communication | Real-time or lightweight communication |

---

# Error Handling

The TCP server:

* Handles client disconnections gracefully
* Continues serving other clients if one disconnects

The UDP server:

* Handles independent datagrams
* Remains operational regardless of sender state

---

# Possible Extensions

* Thread pool instead of unlimited thread creation
* Asynchronous implementation using `asyncio`
* Logging to file
* Performance benchmarking
* Load testing with multiple clients

---

# Educational Objectives Demonstrated

* Practical socket programming
* Difference between stream and datagram communication
* Blocking I/O behavior
* Multi-threaded server design
* Network-level packet inspection
* Understanding TCP handshake and UDP message flow

---

# Author

Omar Wael Al-Qattan
Computer & Communication Engineering
Alexandria University

---

