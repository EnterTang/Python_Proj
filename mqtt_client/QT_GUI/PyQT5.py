import sys, json
from PyQt5.QtWidgets import (QMainWindow, QWidget, QToolTip, QLabel, QTextBrowser, QGridLayout,
    QPushButton, QApplication, QMessageBox, QDesktopWidget)
from PyQt5.QtGui import QIcon, QFont

class GUI_Qapp(QApplication):
    def __init__(self):
        super().__init__(sys.argv)


class GUI_Qwidget(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()  # 界面绘制交给InitUi方法

    # 控制窗口显示在屏幕中心的方法
    def center(self):
        # 获得窗口
        qr = self.frameGeometry()
        # 获得屏幕中心点
        cp = QDesktopWidget().availableGeometry().center()
        # 显示到屏幕中心
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def initUI(self):
        # 这种静态的方法设置一个用于显示工具提示的字体。我们使用10px滑体字体。
        QToolTip.setFont(QFont('SansSerif', 10))
        # 创建一个PushButton并为他设置一个tooltip
        btn = QPushButton('设置', self)
        btn.setToolTip('设置MQTT服务器等配置')
        # btn.sizeHint()显示默认尺寸
        btn.resize(btn.sizeHint())
        # 移动窗口的位置
        btn.move(50, 50)

        # 设置窗口的位置和大小
        self.resize(500, 500)
        self.center()
        # 设置窗口的标题
        self.setWindowTitle('MQTT消息过滤器')
        # 设置窗口的图标，引用当前目录下的web.png图片
        self.setWindowIcon(QIcon('pics/icon_Q.png'))
        # 显示窗口
        self.show()

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message',
                                     "确认要退出吗?", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

class GUI_QMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setFixedSize(960, 700)
        self.center()
        self.setWindowTitle('MQTT消息过滤器')
        # 设置窗口的图标，引用当前目录下的web.png图片
        self.setWindowIcon(QIcon('pics/icon_Q.png'))

        self.main_widget = QWidget()  # 创建窗口主部件
        self.main_layout = QGridLayout()  # 创建主部件的网格布局
        self.main_widget.setLayout(self.main_layout)  # 设置窗口主部件布局为网格布局

        self.left_widget = QWidget()  # 创建左侧部件
        self.left_widget.setObjectName('left_widget')
        self.left_layout = QGridLayout()  # 创建左侧部件的网格布局
        self.left_widget.setLayout(self.left_layout)  # 设置左侧部件布局为网格布局

        self.right_widget = QWidget()  # 创建右侧部件
        self.right_widget.setObjectName('right_widget')
        self.right_layout = QGridLayout()  # 创建右侧部件的网格布局
        self.right_widget.setLayout(self.right_layout)  # 设置右侧部件布局为网格布局

        self.main_layout.addWidget(self.left_widget, 0, 0, 12, 2)
        self.main_layout.addWidget(self.right_widget, 0, 2, 12, 10)
        self.setCentralWidget(self.main_widget)  # 设置窗口主部件

        self.txtbrowser = QTextBrowser()
        self.right_layout.addWidget(self.txtbrowser, 5, 5, 9, 13)

        self.topicbrowser = QTextBrowser()
        self.left_layout.addWidget(self.topicbrowser, 0, 0, 6, 6)

    # 控制窗口显示在屏幕中心的方法
    def center(self):
        # 获得窗口
        qr = self.frameGeometry()
        # 获得屏幕中心点
        cp = QDesktopWidget().availableGeometry().center()
        # 显示到屏幕中心
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def show_msg(self, data):
        self.txtbrowser.append(data)

    def change(self, value):
        isDict = 0
        if isinstance(value, dict):
            isDict = 1
        if isDict:
            if "type" in value:
                if value["type"] == "subTopics":
                    for i in value["topics"]:
                        self.topicbrowser.append(i)
                elif value["type"] == "showMsg":
                    self.txtbrowser.append(json.dumps(json.loads(value["payload"]), sort_keys=True, indent=4, separators=(',', ':')))
        # pass