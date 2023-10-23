import socket
import datetime

# Define the host and port for the server
host = '0.0.0.0'
port = 12345

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the host and port
server_socket.bind((host, port))

# Listen for incoming connections
server_socket.listen(5)

print(f"Server is listening on {host}:{port}")

while True:
    # Accept a connection from a client
    client_socket, addr = server_socket.accept()
    
    # Get the IP address of the host
    host_ip = socket.gethostbyname(socket.gethostname())

    print(f"Accepted connection from {addr}")

    # Get the current date and time
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Create an HTML response with the date and time
    html_response = f"""\
<!DOCTYPE html>
<html>
<head>
    <title>Current Date and Time</title>
</head>
<body>
    <h1>Current Date and Time</h1>
    <p>Current Time: {current_time}</p>
    <p>Client IP: {host_ip}</p>
</body>
</html>
"""
    # Send the HTML response to the client
    response = f"HTTP/1.1 200 OK\r\nContent-Length: {len(html_response)}\r\n\r\n{html_response}"
    client_socket.send(response.encode())
    # Close the client socket
    client_socket.close()

