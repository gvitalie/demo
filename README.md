# Experiments using Python socket.

**Goals:**  
- [x] read text message and send over socket
- [x] read microphone audio and send over socket  
- [x] read webcam video and send over socket  

**Desired types of communication:**  
- [x] uniplex  
- [x] duplex  
- [x] multiplex  

**Bibliography:**

Inter Thread communication in Python - Dot Net Tutorials  
https://dotnettutorials.net/lesson/inter-thread-communication-in-python/

Python | Communicating Between Threads | Set-1 - GeeksforGeeks  
https://www.geeksforgeeks.org/python-communicating-between-threads-set-1/


# Paradigm

```Python
me@amadeus:~$ python3 -q
>>> 
>>> import math
>>> 
>>> def exp(x):
...     a = 0
...     for i in range(100):
...             a = a + (x ** i) / math.factorial(i)
...     return a
... 
>>> def ln(x):
...     a = 0
...     for i in range(100):
...             a = a + 2 * (x - exp(a)) / (x + exp(a))
...     return a
... 
>>> def root(x, k):
...     a = 2
...     for i in range(100):
...             a = a - (a ** k - x) / (k * a ** (k - 1))
...     return a
... 
>>> 2 ** (1/2)
1.4142135623730951
>>> exp(1/2 * ln(2))
1.4142135623730956
>>> root(2, 2)
1.414213562373095
>>> 
>>> exp(1.23 * ln(3.21))
4.197601340269557
>>> exp(1/1.23 * ln(4.197601340269557))
3.2100000000000004
>>> ln(4.197601340269557)/ln(3.21)
1.23
>>> 
>>> # &•
>>> 
me@amadeus:~$ 
```