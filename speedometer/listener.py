import socketserver


class SpeedTCPListener(socketserver.BaseRequestHandler):
    """
    The request handler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """
    _speedometer = None

    @classmethod
    def set_speedometer(cls, speedometer):
        cls._speedometer = speedometer

    def handle(self):
        # self.request is the TCP socket connected to the client
        data = self.request.recv(1024).strip()
        print("{} wrote:".format(self.client_address[0]))
        print(data)

        try:
            speed_angle = int(data.decode())
            response = f"Send \"{speed_angle}\" to the speedometer..."
            self._speedometer.change_speed(speed_angle)
            self.request.sendall(response.encode())
        except ValueError as err:
            response = "Wrong data format!"
            self.request.sendall(response.encode())
            raise err


def run_listener():
    HOST, PORT = "localhost", 8083

    # Create the server, binding to localhost on port 9999
    with socketserver.TCPServer((HOST, PORT), SpeedTCPListener) as server:
        # Activate the server; this will keep running until you
        # interrupt the program with Ctrl-C
        try:
            server.serve_forever()
        except Exception as err:
            server.shutdown()
            raise err
