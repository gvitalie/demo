import socket

if __name__ == "__main__":
    with socket.socket() as server:
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind(("localhost", 3456))
        server.listen()

        try:
            while True:
                client, address = server.accept()
                print(address, 'connected')
                with open("recv_Internet.png", "wb") as log:
                    while True:
                        data = client.recv(1024)
                        if not data:
                            break
                        print("+", flush=True, end="")
                        # print(data, flush=True, file=log)
                        log.write(data)
                    print('Done')
                    break
        except KeyboardInterrupt:
            print("\nServer down")
