# Simple Client-Server Communication

This is a basic Python implementation of client-server communication using sockets.

## Features

- Bidirectional communication between client and server
- Server can send messages to the client while the client can also send messages to the server
- Graceful termination of the connection by typing "quit"

## Usage

1. Run the server script (`server.py`) on the machine where you want to host the server.
2. Run the client script (`client.py`) on the machine where you want to connect as a client.
3. Follow the prompts in the client terminal to send and receive messages.

## Requirements

- Python 3.x

## Instructions

1. Clone this repository to your local machine.
2. Open two terminal windows.
3. In one terminal, navigate to the directory containing the `server.py` file.
4. Run the server script using the command: `python server.py`
5. In the other terminal, navigate to the directory containing the `client.py` file.
6. Run the client script using the command: `python client.py`
7. Follow the prompts in the client terminal to send and receive messages.

## Note

- Make sure to replace any placeholder values in the scripts (such as IP addresses and port numbers) with your actual server details before running.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
