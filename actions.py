from storage import Store
from packages.S4ResponseMessage import ResponseMessage
from DataStream import DataStream
from user import User


STORAGE = Store()


#Authorization
def check_in_database(package, transport, peers):
    if STORAGE.already_exist(package.id):
        #пустить на сервер
        peers.add(User(STORAGE.get_item()))
        resp = ResponseMessage(DataStream(), 20, "Success")
        resp.write_stream()
        transport.write(resp.response)
    else:
        resp = ResponseMessage(DataStream(), 30, "Wrong login or password")
        resp.write_stream()
        transport.write(resp.response)


#Message

def send_message_to_everyone(package, transport, peers):
    for peer in peers:
        peer[1].write(package.message)

