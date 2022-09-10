"""
Серверная часть.
"""
import socket
import os
from _thread import *

ServerSideSocket = socket.socket()
host = '127.0.0.1'
port = 2004
ThreadCount = 0

# Подключиться
try:
    ServerSideSocket.bind((host, port))
except socket.error as e:
    print(str(e))
print('Socket is listening..')

# Слушать до 5 соединений
ServerSideSocket.listen(5)


def multi_threaded_client(connection):
    """
    Работа с клиентом
    """
    connection.send(str.encode('Server is working:'))
    while True:
        data = connection.recv(1024)  # Получить данные на сервере.
        print('Client said: ', data.decode('utf-8'))
        response = 'Server answered: ' + data.decode('utf-8')  # Ответ клиенту.
        # Если клиент выходит - он отправляет 'exit'
        if data.decode('utf-8') == 'exit':
            connection.sendall(b'client closed')
            break
        # Клиент может закрыть сервер - он отправляет 'server close'
        if data.decode('utf-8') == 'server close':
            connection.sendall(b'server closed')
            ServerSideSocket.close()
        connection.sendall(str.encode(response))
    # Закрыть соединение.
    connection.close()


while True:
    try:
        # Подключение нового клиента.
        Client, address = ServerSideSocket.accept()
        # Выводим IP и порт.
        print('Connected to: ' + address[0] + ':' + str(address[1]))
        # Новый поток для каждого клиента.
        start_new_thread(multi_threaded_client, (Client, ))
        # Посчитать потоки
        ThreadCount += 1
        print('Thread Number: ' + str(ThreadCount))
    # Если сервер закрыли раньше, и клиент стучится в уже закрытый сокет.
    except OSError:
        break

