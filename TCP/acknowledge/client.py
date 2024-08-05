import socket
from time import sleep
from random import randint

SERVER = ('localhost', 3456)

if __name__ == "__main__":
    with socket.socket() as client:
        client.connect(SERVER)
        print(f'Client {client.getsockname()} connected\n')

        try:
            while True:
                message = client.recv(1024)
                if not message:
                    break
                print('Received:', message.decode('utf-8'))
                acknowledge = randint(0, 9)
                print('acknowledge', acknowledge)
                sleep(acknowledge)
                client.send(str(acknowledge).encode('utf-8'))
        except KeyboardInterrupt:
            pass
        finally:
            print(f'Client {client.getsockname()} disconnected')
