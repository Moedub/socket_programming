# TCP Socket Programming: Client-Server Communication

A Python implementation of TCP client-server communication demonstrating fundamental socket programming concepts including connection establishment, data transmission, and graceful termination.

## Overview

This project implements a basic TCP client-server application where:
- The client sends a user-provided integer (1-100) along with identification information to the server
- The server responds with its own integer and identification
- Both compute and display the sum of the exchanged integers
- The server validates input and can be gracefully terminated with out-of-range values

## Features

- **TCP Socket Communication**: Reliable connection-oriented data transmission
- **Input Validation**: Server-side validation of integer ranges
- **Graceful Termination**: Clean socket release and shutdown mechanisms
- **Informative Logging**: Both client and server provide detailed execution traces
- **Error Handling**: Robust handling of connection failures and invalid inputs

## Technologies

- **Language**: Python 3
- **Protocol**: TCP/IP
- **Libraries**: `socket`, `sys`

## Project Structure

```
socket_programming/
├── Server.py          # TCP server implementation
├── client.py          # TCP client implementation
└── README.md          # Project documentation
```

## Usage

### Starting the Server

```bash
python3 Server.py
```

The server will:
1. Bind to localhost on port 12000 (configurable)
2. Listen for incoming client connections
3. Process client messages and respond with computed results
4. Terminate when receiving an out-of-range integer (outside 1-100)

### Running the Client

```bash
python3 client.py
```

The client will:
1. Prompt for an integer between 1 and 100
2. Establish a TCP connection to the server
3. Send the integer along with client identification
4. Receive and display the server's response
5. Compute and display the sum of both integers

## Example Execution

**Server Output:**
```
Server is ready to receive
Received connection from ('127.0.0.1', 54321)
Client name: Client of Mohamed Ismail
Server name: Server of Mohamed Ismail
Client's number: 42
Server's number: 58
Sum: 100
Response sent to client
```

**Client Output:**
```
Enter an integer between 1 and 100: 42
Connecting to server...
Message sent to server
Response received from server
Client name: Client of Mohamed Ismail
Server name: Server of Mohamed Ismail
Client's number: 42
Server's number: 58
Sum: 100
```

## Technical Details

### Socket Configuration
- **Protocol**: TCP (SOCK_STREAM)
- **Default Port**: 12000
- **Host**: localhost (127.0.0.1)
- **Buffer Size**: 1024 bytes

### Message Format
Messages are exchanged as formatted strings containing:
- Sender identification (client or server name)
- Integer value (1-100)

### Termination Behavior
- **Client**: Closes socket after receiving server response
- **Server**: Continues listening until receiving out-of-range integer, then performs graceful shutdown

## Course Context

Developed as part of **Communication Networks** coursework at the University of Nebraska at Omaha, demonstrating practical understanding of:
- TCP/IP protocol stack
- Socket API programming
- Client-server architecture
- Network communication patterns

## Key Learning Outcomes

- Understanding of reliable transport protocols (TCP)
- Hands-on experience with socket programming APIs
- Implementation of connection-oriented communication
- Proper resource management (socket lifecycle)
- Error handling in networked applications

## Future Enhancements

Potential extensions to this project:
- Multi-threaded server to handle concurrent clients
- UDP implementation for comparison with TCP
- Enhanced protocol with more complex message formats
- Integration with network monitoring tools for traffic analysis

## Author

Mohamed Ismail  
Computer Science Student  
University of Nebraska at Omaha
