from PyQt5.QtWidgets import QWidget, QMessageBox

from AIDraw.page.enrollPages import EnrollPage
from AIDraw.page.mainpage import MainPage
from AIDraw.page.managerPages import ManagerPage
from AIDraw.sql.tools import create_db
from AIDraw.ui.homepage import Ui_Form


class HomePage(QWidget, Ui_Form):
    def __init__(self):
        super(HomePage, self).__init__()
        self.setupUi(self)
        self.init_slot()  # 初始化槽函数
        print('-------------------')

    def init_slot(self):
        self.loginBtn.clicked.connect(self.login)
        self.enrollBtn.clicked.connect(self.enroll)

    def login(self):
        user_id = self.lineEdit.text()
        user_pwd = self.lineEdit_2.text()

        if user_id.strip() == '' or user_pwd.strip() == '':
            QMessageBox.warning(self, 'Warning', '用户名和密码不能为空')
            return
        else:
            db, cursor = create_db(host='124.222.118.135', password='team2111.', database='ldy',
                                   user='root', port=3306)
            sql = "SELECT user_class FROM aiusers WHERE user_id = {}  AND user_pwd = {} LIMIT 1".format(str(user_id), str(user_pwd))
            try:
                cursor.execute(sql)
                userdata = cursor.fetchall()
                if len(userdata) > 0:
                    QMessageBox.information(self, '登录成功', '登录成功')
                    # 界面跳转
                    user_class = userdata[0][0]  # 获取用户的身份
                    print(user_class)
                    if user_class == '1':
                        # 普通用户
                        print('普通用户')
                        self.page = MainPage()  # 创建一个普通用户的AI画图界面
                        self.page.show()  # 显示该界面
                        self.hide()
                    elif user_class == '2':
                        # 管理员
                        self.page = ManagerPage()  # 创建一个管理员的界面
                        self.hide()
                        self.page.show()  # 显示该界面
                else:
                    print('该用户未注册')
                    QMessageBox.warning(self, 'Warning', '该用户未注册')
                    return
            except:
                print('error')
                return
            pass
    # 在这里写登录逻辑，例如验证用户名密码等


    def enroll(self):
        self.enrollPages = EnrollPage()  # 创建一个注册界面对象
        self.enrollPages.show()
        self.close()