# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'detailUI.ui'
##
## Created by: Qt User Interface Compiler version 6.2.4
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QSizePolicy,
    QWidget)
import myres_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1024, 600)
        Form.setStyleSheet(u"background-color: rgb(248, 245, 238);")

        # title?
        self.title = QLabel(Form)
        self.title.setObjectName(u"title")
        self.title.setGeometry(QRect(100, 40, 281, 101))
        font = QFont()
        font.setPointSize(24)
        font.setBold(True)
        self.title.setFont(font)
        self.title.setStyleSheet(u"\n"
        "background-color: rgba(255, 237, 222,200);\n"
        "color: rgb(124, 200, 135);")
        self.title.setAlignment(Qt.AlignCenter)

        # 뒤로가기
        self.back_button = QPushButton(Form)
        self.back_button.setObjectName(u"back_button")
        self.back_button.setGeometry(QRect(950, 20, 40, 40))
        self.back_button.setStyleSheet(u"border-image: url(:/icon/img/return_green.png);\n"

"background-color: rgb(248, 245, 238);")

        # 테스트 라벨?
        self.testlabel = QLabel(Form)
        self.testlabel.setObjectName(u"testlabel")
        self.testlabel.setGeometry(QRect(150, 250, 131, 211))
        font1 = QFont()
        font1.setPointSize(18)
        font1.setBold(True)
        self.testlabel.setFont(font1)


        self.retranslateUi(Form)
        self.back_button.clicked.connect(Form.go_mainpage)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.title.setText(QCoreApplication.translate("Form", u"MY PLANT", None))
        self.back_button.setText("")
        self.testlabel.setText("")
    # retranslateUi

