import socket
import subprocess
import threading
import psutil
from time import sleep


def client_recv_message(client):

    chat = subprocess.Popen(["xterm"])
    process = psutil.Process(chat.pid)
    sleep(0.5)
    xterm_pid = psutil.Process(process.pid).children()[0].pid
    xterm_tty = psutil.Process(xterm_pid).terminal()

    with open(xterm_tty, 'w') as log:
        while True:
            data = client.recv(1024)
            if not data:
                break
            print(data.decode("utf-8"), flush=True, file=log)
    chat.terminate()


if __name__ == "__main__":

    SERVER_HOST = "amadeus"
    SERVER_PORT = 3456

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        try:
            client.connect((SERVER_HOST, SERVER_PORT))
            server_ip, server_port = client.getpeername()
            client_ip, client_port = client.getsockname()
            print(f"Connected to {server_ip}:{server_port}")

            client_recv_thread = threading.Thread(target=client_recv_message,
                                                  args=[client])
            client_recv_thread.daemon = True
            client_recv_thread.start()

            while True:
                try:
                    user_input = str(input(f"{client_ip}:{client_port} #> "))
                    client.send(user_input.encode("utf-8"))
                except KeyboardInterrupt:
                    print(f"\nDisconnected from {server_ip}:{server_port}")
                    break
        except Exception as e:
            print(e, "-> Server or network may be down")
