
import sys
import signal
import time

import Pyro4

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtQml import *
from PyQt5.QtWidgets import *
from PyQt5.QtQuick import *
from PyQt5.QtQuickWidgets import *

class Content(QObject):
    
    def __init__(self, app):
        QObject.__init__(self)
        self.app = app

    @property
    def name(self):
        return "changer"
    def set_thread(self, thread):
        self.thread = thread

    def change_qml(self, qml_file):
        #print("called")
        self.thread.changed.emit(qml_file)
        

class PyroServer(QThread):

    changed = pyqtSignal(str)
    def __init__(self):
        QThread.__init__(self)

    def set_obj(self, export):
        self.export = export
        
    def run(self):
        daemon = Pyro4.Daemon()
        ns = Pyro4.locateNS()
        self.export.set_thread(self)
        uri = daemon.register(self.export)
        ns.register("info." + self.export.name, uri)
        
        print("Started thread")
        
        daemon.requestLoop()
        
class App(QObject):
    ch = pyqtSignal(str)
    def __init__(self):
        QObject.__init__(self)
        #print("foo")
        
        app = QApplication(sys.argv)

        engine = QQmlApplicationEngine()
        component = QQmlComponent(engine)
        component.loadUrl(QUrl('window.qml'))

        # Removing this line causes segfault...
        self.engine = engine
        
        main = component.create()
        self.main = main
        self.app = app

        print("Started app")
        self.ch.connect(self.set_qml_real)
        #self.ch.emit()
        #self.changed.connect(self.set_qml)
        #self.signal.changed.emit()

        
        
    @property
    def qapp(self):
        return self.app

    def emit(self):
        self.changed.emit()

    def set_qml(self, qml_file):
        self.ch.emit(qml_file)
        
    def set_qml_real(self, qml_file):
        #print("foofoo")
        self.main.findChild(QObject, "Loader").setProperty("source", qml_file)
        #self.loader.setProperty("color", "green")

if __name__ == "__main__":

    signal.signal(signal.SIGINT, signal.SIG_DFL)
    app = App()
    #print("foobar")
    
    pyroserv = PyroServer()
    pyroserv.changed.connect(app.set_qml_real, Qt.QueuedConnection)
    pyroserv.set_obj(Content(app))
    pyroserv.start()
    #print("bar")

    sys.exit(app.qapp.exec_())


