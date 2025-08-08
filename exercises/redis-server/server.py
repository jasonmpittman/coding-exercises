__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2025"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"
__difficuluty__ = ""

import socket

class Redis:
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_address = ('0.0.0.0', 6379)
        self.sock.bind(self.server_address)

    def run(self):
        self.sock.listen(1)

        while True:
            print(f'Waiting for a connection')
            connection, client_address = self.sock.accept()

            try:
                print(f'Connection from {client_address}')
                data = connection.recv(16)

            except Exception as e:
                print(f'An error occured: {e}')
            finally:
                connection.close()




if __name__ == "__main__":
    redis = Redis()
    redis.run()