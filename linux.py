#! /usr/bin/env python3
import socket

import threading

from simple import *

from PyQt5.QtWidgets import QApplication, QMainWindow

from multiprocessing import Process

HOST = "192.168.2.5"
PORT = 65432

def socket_start():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    read_thread = ReadFromConnThread(s)
    read_thread.daemon = True
    read_thread.start()
    print("hello"+"have sent")
    s.sendall("hello".encode("utf-8"))
    s.close()


class ReadFromConnThread(threading.Thread):
    def __init__(self, conn):
        super().__init__()
        self.conn = conn

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

        s = event.windowPos()
        self.setMouseTracking(True)
        self.ui.label.setText('X:' + str(s.x()))
        self.ui.label_2.setText('Y:' + str(s.y()))
        if s.x() > 300 and flag_lr == False:
            print("发射")
            socket_start()
            flag_lr = True
        elif s.x() >= 300:
            pass
        elif s.x() <= 100:
            flag_lr = False


def window_start():
    app = QApplication([])
    mainw = MainWindow()
    mainw.show()
    app.exec_()


if __name__ == '__main__':

    t2 = Process(target=window_start)
    t2.start()