from PyQt5.QtGui import QPixmap, QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QWidget, QMessageBox, QAbstractItemView

from AIDraw.page.respage import ResPage
from AIDraw.sql.tools import create_db
from AIDraw.ui.managerpage import Ui_Form
from AIDraw.word2picture import main, parser_Message


class ManagerPage(QWidget, Ui_Form):
    def __init__(self):
        super(ManagerPage, self).__init__()
        self.setupUi(self)
        self.APPID = ''
        self.APISecret = ''
        self.APIKEY = ''
        self.fengge = ''
        self.content = ''
        self.width = 0
        self.height = 0
        self.respage = ResPage()
        self.tableView.setSelectionMode(QAbstractItemView.SingleSelection)  # 或 ExtendedSelection, MultiSelection 等
        self.tableView.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.init_slot()  # 初始化槽函数

    def init_slot(self):
        db, cursor = create_db(host='124.222.118.135', password='team2111.', database='ldy',
                               user='root', port=3306)
        sql = "SELECT *  FROM aiusers LIMIT 5"
        cursor.execute(sql)
        userdata = cursor.fetchall()
        if userdata:
            # 创建一个标准模型来存储数据
            self.model = QStandardItemModel(len(userdata), 4)  # 根据userdata的长度设置行数，4列
            self.model.setHorizontalHeaderLabels(['用户账号', '用户密码', '用户身份', 'ID'])

            # 填充模型
            for row_index, row_data in enumerate(userdata):
                for column_index, value in enumerate(row_data):
                    item = QStandardItem(str(value))
                    self.model.setItem(row_index, column_index, item)

                    # 将模型设置为tableView的模型
            self.tableView.setModel(self.model)
            print('显示数据到界面')

        self.startBtn.clicked.connect(self.start)
        self.pushButton.clicked.connect(self.find)
        self.pushButton_2.clicked.connect(self.dels)

    def start(self):
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

    def find(self):
        user_id = self.lineEdit.text()
        print(user_id)
        if not user_id:
            print("你输入的信息不全，请输入完整")
            QMessageBox.warning(self, 'Warning', '你输入的信息不全，请输入完整!')
            return
        db, cursor = create_db(host='124.222.118.135', password='team2111.', database='ldy',
                               user='root', port=3306)
        sql = "SELECT user_id, user_pwd, user_class, id FROM aiusers WHERE user_id = {} LIMIT 1".format(str(user_id))
        try:
            cursor.execute(sql)
            userdata = cursor.fetchall()
            if len(userdata) > 0:
                # 创建一个标准模型来存储数据
                model = QStandardItemModel(1, 4)  # 1行4列
                model.setHorizontalHeaderLabels(['用户账号', '用户密码', '用户身份', 'ID'])

                # 填充模型
                for column, value in enumerate(userdata[0]):
                    item = QStandardItem(str(value))
                    model.setItem(0, column, item)

                    # 将模型设置为tableView的模型
                self.tableView.setModel(model)
                print('显示数据到界面')
            else:
                print('未查询到该用户的信息')
                QMessageBox.warning(self, 'Warning', '未查询到该用户的信息')
                return
        except BaseException as e:
            print('error', str(e))
            return

    def dels(self):
        # 获取选中的行索引
        selected_indexes = self.tableView.selectionModel().selectedRows()
        if selected_indexes:
            # 获取第一个（也可能是唯一的）选中的行索引
            row_to_delete = selected_indexes[0].row()

            # 从模型中移除行
            self.model.removeRow(row_to_delete)

            # 如果需要，从数据库中删除对应的记录
            # 假设create_db函数返回有效的数据库连接
            db, cursor = create_db(host='124.222.118.135', password='team2111.', database='ldy',
                                   user='root', port=3306)
            sql = "DELETE FROM aiusers WHERE id = %s"  # 假设表中有id字段

            # 确保获取到的ID不为空
            id_to_delete = self.model.item(row_to_delete, 3).text()
            if id_to_delete:
                try:
                    cursor.execute(sql, (id_to_delete,))
                    db.commit()  # 提交数据库更改
                    print("从数据库中成功删除记录")
                except Exception as e:
                    print(f"从数据库删除记录时出错: {e}")
                    # 这里可以添加代码来撤销从模型中删除的行，或者提示用户手动处理错误
            else:
                print("选中的行中没有找到ID，无法从数据库中删除")

            cursor.close()
            db.close()  # 关闭数据库连接
        else:
            print("没有选中任何行")