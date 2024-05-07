import socket
import threading

def receive_messages(client_socket):
    while True:
        try:
            data = client_socket.recv(1024).decode('utf-8')
            if not data or data.lower() == 'quit':
                print("Client closed the connection")
                break
            print(f"Received message from client: {data}")
        except Exception as e:
            print(f"Error receiving message: {e}")
            break

def send_messages(client_socket):
    while True:
        try:
            msg = input("Enter message to send: ")
            client_socket.send(msg.encode('utf-8'))
            if msg.lower() == 'quit':
                break
        except Exception as e:
            print(f"Error sending message: {e}")
            break

host = '0.0.0.0'
port = 5000

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))
server_socket.listen(1)  # Listen for only one client

print(f"Server is running on {host}:{port}")

client_socket, client_address = server_socket.accept()
print(f"Connection established with {client_address}")

# Start a thread to receive messages from the client
receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
receive_thread.start()

# Start a thread to send messages to the client
send_thread = threading.Thread(target=send_messages, args=(client_socket,))
send_thread.start()

# Wait for both threads to finish
receive_thread.join()
send_thread.join()

client_socket.close()
server_socket.close()


