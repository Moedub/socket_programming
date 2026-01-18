import socket

def main():
    # Configuration
    SERVER_HOST = 'localhost'  # Change this to your server's IP if needed
    SERVER_PORT = 5555
    CLIENT_NAME = "Client of Mohamed Ismail"
    
    print("=== TCP Client Started ===")
    print(f"Client Name: {CLIENT_NAME}")
    
    # Get integer input from user
    while True:
        try:
            client_number = int(input("Enter an integer between 1 and 100: "))
            
            if 1 <= client_number <= 100:
                break
            else:
                print("Number out of range. Please enter a value between 1 and 100.")
        except ValueError:
            print("Invalid input. Please enter an integer.")
    
    print(f"Client number entered: {client_number}")
    
    # Create TCP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print(f"Socket created successfully")
    
    try:
        # Connect to server
        print(f"Attempting to connect to server at {SERVER_HOST}:{SERVER_PORT}...")
        client_socket.connect((SERVER_HOST, SERVER_PORT))
        print("Connected to server successfully")
        
        # Prepare and send message
        message = f"{CLIENT_NAME}|{client_number}"
        print(f"Sending message to server: {message}")
        client_socket.send(message.encode('utf-8'))
        print("Message sent successfully")
        
        # Wait for server response
        print("Waiting for server response...")
        response = client_socket.recv(1024).decode('utf-8')
        print(f"Received response from server: {response}")
        
        # Parse server response
        server_name, server_number_str = response.split('|')
        server_number = int(server_number_str)
        
        # Display results
        print("\n=== Results ===")
        print(f"Client Name: {CLIENT_NAME}")
        print(f"Server Name: {server_name}")
        print(f"Client Number: {client_number}")
        print(f"Server Number: {server_number}")
        print(f"Sum: {client_number + server_number}")
        
    except ConnectionRefusedError:
        print("ERROR: Could not connect to server. Is the server running?")
    except Exception as e:
        print(f"ERROR: {e}")
    finally:
        # Close socket
        print("\nClosing client socket...")
        client_socket.close()
        print("Client socket closed. Client terminating.")

if __name__ == "__main__":
    main()