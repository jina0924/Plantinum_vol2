# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sleepUI.ui'
##
## Created by: Qt User Interface Compiler version 6.2.4
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide2.QtWidgets import (QApplication, QLabel, QPushButton, QSizePolicy,
    QWidget,QGraphicsOpacityEffect)
import myres_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1366, 767)
        Form.setStyleSheet(u"background-color: rgb(20, 1, 44);")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(558, 180, 250, 250))
        self.label.setStyleSheet(u"image: url(:/icon/img/moon.svg);")
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(433, 460, 500, 50))
        font = QFont()
        font.setPointSize(26)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_2.setAlignment(Qt.AlignCenter)
        self.wakeup_button = QPushButton(Form)
        self.wakeup_button.setObjectName(u"wakeup_button")
        self.wakeup_button.setGeometry(QRect(0, 0, 1366, 768))
        self.wakeup_button.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        opacity_effect = QGraphicsOpacityEffect(self.wakeup_button)
        opacity_effect.setOpacity(0)
        self.wakeup_button.setGraphicsEffect(opacity_effect)

        self.retranslateUi(Form)
        self.wakeup_button.clicked.connect(Form.wakeup)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("Form", u"GOOD NIGHT", None))
        self.wakeup_button.setText("")
    # retranslateUi

