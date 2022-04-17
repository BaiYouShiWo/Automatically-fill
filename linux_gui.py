from simple import *

from PyQt5.QtWidgets import QApplication, QMainWindow,QMessageBox,QLabel

import sys

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        # 使用ui文件导入定义界面类
        self.ui = Ui_MainWindow()
        # 初始化界面
        self.ui.setupUi(self)
        # 使用界面定义的控件，也是从ui里面访问
        self.ui.textBrowser.setText('Have changed')
    def mouseMoveEvent(self,event):
        s = event.windowPos()
        #self.setMouseTracking(True)
        self.ui.textBrowser.setText('X:' + str(s.x()))
        self.ui.textBrowser_2.setText('Y:' + str(s.y()))


if __name__ == '__main__':
    app = QApplication([])
    mainw = MainWindow()
    mainw.show()
    app.exec_()