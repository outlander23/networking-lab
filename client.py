import socket
import threading

def receive_messages(client_socket):
    while True:
        try:
            data = client_socket.recv(1024).decode('utf-8')
            if not data or data.lower() == 'quit':
                print("Server closed the connection")
                break
            print(f"Received message from server: {data}")
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

print("Enter the server IP address:")
server_host = input()

print("Enter the server port number:")
server_port = int(input())

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((server_host, server_port))

# Start a thread to receive messages from the server
receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
receive_thread.start()

# Start a thread to send messages to the server
send_thread = threading.Thread(target=send_messages, args=(client_socket,))
send_thread.start()

# Wait for both threads to finish
receive_thread.join()
send_thread.join()

client_socket.close()
