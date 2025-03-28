# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\manager.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(951, 665)
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(0, 0, 951, 671))
        self.frame.setStyleSheet("  background-color: transparent;\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tabWidget = QtWidgets.QTabWidget(self.frame)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setStyleSheet("QWidget#tab{border-image: url(:/img/img/Desktop_-_4.png);}\n"
"")
        self.tab.setObjectName("tab")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_3.setGeometry(QtCore.QRect(550, 270, 271, 41))
        self.lineEdit_3.setStyleSheet("font: 20 10pt \"阿里妈妈方圆体 VF Light\";\n"
"color:#000000;\n"
"border:none;\n"
"background-color: rgba(255, 255, 255, 0);")
        self.lineEdit_3.setText("")
        self.lineEdit_3.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.width_label = QtWidgets.QLabel(self.tab)
        self.width_label.setGeometry(QtCore.QRect(560, 360, 41, 41))
        self.width_label.setStyleSheet("font: 63 10pt \"阿里妈妈方圆体 VF SemiBold\";")
        self.width_label.setObjectName("width_label")
        self.widthcomboBox = QtWidgets.QComboBox(self.tab)
        self.widthcomboBox.setGeometry(QtCore.QRect(610, 370, 61, 21))
        self.widthcomboBox.setStyleSheet("QComboBox#widthcomboBox::drop-down{\n"
"        image:url(:/img/img/Vector_2.png)\n"
"        } \n"
"QComboBox#widthcomboBox::drop-down:hover{\n"
"        background-color:red\n"
"        }\n"
"")
        self.widthcomboBox.setObjectName("widthcomboBox")
        self.widthcomboBox.addItem("")
        self.widthcomboBox.addItem("")
        self.widthcomboBox.addItem("")
        self.widthcomboBox.addItem("")
        self.widthcomboBox.addItem("")
        self.widthcomboBox.addItem("")
        self.widthcomboBox.addItem("")
        self.height_label = QtWidgets.QLabel(self.tab)
        self.height_label.setGeometry(QtCore.QRect(720, 360, 41, 41))
        self.height_label.setStyleSheet("font: 63 10pt \"阿里妈妈方圆体 VF SemiBold\";")
        self.height_label.setObjectName("height_label")
        self.heightcomboBox = QtWidgets.QComboBox(self.tab)
        self.heightcomboBox.setGeometry(QtCore.QRect(770, 370, 61, 21))
        self.heightcomboBox.setStyleSheet("QComboBox#heightcomboBox::drop-down{\n"
"        image:url(:/img/img/Vector_2.png)\n"
"        } \n"
"QComboBox#heightcomboBox::drop-down:hover{\n"
"        background-color:red\n"
"        }\n"
"")
        self.heightcomboBox.setObjectName("heightcomboBox")
        self.heightcomboBox.addItem("")
        self.heightcomboBox.addItem("")
        self.heightcomboBox.addItem("")
        self.heightcomboBox.addItem("")
        self.heightcomboBox.addItem("")
        self.heightcomboBox.addItem("")
        self.heightcomboBox.addItem("")
        self.heightcomboBox.addItem("")
        self.heightcomboBox.addItem("")
        self.startBtn = QtWidgets.QPushButton(self.tab)
        self.startBtn.setGeometry(QtCore.QRect(610, 480, 141, 51))
        self.startBtn.setStyleSheet("\n"
"color:#000000;\n"
"border:none;\n"
"background-color: rgba(255, 255, 255, 0);")
        self.startBtn.setText("")
        self.startBtn.setObjectName("startBtn")
        self.widthcomboBox_2 = QtWidgets.QComboBox(self.tab)
        self.widthcomboBox_2.setGeometry(QtCore.QRect(550, 180, 291, 51))
        self.widthcomboBox_2.setStyleSheet("QComboBox#widthcomboBox_2::drop-down{\n"
"        image:url(:/img/img/Vector_2.png);\n"
"color:#000000;\n"
"border:none;\n"
"background-color: rgba(255, 255, 255, 0);\n"
"\n"
"        } \n"
"QComboBox#widthcomboBox_2::drop-down:hover{\n"
"        background-color:red;\n"
"        }\n"
"")
        self.widthcomboBox_2.setLocale(QtCore.QLocale(QtCore.QLocale.Chinese, QtCore.QLocale.China))
        self.widthcomboBox_2.setObjectName("widthcomboBox_2")
        self.widthcomboBox_2.addItem("")
        self.widthcomboBox_2.addItem("")
        self.widthcomboBox_2.addItem("")
        self.widthcomboBox_2.addItem("")
        self.widthcomboBox_2.addItem("")
        self.widthcomboBox_2.addItem("")
        self.widthcomboBox_2.addItem("")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.tab_2)
        self.horizontalLayout.setContentsMargins(0, 18, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBox = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableView = QtWidgets.QTableView(self.groupBox)
        self.tableView.setObjectName("tableView")
        self.verticalLayout.addWidget(self.tableView)
        self.horizontalLayout.addWidget(self.groupBox)
        self.frame_2 = QtWidgets.QFrame(self.tab_2)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.pushButton = QtWidgets.QPushButton(self.frame_2)
        self.pushButton.setGeometry(QtCore.QRect(30, 260, 121, 31))
        self.pushButton.setStyleSheet(" border: 2px solid #000000; \n"
"border-radius: 9px;")
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setGeometry(QtCore.QRect(10, 130, 81, 41))
        self.label.setStyleSheet("font: 63 10pt \"阿里妈妈方圆体 VF SemiBold\";")
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit.setGeometry(QtCore.QRect(10, 180, 171, 41))
        self.lineEdit.setStyleSheet(" border: 2px solid #000000; \n"
"border-radius: 9px;\n"
"color:#000000;")
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_2.setGeometry(QtCore.QRect(30, 330, 121, 31))
        self.pushButton_2.setStyleSheet(" border: 2px solid #000000; \n"
"border-radius: 9px;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.frame_2)
        self.horizontalLayout.setStretch(0, 4)
        self.horizontalLayout.setStretch(1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.verticalLayout_2.addWidget(self.tabWidget)

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.width_label.setText(_translate("Form", "宽度"))
        self.widthcomboBox.setItemText(0, _translate("Form", "512"))
        self.widthcomboBox.setItemText(1, _translate("Form", "640"))
        self.widthcomboBox.setItemText(2, _translate("Form", "680"))
        self.widthcomboBox.setItemText(3, _translate("Form", "720"))
        self.widthcomboBox.setItemText(4, _translate("Form", "768"))
        self.widthcomboBox.setItemText(5, _translate("Form", "1024"))
        self.widthcomboBox.setItemText(6, _translate("Form", "1280"))
        self.height_label.setText(_translate("Form", "高度"))
        self.heightcomboBox.setItemText(0, _translate("Form", "512"))
        self.heightcomboBox.setItemText(1, _translate("Form", "360"))
        self.heightcomboBox.setItemText(2, _translate("Form", "480"))
        self.heightcomboBox.setItemText(3, _translate("Form", "640"))
        self.heightcomboBox.setItemText(4, _translate("Form", "680"))
        self.heightcomboBox.setItemText(5, _translate("Form", "720"))
        self.heightcomboBox.setItemText(6, _translate("Form", "768"))
        self.heightcomboBox.setItemText(7, _translate("Form", "1024"))
        self.heightcomboBox.setItemText(8, _translate("Form", "1280"))
        self.widthcomboBox_2.setItemText(0, _translate("Form", "赛博朋克"))
        self.widthcomboBox_2.setItemText(1, _translate("Form", "古风"))
        self.widthcomboBox_2.setItemText(2, _translate("Form", "二次元"))
        self.widthcomboBox_2.setItemText(3, _translate("Form", "未来主义"))
        self.widthcomboBox_2.setItemText(4, _translate("Form", "卡通画"))
        self.widthcomboBox_2.setItemText(5, _translate("Form", "油画"))
        self.widthcomboBox_2.setItemText(6, _translate("Form", "像素风格"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "AI画图"))
        self.groupBox.setTitle(_translate("Form", "用户信息"))
        self.pushButton.setText(_translate("Form", "查询"))
        self.label.setText(_translate("Form", "用户账号："))
        self.pushButton_2.setText(_translate("Form", "删除"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "用户管理"))
import ui.imgmanager
