import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from functools import partial
import Ui_dome_1
import time

# def convert(ui):
#     input = ui.lineEdit.text()
#     result = float(input) * 6.7
#     ui.lineEdit_2.setText(str(result))
# 获取当前时间
def newtime(self):
    time_1 = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    #print("打印的时间：",time_1)
    self.label_2.setText(str(time_1))
    self.lineEdit.setText("")
    self.lineEdit_2.setText("")
    self.lineEdit_3.setText("")
    self.lineEdit_4.setText(str(time_1))


# 将输入的时间戳，转换为时间
def time_conersion(self):
    try:
        var_1 = int(self.lineEdit.text())
        time_2 = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(var_1/1000))
        self.lineEdit_2.setText(str(time_2))
    except:
        print("输入错误的时间戳")

# 将输入的时间，转换为时间戳
def time_conersion1(self):
    try:
        var_3 = self.lineEdit_4.text()
        print(type(var_3))
        time_3 = time.strptime(var_3, "%Y-%m-%d %H:%M:%S")
        newStamp = int(time.mktime(time_3))*1000
        self.lineEdit_3.setText(str(newStamp))
    except:
        print("输入了错误的时间")

def No_1_index(self):
    # 刷新按钮
    self.pushButton_5.clicked.connect(partial(newtime, self))



    # 获取时间戳，点击转换
    self.pushButton_2.clicked.connect(partial(time_conersion,self))


    # 获取时间，点击转换
    self.pushButton_4.clicked.connect(partial(time_conersion1,self))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_dome_1.Ui_MainWindow()
    #newtime(ui)
    #ui.pushButton.clicked.connect(partial(convert,ui))
    ui.setupUi(MainWindow)
    MainWindow.show()
    newtime(ui)
    # 所有函数体的内容
    No_1_index(ui)
    sys.exit(app.exec_())