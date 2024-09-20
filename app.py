import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl

app = QApplication(sys.argv)

window = QMainWindow()
view = QWebEngineView()

chemin_html = os.path.abspath("index.html")
url = QUrl.fromLocalFile(chemin_html)
view.setUrl(url)
window.setCentralWidget(view)
window.showMaximized()
window.show()

sys.exit(app.exec_())
