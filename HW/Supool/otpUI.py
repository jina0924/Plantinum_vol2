# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'otpUI.ui'
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
from PySide2.QtWidgets import (QApplication, QGridLayout, QLabel, QLayout,
    QPushButton, QSizePolicy, QWidget)
import myres_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1366, 768)
        Form.setStyleSheet(u"background-color: rgb(248, 245, 238);")
        self.label_otp = QLabel(Form)
        self.label_otp.setObjectName(u"label_otp")
        self.label_otp.setGeometry(QRect(300, 250, 200, 80))
        font = QFont()
        font.setPointSize(48)
        font.setBold(True)
        self.label_otp.setFont(font)
        self.label_otp.setStyleSheet(u"background-color: rgba(255, 237, 216,0);\n"
"color: rgb(101, 128, 93);")
        self.label_otp.setAlignment(Qt.AlignCenter)
        self.button_back = QPushButton(Form)
        self.button_back.setObjectName(u"button_back")
        self.button_back.setGeometry(QRect(1250, 20, 81, 71))
        font1 = QFont()
        font1.setPointSize(22)
        font1.setBold(True)
        self.button_back.setFont(font1)
        self.button_back.setStyleSheet(u"background-color: rgb(248, 245, 238);\n"
"color: rgb(85, 170, 127);\n"
"border-image: url(:/icon/img/home.svg);")
        self.logo_label = QLabel(Form)
        self.logo_label.setObjectName(u"logo_label")
        self.logo_label.setGeometry(QRect(20, 20, 121, 31))
        font2 = QFont()
        font2.setFamilies([u"Palace Script MT"])
        font2.setPointSize(26)
        font2.setItalic(True)
        self.logo_label.setFont(font2)
        self.logo_label.setStyleSheet(u"image: url(:/logo/img/\uff2f\uff34\uff30\uff3f\uff50\uff4c\uff41\uff4e\uff54\uff49\uff4e\uff55\uff4d.png);")
        self.logo_label.setAlignment(Qt.AlignCenter)
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(160, 350, 480, 20))
        font3 = QFont()
        font3.setPointSize(16)
        font3.setBold(False)
        self.label_2.setFont(font3)
        self.label_2.setStyleSheet(u"color: rgb(101, 128, 93);")
        self.label_2.setAlignment(Qt.AlignCenter)
        self.layoutWidget = QWidget(Form)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(204, 420, 401, 71))
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetNoConstraint)
        self.gridLayout.setVerticalSpacing(9)
        self.gridLayout.setContentsMargins(1, 0, 0, 0)
        self.number_3 = QLabel(self.layoutWidget)
        self.number_3.setObjectName(u"number_3")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.number_3.sizePolicy().hasHeightForWidth())
        self.number_3.setSizePolicy(sizePolicy)
        font4 = QFont()
        font4.setPointSize(26)
        font4.setBold(True)
        self.number_3.setFont(font4)
        self.number_3.setStyleSheet(u"background-color : white;\n"
"border-radius: 10px;\n"
"")
        self.number_3.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.number_3, 0, 3, 1, 1)

        self.number_5 = QLabel(self.layoutWidget)
        self.number_5.setObjectName(u"number_5")
        sizePolicy.setHeightForWidth(self.number_5.sizePolicy().hasHeightForWidth())
        self.number_5.setSizePolicy(sizePolicy)
        self.number_5.setFont(font4)
        self.number_5.setStyleSheet(u"background-color : white;\n"
"border-radius: 10px;\n"
"")
        self.number_5.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.number_5, 0, 5, 1, 1)

        self.number_4 = QLabel(self.layoutWidget)
        self.number_4.setObjectName(u"number_4")
        sizePolicy.setHeightForWidth(self.number_4.sizePolicy().hasHeightForWidth())
        self.number_4.setSizePolicy(sizePolicy)
        self.number_4.setFont(font4)
        self.number_4.setStyleSheet(u"background-color : white;\n"
"border-radius: 10px;\n"
"")
        self.number_4.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.number_4, 0, 4, 1, 1)

        self.number_1 = QLabel(self.layoutWidget)
        self.number_1.setObjectName(u"number_1")
        sizePolicy.setHeightForWidth(self.number_1.sizePolicy().hasHeightForWidth())
        self.number_1.setSizePolicy(sizePolicy)
        self.number_1.setFont(font4)
        self.number_1.setStyleSheet(u"background-color : white;\n"
"border-radius: 10px;\n"
"")
        self.number_1.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.number_1, 0, 0, 1, 1)

        self.number_2 = QLabel(self.layoutWidget)
        self.number_2.setObjectName(u"number_2")
        sizePolicy.setHeightForWidth(self.number_2.sizePolicy().hasHeightForWidth())
        self.number_2.setSizePolicy(sizePolicy)
        self.number_2.setFont(font4)
        self.number_2.setStyleSheet(u"background-color : white;\n"
"border-radius: 10px;\n"
"")
        self.number_2.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.number_2, 0, 2, 1, 1)

        self.number_6 = QLabel(self.layoutWidget)
        self.number_6.setObjectName(u"number_6")
        sizePolicy.setHeightForWidth(self.number_6.sizePolicy().hasHeightForWidth())
        self.number_6.setSizePolicy(sizePolicy)
        self.number_6.setFont(font4)
        self.number_6.setStyleSheet(u"background-color : white;\n"
"border-radius: 10px;\n"
"")
        self.number_6.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.number_6, 0, 6, 1, 1)

        self.layoutWidget1 = QWidget(Form)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(740, 150, 381, 491))
        self.gridLayout_2 = QGridLayout(self.layoutWidget1)
        self.gridLayout_2.setSpacing(10)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setSizeConstraint(QLayout.SetNoConstraint)
        self.gridLayout_2.setContentsMargins(10, 10, 10, 10)
        self.pad_3 = QPushButton(self.layoutWidget1)
        self.pad_3.setObjectName(u"pad_3")
        sizePolicy.setHeightForWidth(self.pad_3.sizePolicy().hasHeightForWidth())
        self.pad_3.setSizePolicy(sizePolicy)
        font5 = QFont()
        font5.setPointSize(20)
        font5.setBold(True)
        self.pad_3.setFont(font5)
        self.pad_3.setStyleSheet(u"background-color: rgb(178, 201, 171);\n"
"color: rgb(255,255,255);\n"
"border-radius:5px;")

        self.gridLayout_2.addWidget(self.pad_3, 0, 2, 1, 1)

        self.pad_1 = QPushButton(self.layoutWidget1)
        self.pad_1.setObjectName(u"pad_1")
        self.pad_1.setEnabled(True)
        sizePolicy.setHeightForWidth(self.pad_1.sizePolicy().hasHeightForWidth())
        self.pad_1.setSizePolicy(sizePolicy)
        self.pad_1.setFont(font5)
        self.pad_1.setStyleSheet(u"background-color: rgb(178, 201, 171);\n"
"color: rgb(255,255,255);\n"
"border-radius:5px;")

        self.gridLayout_2.addWidget(self.pad_1, 0, 0, 1, 1)

        self.pad_7 = QPushButton(self.layoutWidget1)
        self.pad_7.setObjectName(u"pad_7")
        sizePolicy.setHeightForWidth(self.pad_7.sizePolicy().hasHeightForWidth())
        self.pad_7.setSizePolicy(sizePolicy)
        self.pad_7.setFont(font5)
        self.pad_7.setStyleSheet(u"background-color: rgb(178, 201, 171);\n"
"color: rgb(255,255,255);\n"
"border-radius:5px;")

        self.gridLayout_2.addWidget(self.pad_7, 2, 0, 1, 1)

        self.pad_8 = QPushButton(self.layoutWidget1)
        self.pad_8.setObjectName(u"pad_8")
        sizePolicy.setHeightForWidth(self.pad_8.sizePolicy().hasHeightForWidth())
        self.pad_8.setSizePolicy(sizePolicy)
        self.pad_8.setFont(font5)
        self.pad_8.setStyleSheet(u"background-color: rgb(178, 201, 171);\n"
"color: rgb(255,255,255);\n"
"border-radius:5px;")

        self.gridLayout_2.addWidget(self.pad_8, 2, 1, 1, 1)

        self.pad_ok = QPushButton(self.layoutWidget1)
        self.pad_ok.setObjectName(u"pad_ok")
        sizePolicy.setHeightForWidth(self.pad_ok.sizePolicy().hasHeightForWidth())
        self.pad_ok.setSizePolicy(sizePolicy)
        self.pad_ok.setFont(font5)
        self.pad_ok.setStyleSheet(u"background-color: rgb(255,255,255);\n"
"color: rgb(178, 201, 171);\n"
"border-radius:5px;")

        self.gridLayout_2.addWidget(self.pad_ok, 3, 2, 1, 1)

        self.pad_6 = QPushButton(self.layoutWidget1)
        self.pad_6.setObjectName(u"pad_6")
        sizePolicy.setHeightForWidth(self.pad_6.sizePolicy().hasHeightForWidth())
        self.pad_6.setSizePolicy(sizePolicy)
        self.pad_6.setFont(font5)
        self.pad_6.setStyleSheet(u"background-color: rgb(178, 201, 171);\n"
"color: rgb(255,255,255);\n"
"border-radius:5px;")

        self.gridLayout_2.addWidget(self.pad_6, 1, 2, 1, 1)

        self.pad_0 = QPushButton(self.layoutWidget1)
        self.pad_0.setObjectName(u"pad_0")
        sizePolicy.setHeightForWidth(self.pad_0.sizePolicy().hasHeightForWidth())
        self.pad_0.setSizePolicy(sizePolicy)
        self.pad_0.setFont(font5)
        self.pad_0.setStyleSheet(u"background-color: rgb(178, 201, 171);\n"
"color: rgb(255,255,255);\n"
"border-radius:5px;")

        self.gridLayout_2.addWidget(self.pad_0, 3, 1, 1, 1)

        self.pad_2 = QPushButton(self.layoutWidget1)
        self.pad_2.setObjectName(u"pad_2")
        sizePolicy.setHeightForWidth(self.pad_2.sizePolicy().hasHeightForWidth())
        self.pad_2.setSizePolicy(sizePolicy)
        self.pad_2.setFont(font5)
        self.pad_2.setStyleSheet(u"background-color: rgb(178, 201, 171);\n"
"color: rgb(255,255,255);\n"
"border-radius:5px;")

        self.gridLayout_2.addWidget(self.pad_2, 0, 1, 1, 1)

        self.pad_9 = QPushButton(self.layoutWidget1)
        self.pad_9.setObjectName(u"pad_9")
        sizePolicy.setHeightForWidth(self.pad_9.sizePolicy().hasHeightForWidth())
        self.pad_9.setSizePolicy(sizePolicy)
        self.pad_9.setFont(font5)
        self.pad_9.setStyleSheet(u"background-color: rgb(178, 201, 171);\n"
"color: rgb(255,255,255);\n"
"border-radius:5px;")

        self.gridLayout_2.addWidget(self.pad_9, 2, 2, 1, 1)

        self.pad_4 = QPushButton(self.layoutWidget1)
        self.pad_4.setObjectName(u"pad_4")
        sizePolicy.setHeightForWidth(self.pad_4.sizePolicy().hasHeightForWidth())
        self.pad_4.setSizePolicy(sizePolicy)
        self.pad_4.setFont(font5)
        self.pad_4.setStyleSheet(u"background-color: rgb(178, 201, 171);\n"
"color: rgb(255,255,255);\n"
"border-radius:5px;")

        self.gridLayout_2.addWidget(self.pad_4, 1, 0, 1, 1)

        self.pad_back = QPushButton(self.layoutWidget1)
        self.pad_back.setObjectName(u"pad_back")
        sizePolicy.setHeightForWidth(self.pad_back.sizePolicy().hasHeightForWidth())
        self.pad_back.setSizePolicy(sizePolicy)
        self.pad_back.setFont(font5)
        self.pad_back.setStyleSheet(u"background-color: rgb(255,255,255);\n"
"color: rgb(178, 201, 171);\n"
"border-radius:5px;")

        self.gridLayout_2.addWidget(self.pad_back, 3, 0, 1, 1)

        self.pad_5 = QPushButton(self.layoutWidget1)
        self.pad_5.setObjectName(u"pad_5")
        sizePolicy.setHeightForWidth(self.pad_5.sizePolicy().hasHeightForWidth())
        self.pad_5.setSizePolicy(sizePolicy)
        self.pad_5.setFont(font5)
        self.pad_5.setStyleSheet(u"background-color: rgb(178, 201, 171);\n"
"color: rgb(255,255,255);\n"
"border-radius:5px;")

        self.gridLayout_2.addWidget(self.pad_5, 1, 1, 1, 1)

        self.gridLayout_2.setRowStretch(0, 1)
        self.gridLayout_2.setRowStretch(1, 1)
        self.gridLayout_2.setRowStretch(2, 1)
        self.gridLayout_2.setRowStretch(3, 1)

        self.retranslateUi(Form)
        self.button_back.clicked.connect(Form.back_entry)
        self.pad_ok.clicked.connect(Form.check_otp)
        self.pad_back.clicked.connect(Form.click_pad)
        self.pad_1.clicked.connect(Form.click_pad)
        self.pad_2.clicked.connect(Form.click_pad)
        self.pad_3.clicked.connect(Form.click_pad)
        self.pad_4.clicked.connect(Form.click_pad)
        self.pad_5.clicked.connect(Form.click_pad)
        self.pad_6.clicked.connect(Form.click_pad)
        self.pad_7.clicked.connect(Form.click_pad)
        self.pad_9.clicked.connect(Form.click_pad)
        self.pad_8.clicked.connect(Form.click_pad)
        self.pad_0.clicked.connect(Form.click_pad)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_otp.setText(QCoreApplication.translate("Form", u"OTP", None))
        self.button_back.setText("")
        self.logo_label.setText("")
        self.label_2.setText(QCoreApplication.translate("Form", u"\uc6f9 \ud654\uba74\uc5d0 \ud45c\uc2dc\ub41c \uc22b\uc790\ub97c \uc785\ub825\ud574\uc8fc\uc138\uc694", None))
        self.number_3.setText(QCoreApplication.translate("Form", u"1", None))
        self.number_5.setText(QCoreApplication.translate("Form", u"1", None))
        self.number_4.setText(QCoreApplication.translate("Form", u"1", None))
        self.number_1.setText(QCoreApplication.translate("Form", u"1", None))
        self.number_2.setText(QCoreApplication.translate("Form", u"1", None))
        self.number_6.setText(QCoreApplication.translate("Form", u"1", None))
        self.pad_3.setText(QCoreApplication.translate("Form", u"3", None))
        self.pad_1.setText(QCoreApplication.translate("Form", u"1", None))
        self.pad_7.setText(QCoreApplication.translate("Form", u"7", None))
        self.pad_8.setText(QCoreApplication.translate("Form", u"8", None))
        self.pad_ok.setText(QCoreApplication.translate("Form", u"ok", None))
        self.pad_6.setText(QCoreApplication.translate("Form", u"6", None))
        self.pad_0.setText(QCoreApplication.translate("Form", u"0", None))
        self.pad_2.setText(QCoreApplication.translate("Form", u"2", None))
        self.pad_9.setText(QCoreApplication.translate("Form", u"9", None))
        self.pad_4.setText(QCoreApplication.translate("Form", u"4", None))
        self.pad_back.setText(QCoreApplication.translate("Form", u"<", None))
        self.pad_5.setText(QCoreApplication.translate("Form", u"5", None))
    # retranslateUi

