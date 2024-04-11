from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QMessageBox

from AIDraw.ui.res_page import Ui_Form
from AIDraw.word2picture import main, parser_Message


class ResPage(QWidget, Ui_Form):
    def __init__(self):
        super(ResPage, self).__init__()
        self.setupUi(self)
        self.APPID = '5277f5fd'
        self.APISecret = 'ZjIyOGRlMmMyMTcyNDA3YmNkYWUwNjk0'
        self.APIKEY = 'a866423e3dc77a55ea875cecc6cdb153'
        self.fengge = ''
        self.content = ''
        self.width = 0
        self.height = 0
        self.init_slot()  # 初始化槽函数

    def init_slot(self):
        self.restartBtn.clicked.connect(self.startDraw)

    def startDraw(self):
        # 判断用户输入的内容是否为空
        if not self.fengge or not self.content or not self.width or not self.height:
            print("你输入的信息不全，请输入完整")
            QMessageBox.warning(self, 'Warning', '你输入的信息不全，请输入完整!')
            return
        else:
            # 开始生成图片
            res = main(self.content, appid=self.APPID, apikey=self.APIKEY, apisecret=self.APISecret, width=int(self.width),
                       height=int(self.height), user="user", fengge=self.fengge)
            # print(res)
            # 保存到指定位置
            ok, data = parser_Message(res, 'image/')
            if ok:
                url_path = data
                print('作画成功')

                # 加载本地图片
                pixmap = QPixmap(url_path)

                # 将图片显示在label中，不进行等比例缩放
                self.label.setPixmap(pixmap)
                self.label.setScaledContents(False)
                return
            QMessageBox.warning(self, 'Warning', '{}'.format(data))
            return

