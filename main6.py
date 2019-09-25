# pyrcc5 res.qrc -o res.py 资源整合命令

#   打包命令
#pyinstaller -F -w -i icon/icon.ico main5.py -p C:\\my\\python\\mypy37-32\\SRAN_Reading\\SRAN_Reading_Tool\\mod


from PyQt5 import QtWidgets
import sys
from untitled6 import Ui_MainWindow
from About import Ui_Dialog
# from PyQt5.QtWidgets import (QWidget, QToolTip,QDesktopWidget,QMessageBox,
#      QPushButton, QApplication,QFileDialog,QAction,QSplashScreen,QDialog)
from PyQt5.QtWidgets import (QWidget,QMessageBox,
      QApplication,QFileDialog,QSplashScreen,QDialog)
from PyQt5.QtGui import QIcon,QPixmap
from PyQt5.QtCore import Qt
# from private_fuction_lij import *
from checkbox_name import *
import datetime,time
import res
class childWindow(QDialog,Ui_Dialog):
    def __init__(self):
        # QDialog.__init__(self)
        # self.child=Ui_Dialog()
        super(childWindow, self).__init__()
        self.setupUi(self)
        # self.child.setupUi(self)
        self.setWindowIcon(QIcon(':icon/icon.ico'))
        self.label.setText("开发工具:\npython3.7\n\n"
                           "开发者:\nLi Jie & Zhang Cong\n\n"
                           "版本:\nSRAN Reading Tool v190925\n\n"
                           "我的邮箱:\njie.2.li@nokia-sbell.com\n\n"
                           "欢迎加我微信:")
        self.label_2.setPixmap(QPixmap(':icon/my-weixin.png'))
        self.label_2.setScaledContents(True)

class Mywindow(QtWidgets.QMainWindow, Ui_MainWindow):
    # 建立的是Main Window项目，故此处导入的是QMainWindow
    def __init__(self):
        super(Mywindow, self).__init__()
        self.setupUi(self)
        self.setWindowIcon(QIcon(':icon/icon.ico'))  # 设置窗体标题图标
        self.pushButton.setToolTip("点击选择XML文件")
        # self.pushButton.setIcon(QIcon('icon/I_like_buttons_024.png'))
        # self.pushButton.setStyleSheet("QPushButton{color:black}"
        #                               "QPushButton:hover{color:red}"
        #                               "QPushButton{background-color:lightgreen}"
        #                               "QPushButton{border:2px}"
        #                               "QPushButton{border-radius:10px}"
        #                               "QPushButton{padding:2px 4px}")
        # self.pushButton_2.setStyleSheet("QPushButton{color:black}"
        #                               "QPushButton:hover{color:red}"
        #                               "QPushButton{background-color:lightgreen}"
        #                               "QPushButton{border:2px}"
        #                               "QPushButton{border-radius:10px}"
        #                               "QPushButton{padding:2px 4px}")
        # self.pushButton.setStyleSheet("QPushButton{border-image: url(off.png)}"
        #                           "QPushButton:hover{border-image: url(on.png)}")
        # self.SELECT_ALL.setStyleSheet("QCheckBox{color:black}"
        #                                "QCheckBox:hover{color:red}"
        #                               "QCheckBox{background-color:lightgreen}"
        #                               "QCheckBox{border:2px}"
        #                               "QCheckBox{border-radius:10px}"
        #                               "QCheckBox{padding:2px 4px}"
        #                                )
        # self.setStyleSheet("QMainWindow{background-color:lightgreen}"
        #                               )
        # self.menu.setStyleSheet("QMenu{background-color:lightgreen}"
        #                    )
        # self.menubar.setStyleSheet("QMenuBar{background-color:light}"

                           # )
        # self.btn.clicked.connect(self.button_change)
        # self.actionopenfile.triggered.connect(self.btn_click)
        self.pushButton.clicked.connect(self.btn_click)
        self.pushButton.setStyleSheet("QPushButton{color:black}"
                                        "QPushButton{background-color:rgb(72,118,255)}")


        self.pushButton_2.clicked.connect(self.del_a)
        self.pushButton_2.setStyleSheet("QPushButton{color:black}"
                                      "QPushButton{background-color:rgb(72,118,255)}")


        # self.pushButton.clicked.connect(self.test1)
        # self.pushButton.clicked.connect(self.checkbox_state)
        self.splash = QSplashScreen(QPixmap(":icon/company_logo.jpg"))
        self.splash.show()
        self.splash.showMessage("正在加载......",color = Qt.white)

        time.sleep(1)
        self.splash.showMessage("稍等......",color = Qt.white)


        time.sleep(1)
        self.splash.finish(self)
        # QtWidgets.QApplication.processEvents()
        # self.splash = QSplashScreen(setMovie(QMovie('tt.gif')))
        # self.label.setPixmap(QPixmap('icon/off.png'))
        # self.gif = QMovie('icon/tt.gif')
        # self.label.setMovie(self.gif)
        # self.gif.start()

        self.SELECT_ALL.stateChanged.connect(self.SELECT_ALL_def)
        for xxx in checkbox_name:
            yyy = getattr(self, xxx)
            yyy.stateChanged.connect(self.SELECT)

        self.childWindow = childWindow()
        self.actiontest.triggered.connect(self.childWindow.show)

    def del_a(self):
        if self.SRAN.isChecked():
            import private_fuction_lij
            private_fuction_lij.del_all(self,checkbox_name)
        else:
            import private_fuction_tdd
            private_fuction_tdd.del_all(self,checkbox_name)



    def closeEvent(self, event):

        reply = QMessageBox.question(self, 'Message',
                                     "Are you sure to quit?", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def SELECT_ALL_def(self):
        if self.SELECT_ALL.checkState() == Qt.Checked:
            for xx in checkbox_name:
                temp = getattr(self, xx)
                temp.setChecked(True)
        elif self.SELECT_ALL.checkState() == Qt.Unchecked:
            for xx in checkbox_name:
                temp = getattr(self, xx)
                temp.setChecked(False)

    def SELECT(self):
        checkbox_state = []
        for xx_name in checkbox_name:
            temp = getattr(self, xx_name)
            if temp.checkState():  # checkbox.checkState():复选框是否被勾选的状态
                checkbox_state.append(1)
            else:
                checkbox_state.append(0)
        checkbox_state_sum = sum(checkbox_state)
        checkbox_state_len = len(checkbox_state)
        if checkbox_state_sum == checkbox_state_len:
            self.SELECT_ALL.setCheckState(Qt.Checked)
        elif checkbox_state_sum > 0 and checkbox_state_sum < checkbox_state_len:
            self.SELECT_ALL.setTristate()
            self.SELECT_ALL.setCheckState(Qt.PartiallyChecked)
        else:
            self.SELECT_ALL.setTristate(False)
            self.SELECT_ALL.setCheckState(Qt.Unchecked)


    def btn_click(self):
        # 选择XML文件
        file, _ = QFileDialog.getOpenFileName(self,
                                                          "选取文件",
                                                          "./",
                                                          "xml Files (*.xml);;ALL Files (*)")  # 设置文件扩展名过滤,注意用双分号间隔

        if file:
            # 定义XML的命名空间，xmlns的值，xmlns="raml20.xsd"

            xmlns = "{raml20.xsd}"
            # 开始计时
            # starttime = datetime.datetime.now()
            # 清空数据库
            # del_rs(self)
            # self.label.setPixmap(QPixmap('icon/on.png'))
            self.textBrowser.setText("")
            self.textBrowser.append("打开文件：" + file)
            QtWidgets.QApplication.processEvents()

            # 定义空列表
            # 有几个CLASS，下面要填几个中括号
            # 0:MRBTS,1:HW,2:GNSSE_R,3:GNSSE,4:GNBCF,5:GNCEL,6:GNCEL_R,7:LNBTS,8:LNCEL,9:LNCEL_FDD,10:NBIOT_FDD
            # 11:VLANIF,12:IPADDRESSV4,13:IPRT,14:MPLANENW,15:BBMOD_HW,16:SMOD_HW,17:RMOD_HW,18:BBMOD_R,19:SMOD_R
            # 20:RMOD_R,21:LNMME,22:CHANNEL,23:CARRIERGROUPC_R,24:MNL_R，25：CHANNELGROUP，26：SECADM，27：FEATCADM
            # 28：BBMOD_EQM,29:SMOD_EQM,30:RMOD_EQM,31:GNSSE_EQM
            # NODE_LIST = [[], [], [], [], [], [], [], [], [], [],
            #              [], [], [], [], [], [], [], [], [], [],
            #              [], [], [], [], [], [], [], [], [], [],
            #              [], []]


            if self.SRAN.isChecked():
                # from private_fuction_lij import *
                import private_fuction_lij
                NODE_LIST = list()
                checkbox_state = []
                for xx_name in checkbox_name:
                    temp = getattr(self, xx_name)
                    if temp.checkState():  # checkbox.checkState():复选框是否被勾选的状态
                        checkbox_state.append(1)
                    else:
                        checkbox_state.append(0)

                if sum(checkbox_state) != 0:
                    anniu_False(self)
                    private_fuction_lij.del_rs(self, checkbox_state)  # 清空数据库
                    starttime = datetime.datetime.now()  # 开始计时
                    self.textBrowser.append("开始读取XML....")
                    QtWidgets.QApplication.processEvents()
                    # print("开始读取XML....")
                    private_fuction_lij.read_XML_to_list(file, xmlns, NODE_LIST, checkbox_state)
                    # print("读取XML完成")
                    self.textBrowser.append("读取XML完成")
                    QtWidgets.QApplication.processEvents()
                    self.textBrowser.append("导入数据库....")
                    # print(NODE_LIST)
                    QtWidgets.QApplication.processEvents()
                    # print("导入数据库....")
                    private_fuction_lij.read_list_to_access(NODE_LIST, self)
                    # print("导入完成")
                    self.textBrowser.append("导入完成")
                    QtWidgets.QApplication.processEvents()
                    endtime = datetime.datetime.now()
                    # print("使用时间:", (endtime - starttime).seconds, "(秒)")

                    usetime = (endtime - starttime).seconds
                    # self.label.setPixmap(QPixmap('icon/off.png'))
                    self.textBrowser.append("使用时间:" + str(usetime) + "(秒)\n")
                    reply = QMessageBox.information(self,  # 使用infomation信息框
                                                    "完成提示",
                                                    "读取完成！",
                                                    QMessageBox.Yes)
                else:
                    reply = QMessageBox.warning(self, '未选择模块', '请选择模块！', QMessageBox.Yes)
                # self.pushButton.setEnabled(True)
                # self.pushButton_2.setEnabled(True)
                anniu_True(self)
                # print("ok1")

            if self.TDD.isChecked():

                # from private_fuction_lij import *
                import private_fuction_tdd
                NODE_LIST = list()
                checkbox_state = []
                for xx_name in checkbox_name:
                    temp = getattr(self, xx_name)
                    if temp.checkState():  # checkbox.checkState():复选框是否被勾选的状态
                        checkbox_state.append(1)
                    else:
                        checkbox_state.append(0)

                if sum(checkbox_state) != 0:
                    anniu_False(self)
                    private_fuction_tdd.del_rs(self, checkbox_state)  # 清空数据库
                    starttime = datetime.datetime.now()  # 开始计时
                    self.textBrowser.append("开始读取XML....")
                    QtWidgets.QApplication.processEvents()
                    # print("开始读取XML....")
                    private_fuction_tdd.read_XML_to_list(file, xmlns, NODE_LIST, checkbox_state)
                    # print("读取XML完成")
                    self.textBrowser.append("读取XML完成")
                    QtWidgets.QApplication.processEvents()
                    self.textBrowser.append("导入数据库....")
                    # print(NODE_LIST)
                    QtWidgets.QApplication.processEvents()
                    # print("导入数据库....")
                    private_fuction_tdd.read_list_to_access(NODE_LIST, self)
                    # print("导入完成")
                    self.textBrowser.append("导入完成")
                    QtWidgets.QApplication.processEvents()
                    endtime = datetime.datetime.now()
                    # print("使用时间:", (endtime - starttime).seconds, "(秒)")

                    usetime = (endtime - starttime).seconds
                    # self.label.setPixmap(QPixmap('icon/off.png'))
                    self.textBrowser.append("使用时间:" + str(usetime) + "(秒)\n")
                    reply = QMessageBox.information(self,  # 使用infomation信息框
                                                    "完成提示",
                                                    "读取完成！",
                                                    QMessageBox.Yes)
                else:
                    reply = QMessageBox.warning(self, '未选择模块', '请选择模块！', QMessageBox.Yes)
                # self.pushButton.setEnabled(True)
                # self.pushButton_2.setEnabled(True)
                anniu_True(self)			
                # print("ok2")

            # NODE_LIST = list()
            # checkbox_state = []
            # for xx_name in checkbox_name:
            #     temp = getattr(self, xx_name)
            #     if temp.checkState():  # checkbox.checkState():复选框是否被勾选的状态
            #         checkbox_state.append(1)
            #     else:
            #         checkbox_state.append(0)
            #
            # if sum(checkbox_state) != 0:
            #     anniu_False(self)
            #     del_rs(self,checkbox_state) # 清空数据库
            #     starttime = datetime.datetime.now()  # 开始计时
            #     self.textBrowser.append("开始读取XML....")
            #     QtWidgets.QApplication.processEvents()
            #     # print("开始读取XML....")
            #     read_XML_to_list(file, xmlns, NODE_LIST,checkbox_state)
            #     # print("读取XML完成")
            #     self.textBrowser.append("读取XML完成")
            #     QtWidgets.QApplication.processEvents()
            #     self.textBrowser.append("导入数据库....")
            #     # print(NODE_LIST)
            #     QtWidgets.QApplication.processEvents()
            #     # print("导入数据库....")
            #     read_list_to_access(NODE_LIST,self)
            #     # print("导入完成")
            #     self.textBrowser.append("导入完成")
            #     QtWidgets.QApplication.processEvents()
            #     endtime = datetime.datetime.now()
            #     # print("使用时间:", (endtime - starttime).seconds, "(秒)")
            #
            #     usetime  = (endtime - starttime).seconds
            #     # self.label.setPixmap(QPixmap('icon/off.png'))
            #     self.textBrowser.append("使用时间:" + str(usetime) + "(秒)\n")
            #     reply = QMessageBox.information(self,  # 使用infomation信息框
            #                                     "完成提示",
            #                                     "读取完成！",
            #                                     QMessageBox.Yes )
            # else:
            #     reply = QMessageBox.warning(self, '未选择模块', '请选择模块！', QMessageBox.Yes)
            # # self.pushButton.setEnabled(True)
            # # self.pushButton_2.setEnabled(True)
            # anniu_True(self)

def anniu_True(self):
    self.pushButton.setEnabled(True)
    self.pushButton_2.setEnabled(True)
    self.SELECT_ALL.setEnabled(True)
    for xx in checkbox_name:
        temp = getattr(self, xx)
        temp.setEnabled(True)

def anniu_False(self):
    self.pushButton.setEnabled(False)
    self.pushButton_2.setEnabled(False)
    self.SELECT_ALL.setEnabled(False)
    for xx in checkbox_name:
        temp = getattr(self, xx)
        temp.setEnabled(False)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Mywindow()


    # window.setStyleSheet(qss)


    window.show()
    sys.exit(app.exec_())

