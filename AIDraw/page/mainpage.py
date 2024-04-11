from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QMessageBox
from PyQt5.QtGui import QPixmap
from AIDraw.page.respage import ResPage
from AIDraw.ui.main_page import Ui_Form
from AIDraw.word2picture import main, parser_Message


class MainPage(QWidget, Ui_Form):
    def __init__(self):
        super(MainPage, self).__init__()
        self.setupUi(self)
        self.APPID = ''
        self.APISecret = ''
        self.APIKEY = ''
        self.init_slot()  # 初始化槽函数
        print('MainPage')

    def init_slot(self):
        self.respage = ResPage()  # 创建一个结果显示的界面
        self.startBtn.clicked.connect(self.startDraw)

    def startDraw(self):
        fengge = self.widthcomboBox_2.currentText()  # 获取用户输入的风格
        content = self.lineEdit_3.text()  # 获取用户输入的内容描述
        width = self.widthcomboBox.currentText()  # 获取用户选择的图片宽度
        height = self.heightcomboBox.currentText()  # 获取用户选择的图片的高度

        # 判断用户输入的内容是否为空
        if not fengge or not content or not width or not height:
            print("你输入的信息不全，请输入完整")
            QMessageBox.warning(self, 'Warning', '你输入的信息不全，请输入完整!')
            return
        else:
            # 开始生成图片
            res = main(content, appid=self.APPID, apikey=self.APIKEY, apisecret=self.APISecret, width=int(width),
                       height=int(height), user="user", fengge=fengge)
            # print(res)
            # 保存到指定位置
            ok, data = parser_Message(res, 'image/')
            if ok:
                url_path = data
                print('作画成功')

                # 加载本地图片
                pixmap = QPixmap(url_path)

                # 将图片显示在label中，不进行等比例缩放
                self.respage.label.setPixmap(pixmap)
                self.respage.label.setScaledContents(False)
                self.respage.content = content
                self.respage.fengge = fengge
                self.respage.width = width
                self.respage.height = height
                self.respage.show()
                return
            QMessageBox.warning(self, 'Warning', '{}'.format(data))
            return
