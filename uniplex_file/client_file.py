import socket

with socket.socket() as client:
    client.connect(("localhost", 3456))

    try:
        with open("Internet.png", "rb") as log:
            client.sendfile(log)
    except KeyboardInterrupt:
        print("\nClient disconnected")

