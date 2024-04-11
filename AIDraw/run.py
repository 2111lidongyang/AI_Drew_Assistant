import sys

from PyQt5.QtWidgets import QApplication
from page.homePages import HomePage

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_page = HomePage()
    main_page.show()
    sys.exit(app.exec())
