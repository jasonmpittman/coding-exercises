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
    def __init__(self, ip='localhost', port=6379):
        self.ip = ip
        self.port = port
        self.socket = None

    def _send_command(self, command, *args):
        """
        Constructs the RESP array for the command

        command (str):
        *args :
        """
        command_parts = [command] + list(args)
        resp_array = f"*{len(command_parts)}\r\n"

        for part in command_parts:
            part_bytes = str(part).encode('utf-8')
            resp_array += f"${len(part_bytes)}\r\n{part_bytes.decode('utf-8')}\r\n"

        self.socket.sendall(resp_array.encode('utf-8'))

    def _read_response(self):
        pass

    def set(self, key, value):
        """ SET key value"""
        self._send_command("SET", key, value)

    def get(self, get):
        pass

    def connect(self, ip="localhost", port=6379):
        """ 
        Establish a IPv4 TCP connection to target redis server.

        Args:
            ip (str): The IPv4 address of the redis server. The default is localhost.
            port (int): The TCP port of the redis server. The default is 6379.
        """
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((self.ip, self.port))


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
        client = RedisClient(ip=args.ip, port=args.port)
        client.connect()
    elif args.ip != None and args.port == None:
        client = RedisClient(ip=args.ip)
        client.connect()
    elif args.ip == None and args.ip != None:
        client = RedisClient(port=args.port)
        client.connect()
    else:
        client = RedisClient()
        client.connect()

    if args.action == 'SET':
        value = input('Enter KEY,VALUE: ')
        msg_key, msg_value = value.split(',')
        set_response = client.set(msg_key, msg_value)
