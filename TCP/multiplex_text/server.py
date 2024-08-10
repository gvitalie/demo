import socket
import threading


def clients_message(client, clients, message):
    for client_id in clients:
        # if client_id != client:
        client_id.send(message.encode("utf-8"))


def client_recv_message(client, address, clients):
    connected = f"+ {address[0]}:{address[1]}"
    print(connected)
    clients_message(client, clients, connected)
    while True:
        data = client.recv(1024)
        if not data:
            disconnected = f"- {address[0]}:{address[1]}"
            print(disconnected)
            clients.remove(client)
            clients_message(client, clients, disconnected)
            break
        message = f"{address[0]}:{address[1]} #> " + data.decode("utf-8")
        print(message)
        clients_message(client, clients, message)


if __name__ == "__main__":

    SERVER_HOST = "192.168.1.2"
    SERVER_PORT = 3456

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind((SERVER_HOST, SERVER_PORT))
        server.listen()
        server_ip, server_port = server.getsockname()
        print(f"Server {server_ip}:{server_port} started\n")
        clients = list()
        while True:
            try:
                client, address = server.accept()
                clients.append(client)
                client_recv_thread = threading.Thread(target=client_recv_message,
                                                      args=[client, address, clients])
                client_recv_thread.daemon = True
                client_recv_thread.start()
            except KeyboardInterrupt:
                print(f"\nServer {server_ip}:{server_port} shutdown")
                break
