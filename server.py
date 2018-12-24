import asyncio
from receiver import Receiver
from action import Action
import actions


class IncorrectTypeOfDataException(Exception):
    pass

to_do_actions = {
    1: [
        actions.check_in_database
    ],
    5: [
        actions.send_message_to_everyone
    ]
}
class EchoServerClientProtocol(asyncio.Protocol):
    """Async server"""

    peers = set()

    def __init__(self):
        super().__init__()

        self._buffer = b''
        self.reciver = Receiver
        self.actions = Action

    def process_data(self, data):
        """Prosessing incoming data"""
        package = self.reciver(data).decode()
        if package is not None:
            if package.id in to_do_actions:
                for func in to_do_actions[package.id]:
                    func(package, self.transport, self.peers)

    def connection_made(self, transport):
        self.peername = transport.get_extra_info("peername")
        print(f"Connection from {self.peername}")
        self.transport = transport
        self.peers.add((self.peername, self.transport))

    def data_received(self, data):
        self._buffer += data
        try:
            decoded_data = self._buffer
        except UnicodeDecodeError:
            return

        self._buffer = b''

        print(f"Data received: {decoded_data}")

        try:
            self.process_data(decoded_data)
            #self.transport.write(resp)

        except IncorrectTypeOfDataException as err:
            self.transport.write(f"error: {err}".encode())
            return

    def connection_lost(self, exc):
        self.peers.discard((self.peername,self.transport))
        print(self.peername, "has left server")


def run_server(host, port):
    loop = asyncio.get_event_loop()
    coro = loop.create_server(
        EchoServerClientProtocol, host, port
    )
    server = loop.run_until_complete(coro)
    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass

    server.close()
    loop.run_until_complete(server.wait_closed())
    loop.close()


if __name__ == "__main__":
    host = '127.0.0.1' #socket.gethostbyname(socket.gethostname())
    port = 8888
    run_server(host, port)

