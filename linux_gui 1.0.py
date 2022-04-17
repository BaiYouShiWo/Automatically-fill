from simple import *

from PyQt5.QtWidgets import QApplication, QMainWindow

from multiprocessing import Process

import client

client.content='pass'
flag_lr=False#left is False right is True

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        # 使用ui文件导入定义界面类
        self.ui = Ui_MainWindow()
        # 初始化界面
        self.ui.setupUi(self)

    def mouseMoveEvent(self,event):
        global flag_lr
        s = event.windowPos()
        self.setMouseTracking(True)
        self.ui.label.setText('X:' + str(s.x()))
        self.ui.label_2.setText('Y:' + str(s.y()))

        if s.x() >300 and flag_lr == False:
            print("发射")
            client.change('wuhu')
            flag_lr = True
        elif s.x() >= 300 :
            client.change('wuhu')
            pass
        elif s.x() <= 100:
            client.change('pass')
            flag_lr = False
def hello():
    app = QApplication([])
    mainw = MainWindow()
    mainw.show()
    app.exec_()

if __name__ == '__main__':
    t1 = Process(target=client.start)
    t1.start()
    hello()