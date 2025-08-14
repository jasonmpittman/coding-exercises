__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2025"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"
__difficuluty__ = ""

"""
Start: 8.10.25 7:10am, 8.12.25 9:55am, 8.13.25 7:00am, 8.14.25 3:25am
End:
Cycles: 3
"""
import argparse
import socket

class RedisClient:

    def set(self, key, value, *args):
        """ SET key value"""
        pass

    def get(self, get):
        pass

    def connect(self, ip, port):
        """ """
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((ip, port))


    def disconnect(self):
        """ """
        self.sock.close()




if __name__ == "__main__":

    args_parser = argparse.ArgumentParser(description='A simple Redis client')

    args_parser.add_argument('--ip', '-i', help='The IP address you want to connect with. Default is localhost')
    args_parser.add_argument('--port', '-p', type=int, help='The port the host listens on. Default is 6379')
    args_parser.add_argument('--action', '-a', help='The action to take once connected. Options are SET, GET')

    args = args_parser.parse_args()

    print(args)

    if args.ip != None and args.port != None:
        client = RedisClient()
        client.connect(ip=args.ip, port=args.port)
    elif args.ip != None and args.port == None:
        client = RedisClient()
        client.connect(ip=args.ip)
    elif args.ip == None and args.ip != None:
        client = RedisClient()
        client.connect(port=args.port)
    else:
        client = RedisClient()

    if args.action == 'SET':
        value = input('Enter KEY,VALUE: ')
        msg_key, msg_value = value.split(',')
        print(f'{msg_key} holds {msg_value}')
