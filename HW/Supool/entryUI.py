# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'entryUI.ui'
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
    QWidget)
import myres_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1366, 768)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setStyleSheet(u"background-color: rgb(248, 245, 238);")
        self.new_button = QPushButton(Form)
        self.new_button.setObjectName(u"new_button")
        self.new_button.setGeometry(QRect(583, 270, 200, 70))
        self.new_button.setStyleSheet(u"background-color: rgb(178, 201, 171);\n"
"color: rgb(248, 245, 238);\n"
"font: 700 24pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"border-radius: 5px;")
        self.old_button = QPushButton(Form)
        self.old_button.setObjectName(u"old_button")
        self.old_button.setGeometry(QRect(583, 380, 200, 70))
        self.old_button.setStyleSheet(u"background-color: rgb(178, 201, 171);\n"
"color: rgb(248, 245, 238);\n"
"font: 700 24pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"border-radius: 5px;")
        self.background_label = QLabel(Form)
        self.background_label.setObjectName(u"background_label")
        self.background_label.setGeometry(QRect(0, 0, 1366, 768))
        self.background_label.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0.517045, y1:1, x2:0.466, y2:0, stop:0 rgba(178, 201, 171, 255), stop:1 rgba(248, 245, 238, 255));\n"
"border-image: url(:/img/img/\uc2dc\uc791\ud654\uba74_\ubc30\uacbd.png);")
        self.background_label.setMidLineWidth(0)
        self.background_label.raise_()
        self.new_button.raise_()
        self.old_button.raise_()

        self.retranslateUi(Form)
        self.new_button.clicked.connect(Form.new_plant)
        self.old_button.clicked.connect(Form.old_plant)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.new_button.setText(QCoreApplication.translate("Form", u"New", None))
        self.old_button.setText(QCoreApplication.translate("Form", u"Load", None))
        self.background_label.setText("")
    # retranslateUi

