import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QWidget,QFileDialog
from Ui_untitled import Ui_MainWindow
from Ui_ChildrenForm2 import Ui_ChildrenForm

class MainForm(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(MainForm,self).__init__()
        self.setupUi(self)

        self.child = ChildrenForm()



        self.fileCloseAction.triggered.connect(self.close)
        self.fileOpenAction.triggered.connect(self.openMenu)
        self.addWinAction.triggered.connect(self.childShow)



    # 打开文件窗口
    def openMenu(self):
        file,ok = QFileDialog.getOpenFileName(self,"打开","C:/","All Files(*);;Text Files (*.txt)")
        self.statusbar.showMessage(file)

    # 添加子窗口
    def childShow(self):
        self.MaingridLayout.addWidget(self.child)
        self.child.show()
        self.status = self.statusBar()
        self.status.showMessage("响应成功",3000)


class ChildrenForm(QMainWindow,Ui_ChildrenForm):
    def __init__(self):
        super(ChildrenForm,self).__init__()
        self.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainForm()
    window.show()
    sys.exit(app.exec_())