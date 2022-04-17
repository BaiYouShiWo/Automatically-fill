#! /usr/bin/env python3
import socket
import threading
import time

HOST = "192.168.2.5"
PORT = 65432

lock = threading.Lock()
# lock.acquire()  # 开始给线程加锁
# client.lock.release()  # 给线程解锁
def change(x):
    global content
    lock.acquire()
    content =x
    print(x)
    print(content+"change")

    lock.release()
def start():
    global content
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    read_thread = ReadFromConnThread(s)
    read_thread.daemon = True
    read_thread.start()
    while True:
        print(content)
        for i in range(10000000):
            a=0
        if content != "pass":
            print(content+"have sent")
            s.sendall(content.encode("utf-8"))

    s.close()

class ReadFromConnThread(threading.Thread):
    def __init__(self, conn):
        super().__init__()
        self.conn = conn
# if __name__ == "__main__":
#     s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     s.connect((HOST, PORT))
#     read_thread = ReadFromConnThread(s)
#     read_thread.daemon = True
#
#     while True:
#         content = input("YOUR:")
#         if content == "quit":
#             break
#         s.sendall(content.encode("utf-8"))
#     s.close()