__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2025"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"
__difficuluty__ = ""

"""
Start: 8.10.25 7:10am, 8.12.25 9:55am, 8.13.25 7:00am
End:
Cycles: 3
"""
import argparse
import socket

class RedisClient:
    def __init__(self, host='localhost', port=6379):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        try:
            self.sock.connect((host, port))
        except Exception as e:
            print(f'There was an error connecting to host: {e}')

    def _encode_resp(self, value):
        encoded_value = value.encode('utf-8')
        return f"${len(encoded_value)}\r\n{encoded_value.decode('latin-1')}\r\n"

    def _decode_resp(self):
        pass

    def set(self):
        pass

    def get(self):
        pass

    def close(self):
        self.sock.close()




if __name__ == "__main__":

    args_parser = argparse.ArgumentParser(description='A simple Redis client')

    args_parser.add_argument('--ip', '-i', help='The IP address you want to connect with. Default is localhost')
    args_parser.add_argument('--port', '-p', type=int, help='The port the host listens on. Default is 6379')
    args_parser.add_argument('--action', '-a', help='The action to take once connected. Options are SET, GET')

    args = args_parser.parse_args()

    print(args)

    if args.ip != None and args.port != None:
        client = RedisClient(host=args.ip, port=args.port)
    elif args.ip != None and args.port == None:
        client = RedisClient(host=args.ip)
    elif args.ip == None and args.ip != None:
        client = RedisClient(port=args.port)
    else:
        client = RedisClient()

    if args.action == 'SET':
        value = input('Enter KEY,VALUE: ')
        msg = client._encode_resp(value)
        print(f'{msg}')
