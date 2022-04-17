from simple import *

from PyQt5.QtWidgets import QApplication, QMainWindow

from multiprocessing import Process

import socket

import threading

lock = threading.RLock()

HOST = "192.168.2.5"

PORT = 65432

content = 'hello'

class ReadFromConnThread(threading.Thread):
    def __init__(self, conn):
        super().__init__()
        self.conn = conn

    def run(self):
        try:
            while True:
                contents = self.conn.recv(1024)
                print(f"\n({HOST}:{PORT}): {contents.decode('utf-8')}\n", end="")
        except Exception:
            pass

def socket_start():
    global content
    print(str(id(content))+"--1")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    read_thread = ReadFromConnThread(s)
    read_thread.daemon = True
    read_thread.start()
    while True:
        print(str(id(content))+"--2")
        for i in range(1000000000):
            a=0
        while content == "wuhu":
            s.sendall(content.encode("utf-8"))
            lock.acquire()
            content = 'pass'
            lock.release()
    s.close()


flag_lr = False  # left is False right is True


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        # 使用ui文件导入定义界面类
        self.ui = Ui_MainWindow()
        # 初始化界面
        self.ui.setupUi(self)

    def mouseMoveEvent(self, event):
        global flag_lr
        global content

        print(str(id(content))+ "--3")
        s = event.windowPos()
        self.setMouseTracking(True)
        self.ui.label.setText('X:' + str(s.x()))
        self.ui.label_2.setText('Y:' + str(s.y()))
        if s.x() > 300 and flag_lr == False:
            range(1000000000)
            print("发射")
            lock.acquire()
            content = 'wuhu'
            print(str(id(content))+"--4")
            lock.release()
            flag_lr = True
        elif s.x() >= 300:
            lock.acquire()
            content = 'wuhu'
            lock.release()
            pass
        elif s.x() <= 100:
            lock.acquire()
            content = 'pass'
            lock.release()
            flag_lr = False


def window_start():
    app = QApplication([])
    mainw = MainWindow()
    mainw.show()
    app.exec_()


if __name__ == '__main__':
    #global content
    t2 = Process(target=window_start)
    t1 = Process(target=socket_start)
    t2.start()
    t1.start()