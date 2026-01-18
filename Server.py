import socket

def main():
    # Configuration
    SERVER_HOST = 'localhost'  # Listen on all interfaces
    SERVER_PORT = 5555
    SERVER_NAME = "Server of Mohamed Ismail"
    SERVER_NUMBER = 42  # The server's chosen number (can be any number 1-100)
    
    print("=== TCP Server Started ===")
    print(f"Server Name: {SERVER_NAME}")
    print(f"Server Number: {SERVER_NUMBER}")
    
    # Create TCP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Server socket created successfully")
    
    # Set socket option to reuse address (helps avoid "address already in use" errors)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    try:
        # Bind socket to address and port
        server_socket.bind((SERVER_HOST, SERVER_PORT))
        print(f"Server socket bound to {SERVER_HOST}:{SERVER_PORT}")
        
        # Listen for incoming connections
        server_socket.listen(5)
        print("Server is listening for connections...")
        print("(Send an out-of-range number to terminate the server)")
        
        while True:
            # Accept client connection
            print("\nWaiting for client connection...")
            client_socket, client_address = server_socket.accept()
            print(f"Connection established with client at {client_address}")
            
            try:
                # Receive message from client
                print("Receiving message from client...")
                message = client_socket.recv(1024).decode('utf-8')
                print(f"Received message: {message}")
                
                # Parse client message
                client_name, client_number_str = message.split('|')
                client_number = int(client_number_str)
                
                # Check if number is out of range (termination condition)
                if client_number < 1 or client_number > 100:
                    print(f"ERROR: Received out-of-range number: {client_number}")
                    print("Terminating server as requested...")
                    client_socket.close()
                    break
                
                # Display information
                print("\n=== Processing Request ===")
                print(f"Client Name: {client_name}")
                print(f"Server Name: {SERVER_NAME}")
                print(f"Client Number: {client_number}")
                print(f"Server Number: {SERVER_NUMBER}")
                print(f"Sum: {client_number + SERVER_NUMBER}")
                
                # Send response to client
                response = f"{SERVER_NAME}|{SERVER_NUMBER}"
                print(f"\nSending response to client: {response}")
                client_socket.send(response.encode('utf-8'))
                print("Response sent successfully")
                
            except Exception as e:
                print(f"ERROR processing client request: {e}")
            finally:
                # Close client socket
                print("Closing client connection...")
                client_socket.close()
                print("Client connection closed")
        
    except Exception as e:
        print(f"ERROR: {e}")
    finally:
        # Close server socket
        print("\nClosing server socket...")
        server_socket.close()
        print("Server socket closed. Server terminated.")

if __name__ == "__main__":
    main()