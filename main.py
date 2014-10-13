import sys
import io
import signal

from PyQt5.QtWidgets import QApplication
from PyQt5.QtQml import qmlRegisterType, QQmlComponent, QQmlEngine, QQmlApplicationEngine
from PyQt5.QtCore import QUrl


if __name__ == '__main__':
    app = QApplication(sys.argv)
    engine = QQmlApplicationEngine('main.qml')

    # Killable by Ctrl+C
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    sys.exit(app.exec_())

