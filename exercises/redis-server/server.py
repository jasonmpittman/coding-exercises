__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2025"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"
__difficuluty__ = ""

"""
Start: 8.08.25 6:30am, 8.09.25 6:50am, 8.11.25 6:55am
End:
Cycles: 3
"""

import asyncio

class RedisServer:
    def __init__(self):
        print('Starting Redis Server')

    async def handle_client(self, reader, writer):
        addr = writer.get_extra_info('peername')

        data_buffer = bytearray()
        while True:
            data = await reader.read(512)

            if not data:
                break

            data_buffer.extend(data)
        
        message = data_buffer.decode()
        print(f'Message received from {addr}: {message}')

        writer.write(data_buffer)
        await writer.drain()

        print(f'Closing connection with {addr}')
        writer.close()

    
    async def run(self):
        server = await asyncio.start_server(
            self.handle_client, '0.0.0.0', 6379
        )
        
        addr = server.sockets[0].getsockname()
        print(f'Redis available on {addr}')

        async with server:
            await server.serve_forever()



if __name__ == "__main__":
    redis = RedisServer()
    asyncio.run(redis.run())