import sys

from PyQt5.QtWidgets import QApplication

from widget.main_window import MainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)  # 1. Instantiate ApplicationContext
    window = MainWindow()
    window.show()

    exit_code = app.exec_()  # 2. Invoke appctxt.app.exec_()
    sys.exit(exit_code)
