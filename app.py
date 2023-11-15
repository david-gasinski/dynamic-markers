from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton
from PyQt6.QtWebEngineWidgets import QWebEngineView

import sys

app = QApplication(sys.argv)
window = QWidget()
layout = QVBoxLayout()


view = QWebEngineView()
layout.addWidget(view)
button = QPushButton("Add marker at pos +0.0001")

# set the url to the html
view.setHtml(open('./static/index.html').read())

lon = 51.505
lat = -0.09

def addMarker():
    global lon, lat
    lon += 0.01
    lat += 0.01
    view.page().runJavaScript(f'addMarker({lon},{lat})')
button.clicked.connect(addMarker)

layout.addWidget(button)

window.setLayout(layout)
window.show()

app.exec()
