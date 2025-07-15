import socket  # noqa: F401


def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    print("Logs from your program will appear here!")

    # Uncomment this to pass the first stage
    #
    server_socket = socket.create_server(("localhost", 6379), reuse_port=True)
   # server_socket.accept() # wait for client

     # Accept client connection (blocking call)
    connection, _ = server_socket.accept()

    # Send a PONG response using Redis protocol format
    connection.sendall(b"+PONG\r\n")

    # Optionally, close the connection (depends on spec)
    connection.close()


if __name__ == "__main__":
    main()
