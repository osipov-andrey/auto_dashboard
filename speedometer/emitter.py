import socket

HOST, PORT = "localhost", 8083


if __name__ == '__main__':
    while True:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.connect((HOST, PORT))
            data = input()
            sock.send(bytes(data + "\n", "utf-8"))
            received = str(sock.recv(1024), "utf-8")

            print("Sent:     {}".format(data))
            print("Received: {}".format(received))
