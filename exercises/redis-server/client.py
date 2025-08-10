__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2025"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"
__difficuluty__ = ""

"""
Start: 8.10.25 7:10am
End:
Cycles: 1
"""
import socket
import sys

class RedisClient:
    def __init__(self, host='localhost', port=6389):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        try:
            self.sock.connect((host, port))
        except Exception as e:
            print(f'There was an error connecting to host: {e}')
    
    def set(self):
        pass

    def get(self):
        pass

    def close(self):
        self.sock.close()




if __name__ == "__main__":
    host = sys.argv[1]
    port = int(sys.argv[2])

    client = RedisClient(host, port)
