import socket
import threading
import socketserver


class ThreadedTCPRequestHandler(socketserver.BaseRequestHandler):
    """Класс Обработчика клиентских запросов"""

    def handle(self):
        data = str(self.request.recv(1024), 'ascii')
        cur_thread = threading.current_thread()
        response = bytes(f"{cur_thread.name}: {data}", 'ascii')
        self.request.sendall(response)


class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    """
    Класс асинхронного сервера
    """
    pass


def client(ip, port, message):
    """Функция клиента"""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((ip, port))
        sock.sendall(bytes(message, 'ascii'))
        response = str(sock.recv(1024), 'ascii')
        print(f"Принято: {response}")


# создаем сервер асинхронный сервер
server = ThreadedTCPServer(('localhost', 12345), ThreadedTCPRequestHandler)

# Запускаем поток с сервером - этот поток затем
# запустит еще один поток для каждого запроса
server_thread = threading.Thread(target=server.serve_forever)
# Выйдем из потока сервера, когда основной поток завершится
server_thread.daemon = True
server_thread.start()
print("Серверный цикл, работающий в потоке:", server_thread.name)

