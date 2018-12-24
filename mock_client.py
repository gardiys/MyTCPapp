import asyncio
from Messenger import Messenger
from DataStream import DataStream


class EchoClientProtocol(asyncio.Protocol):
    def __init__(self, loop):
        self.message = b"Hi everyone!"
        self.loop = loop
        self.messenger = Messenger()

    def connection_made(self, transport):
        stream = DataStream()
        stream.write_uint16(1)
        stream.write_string_unicode(b"admin")
        stream.write_string_unicode(b"123")
        send_data = stream.send()
        transport.write(send_data)
        print('Data sent: {!r}'.format(send_data))

    def data_received(self, data):
        print('Data received: {!r}'.format(data.decode()))

    def connection_lost(self, exc):
        print('The server closed the connection')
        print('Stop the event loop')
        self.loop.stop()


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    coro = loop.create_connection(lambda: EchoClientProtocol(loop),
                                  '127.0.0.1', 8888)
    loop.run_until_complete(coro)
    loop.run_forever()
    loop.close()
