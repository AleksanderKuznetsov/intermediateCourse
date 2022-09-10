"""
Клиентская часть
"""
import socket
import time

ClientMultiSocket = socket.socket()
host = '127.0.0.1'
port = 2004

print('Waiting for connection response')

# Подключиться.
try:
    ClientMultiSocket.connect((host, port))
except socket.error as e:
    print(str(e))

# Получить данные.
res = ClientMultiSocket.recv(1024)

# Проверить мультипоточность.
for i in range(50):
    ClientMultiSocket.send(str.encode(str(i)))
    res = ClientMultiSocket.recv(1024)
    print(res.decode('utf-8'))
    time.sleep(0.2)

while True:
    try:
        Input = input('Hey there: ') # Вводим разную информацию
        ClientMultiSocket.send(str.encode(Input))
        # Получаем ответ сервера.
        res = ClientMultiSocket.recv(1024)
        # Выводим ответ сервера.
        print(res.decode('utf-8'))
        # Если клиент закрыл соединение или сокет.
        if res.decode('utf-8') == 'client closed' or res.decode('utf-8') == 'server closed':
            ClientMultiSocket.close()
            break
    # Если клиент постучался в закрытый сокет.
    except ConnectionResetError:
        print('Sorry, but server is closed')
        ClientMultiSocket.close()


