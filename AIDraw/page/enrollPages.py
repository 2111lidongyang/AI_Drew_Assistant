from PyQt5.QtWidgets import QWidget, QMessageBox

from AIDraw.page.mainpage import MainPage
from AIDraw.page.managerPages import ManagerPage
from AIDraw.sql.tools import create_db
from AIDraw.ui.enrollpage import Ui_Form

"""
注册界面，能够进行普通用户注册或者管理员注册
"""


class EnrollPage(QWidget, Ui_Form):
    def __init__(self):
        super(EnrollPage, self).__init__()
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
        self.enrollBtn.clicked.connect(self.enrollfunc)
        self.loginBtn.clicked.connect(self.login)

    def enrollfunc(self):
        user_id = self.idlineEdit.text()
        user_pwd = self.pwdlineEdit.text()
        if self.radioButton.isChecked():
            user_class = '1'
        elif self.radioButton_2.isChecked():
            user_class = '2'
        else:
            print('请选择你的身份类别')
            QMessageBox.warning(self, 'Warning', '请选择你的身份类别')
            return
        # 检查用户名和密码是否为空
        if not user_id or not user_pwd:
            print('请填写用户名和密码')
            QMessageBox.warning(self, 'Warning', '请填写用户名和密码')
            return
        print('开始注册')
        db, cursor = create_db(host='124.222.118.135', password='team2111.', database='ldy',
                               user='root', port=3306)
        sql = "SELECT * FROM aiusers WHERE user_id = {} LIMIT 1".format(str(user_id))  # 判断该用户是否存在
        try:
            cursor.execute(sql)
            userdata = cursor.fetchall()
            if len(userdata) > 0:
                QMessageBox.warning(self, '注册失败', '该用户已存在！')
                return
            print('注册中')
            sql_insert = "INSERT INTO aiusers (user_id, user_pwd, user_class) VALUES ('{}', '{}', '{}')".format(
                str(user_id), str(user_pwd), str(user_class))
            try:
                cursor.execute(sql_insert)
                db.commit()
                cursor.close()
                db.close()
                QMessageBox.information(self, '注册成功', '用户注册成功')
                if user_class == '1':
                    self.loginpage = MainPage()  # 直接登录
                    self.hide()
                    self.loginpage.show()
                    return
                elif user_class == '2':
                    self.page = ManagerPage()
                    self.hide()
                    self.page.show()
                    return
            except:
                db.rollback()
                cursor.close()
                db.close()
                return
        except BaseException as e:
            print("error", str(e))
            return

    def login(self):
        print('d=========')
        pass
