"""
GUI. Чат
"""

from socket import *
from threading import *
from tkinter import *
from tkinter.ttk import *


def quit():
    """
    Функция выхода из чата
    """
    global window
    window.destroy()


def send_message():
    """
    Функция отправки сообщения
    """
    client_message = txt_combobox.get()
    txt_messages.insert(END, "\n" + "You: " + client_message)
    client_socket.send(client_message.encode("utf-8"))


def recv_message():
    """
    Ответ сервера
    :return:
    """
    while True:
        server_message = client_socket.recv(1024).decode("utf-8")
        print(server_message)
        txt_messages.insert(END, "\n" + server_message)


# Подключить клиента.
client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
hostIp = "127.0.0.1"
portNumber = 2004
client_socket.connect((hostIp, portNumber))

# Главное окно.
window = Tk()
window.title("Добрый чат: ")

# Текстовый блок для отображения написанного и ответа сервера
txt_messages = Text(window, font=f'Arial 12', wrap='word')
txt_messages.grid(row=0, column=0, padx=10, pady=10)

# Ввод текста.
txt_combobox = Combobox(window, width=100, values=['Привет', 'Как дела?', 'Который час?'])
txt_combobox.grid(row=1, column=0, padx=10, pady=10)

# Отправка сообщения.
btn_send_message = Button(window, text="Отправить", width=20, command=send_message)
btn_send_message.grid(row=2, column=0, padx=10, pady=10)

# Кнопка выхода
btn_quit = Button(window, text="Закрыть", width=20, command=quit)
btn_quit.grid(row=2, column=2, padx=20, pady=20)

recv_thread = Thread(target=recv_message)
recv_thread.daemon = True
recv_thread.start()

window.mainloop()
