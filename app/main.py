import socket  # noqa: F401


def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    print("Logs from your program will appear here!")

    # Uncomment this to pass the first stage
    #
    server_socket = socket.create_server(("localhost", 6379), reuse_port=True)
   # server_socket.accept() # wait for client

    # Accept client connection (blocking call)
    # connection, _ = server_socket.accept()

    # # Send a PONG response using Redis protocol format
    # connection.sendall(b"+PONG\r\n")

    # # Optionally, close the connection (depends on spec)
    # connection.close()

        # Accept a client connection
    connection, _ = server_socket.accept()
    print("Client connected.")

    # Loop to respond to multiple PINGs
    while True:
        data = connection.recv(1024)  # Read up to 1024 bytes
        if not data:
            break  # Client closed connection

        # For every message (we assume it's a PING), send a PONG
        connection.sendall(b"+PONG\r\n")
    connection.close()
    print("Connection closed.")


if __name__ == "__main__":
    main()
