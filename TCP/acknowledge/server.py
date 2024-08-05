import socket
from datetime import datetime

SERVER = ('localhost', 3456)

if __name__ == "__main__":
    with socket.socket() as server:
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind(SERVER)
        server.listen()
        print('Server listening\n')

        client = server.accept()
        print(f'{client[1]} connected')

        try:
            while True:
                time_is = datetime.now().time()
                message = f'Hello {time_is}'
                length = client[0].send(message.encode('utf-8'))
                print(f'Send {message} of length: {length}')
                acknowledge = client[0].recv(1024)
                if not acknowledge:
                    break
                print('acknowledge:', acknowledge.decode('utf-8'))
        except KeyboardInterrupt:
            pass
        finally:
            print('\nServer down')
