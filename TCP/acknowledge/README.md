To do: describe ACKNOWLEDGE example.

```Python
/home/me/PycharmProjects/demo/.venv/bin/python /home/me/PycharmProjects/demo/TCP/acknowledge/server.py 
Server listening

('127.0.0.1', 45618) connected
Send Hello 05:25:32.137244 of length: 21
acknowledge: 8
Send Hello 05:25:40.144510 of length: 21
acknowledge: 9
Send Hello 05:25:49.150520 of length: 21
acknowledge: 9
Send Hello 05:25:58.158718 of length: 21

Server down

Process finished with exit code 0
```

```Python
/home/me/PycharmProjects/demo/.venv/bin/python /home/me/PycharmProjects/demo/TCP/acknowledge/client.py 
Client ('127.0.0.1', 45618) connected

Received: Hello 05:25:32.137244
acknowledge 8
Received: Hello 05:25:40.144510
acknowledge 9
Received: Hello 05:25:49.150520
acknowledge 9
Received: Hello 05:25:58.158718
acknowledge 6
Client ('127.0.0.1', 45618) disconnected

Process finished with exit code 0
```