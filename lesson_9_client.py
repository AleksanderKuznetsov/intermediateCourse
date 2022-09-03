from lesson_9_server import client
import time

for i in range(50):
    client('127.0.0.1', 12345, 'Hello!')
