import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QWidget,QFileDialog
from Ui_CaiDan_1 import Ui_Form
from Ui_CaiDan_2 import Ui_Form2
from Ui_main_index import Ui_MainWindow
from time_PY import time_index

class MainForm(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(MainForm,self).__init__()
        self.setupUi(self)
        # 实例化菜单1
        self.CaiDan = CaiDan_1()
        self.action.triggered.connect(self.addmenu_1)

        # !实例化菜单2
        # self.CaiDan2 = CaiDan_2()
        # self.actionjson.triggered.connect(self.addmenu_2)


    def addmenu_1(self):
        self.MaingridLayout.addWidget(self.CaiDan)
        self.CaiDan.show()
        self.status = self.statusBar()
        self.status.showMessage("成功跳转菜单1",3000)
    # def addmenu_2(self):
    #     self.MaingridLayout.addWidget(self.CaiDan2)
    #     self.CaiDan2.show()
    #     self.status = self.statusBar()
    #     self.status.showMessage("成功跳转菜单2",3000)  
        
        pass
class CaiDan_1(QWidget,Ui_Form):
    def __init__(self):
        super(CaiDan_1,self).__init__()
        self.setupUi(self)
        time_index.newtime(self)
        time_index.No_1_index(self)

class CaiDan_2(QWidget,Ui_Form2):
    def __init__(self):
        super(CaiDan_2,self).__init__()
        self.setupUi(self)
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainForm()
    window.show()
    sys.exit(app.exec_())