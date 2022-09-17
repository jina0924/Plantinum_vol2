# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'detailUI.ui'
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
from PySide2.QtWidgets import (QApplication, QFrame, QLabel, QProgressBar,
    QPushButton, QSizePolicy, QWidget)
import myres_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1366, 768)
        Form.setLayoutDirection(Qt.LeftToRight)
        Form.setAutoFillBackground(False)
        Form.setStyleSheet(u"background-color: rgb(248, 245, 238);")
        self.back_button = QPushButton(Form)
        self.back_button.setObjectName(u"back_button")
        self.back_button.setGeometry(QRect(1259, 20, 71, 71))
        self.back_button.setAutoFillBackground(False)
        self.back_button.setStyleSheet(u"border-image: url(:/icon/img/return_green.png);")
        self.logo = QPushButton(Form)
        self.logo.setObjectName(u"logo")
        self.logo.setEnabled(False)
        self.logo.setGeometry(QRect(20, 20, 150, 42))
        self.logo.setAutoFillBackground(False)
        self.logo.setStyleSheet(u"border-image: url(:/logo/img/\uff2f\uff34\uff30\uff3f\uff50\uff4c\uff41\uff4e\uff54\uff49\uff4e\uff55\uff4d.png);")
        self.temp_label = QLabel(Form)
        self.temp_label.setObjectName(u"temp_label")
        self.temp_label.setGeometry(QRect(350, 260, 239, 100))
        self.temp_label.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius : 15px;\n"
"\n"
"")
        self.temp_label.setFrameShape(QFrame.Box)
        self.temp_label.setFrameShadow(QFrame.Raised)
        self.temp_label.setLineWidth(10)
        self.temp_label.setMidLineWidth(30)
        self.humi_label = QLabel(Form)
        self.humi_label.setObjectName(u"humi_label")
        self.humi_label.setGeometry(QRect(350, 395, 239, 100))
        self.humi_label.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius : 15px;\n"
"\n"
"")
        self.humi_label.setFrameShape(QFrame.Box)
        self.humi_label.setFrameShadow(QFrame.Raised)
        self.humi_label.setLineWidth(10)
        self.humi_label.setMidLineWidth(30)
        self.soil_label = QLabel(Form)
        self.soil_label.setObjectName(u"soil_label")
        self.soil_label.setGeometry(QRect(350, 530, 239, 100))
        self.soil_label.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius : 15px;\n"
"\n"
"")
        self.soil_label.setFrameShape(QFrame.Box)
        self.soil_label.setFrameShadow(QFrame.Raised)
        self.soil_label.setLineWidth(10)
        self.soil_label.setMidLineWidth(30)
        self.temp_label_text = QLabel(Form)
        self.temp_label_text.setObjectName(u"temp_label_text")
        self.temp_label_text.setGeometry(QRect(350, 280, 50, 60))
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.temp_label_text.setFont(font)
        self.temp_label_text.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(101, 128, 93);")
        self.temp_label_text.setAlignment(Qt.AlignCenter)
        self.bar1 = QLabel(Form)
        self.bar1.setObjectName(u"bar1")
        self.bar1.setGeometry(QRect(415, 270, 1, 81))
        self.bar1.setStyleSheet(u"background-color: rgb(101, 128, 93);")
        self.humi_label_text = QLabel(Form)
        self.humi_label_text.setObjectName(u"humi_label_text")
        self.humi_label_text.setGeometry(QRect(350, 415, 50, 60))
        self.humi_label_text.setFont(font)
        self.humi_label_text.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(101, 128, 93);")
        self.humi_label_text.setAlignment(Qt.AlignCenter)
        self.soil_label_text = QLabel(Form)
        self.soil_label_text.setObjectName(u"soil_label_text")
        self.soil_label_text.setGeometry(QRect(350, 550, 50, 60))
        self.soil_label_text.setFont(font)
        self.soil_label_text.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(101, 128, 93);")
        self.soil_label_text.setAlignment(Qt.AlignCenter)
        self.bar2 = QLabel(Form)
        self.bar2.setObjectName(u"bar2")
        self.bar2.setGeometry(QRect(415, 405, 1, 81))
        self.bar2.setStyleSheet(u"background-color: rgb(101, 128, 93);")
        self.bar3 = QLabel(Form)
        self.bar3.setObjectName(u"bar3")
        self.bar3.setGeometry(QRect(415, 540, 1, 81))
        self.bar3.setStyleSheet(u"background-color: rgb(101, 128, 93);")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(450, 280, 60, 60))
        self.label.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-image: url(:/icon/img/temperature_green.svg);")
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(450, 415, 60, 60))
        self.label_2.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-image: url(:/icon/img/humidity.svg);")
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(450, 550, 60, 60))
        self.label_3.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-image: url(:/icon/img/soil.svg);")
        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(510, 295, 61, 31))
        font1 = QFont()
        font1.setPointSize(18)
        font1.setBold(True)
        self.label_4.setFont(font1)
        self.label_4.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(101, 128, 93);")
        self.label_4.setAlignment(Qt.AlignCenter)
        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(510, 430, 61, 31))
        self.label_5.setFont(font1)
        self.label_5.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(101, 128, 93);")
        self.label_5.setAlignment(Qt.AlignCenter)
        self.label_6 = QLabel(Form)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(510, 565, 61, 31))
        self.label_6.setFont(font1)
        self.label_6.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(101, 128, 93);")
        self.label_6.setAlignment(Qt.AlignCenter)
        self.recent_water_board = QLabel(Form)
        self.recent_water_board.setObjectName(u"recent_water_board")
        self.recent_water_board.setGeometry(QRect(625, 260, 301, 251))
        self.recent_water_board.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius : 15px;\n"
"\n"
"")
        self.recent_water_board.setFrameShape(QFrame.Box)
        self.recent_water_board.setFrameShadow(QFrame.Raised)
        self.recent_water_board.setLineWidth(10)
        self.recent_water_board.setMidLineWidth(30)
        self.label_7 = QLabel(Form)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(650, 275, 151, 41))
        font2 = QFont()
        font2.setPointSize(16)
        font2.setBold(True)
        self.label_7.setFont(font2)
        self.label_7.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(101, 128, 93);")
        self.label_7.setAlignment(Qt.AlignCenter)
        self.label_8 = QLabel(Form)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(660, 340, 250, 40))
        font3 = QFont()
        font3.setPointSize(14)
        self.label_8.setFont(font3)
        self.label_8.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(101, 128, 93);\n"
"border-bottom : 1px solid  rgb(178, 201, 171);\n"
"")
        self.label_8.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_9 = QLabel(Form)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(660, 390, 250, 40))
        self.label_9.setFont(font3)
        self.label_9.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(101, 128, 93);\n"
"border-bottom : 1px solid  rgb(178, 201, 171);")
        self.label_9.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_10 = QLabel(Form)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(660, 440, 250, 40))
        self.label_10.setFont(font3)
        self.label_10.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(101, 128, 93);\n"
"border-bottom : 1px solid  rgb(178, 201, 171);")
        self.label_10.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_11 = QLabel(Form)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(483, 130, 400, 71))
        font4 = QFont()
        font4.setPointSize(28)
        font4.setBold(True)
        self.label_11.setFont(font4)
        self.label_11.setStyleSheet(u"color: rgb(101, 128, 93);")
        self.label_11.setAlignment(Qt.AlignCenter)
        self.recent_water_board_2 = QLabel(Form)
        self.recent_water_board_2.setObjectName(u"recent_water_board_2")
        self.recent_water_board_2.setGeometry(QRect(955, 260, 100, 251))
        self.recent_water_board_2.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius : 15px;\n"
"\n"
"")
        self.recent_water_board_2.setFrameShape(QFrame.Box)
        self.recent_water_board_2.setFrameShadow(QFrame.Raised)
        self.recent_water_board_2.setLineWidth(10)
        self.recent_water_board_2.setMidLineWidth(30)
        self.progressBar = QProgressBar(Form)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(965, 310, 81, 181))
        self.progressBar.setAutoFillBackground(False)
        self.progressBar.setStyleSheet(u"border-radius: 15px;\n"
"background-color : rgb(255,255,255);\n"
"")
        self.progressBar.setValue(80)
        self.progressBar.setAlignment(Qt.AlignCenter)
        self.progressBar.setTextVisible(False)
        self.progressBar.setOrientation(Qt.Vertical)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setTextDirection(QProgressBar.TopToBottom)
        self.progressBar.setStyleSheet(u"border-radius: 15px;\n"
                                       "background-color : rgb(255,255,255);\n"
                                       "")
        self.progressBar.setStyleSheet(
            "QProgressBar::chunk { background-color : rgb(101, 128, 93) ; border-radius : 10px;} QProgressBar {background-color : rgb(255,255,255);border-radius : 15px;}")


        self.label_12 = QLabel(Form)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(970, 275, 71, 20))
        font5 = QFont()
        font5.setPointSize(10)
        self.label_12.setFont(font5)
        self.label_12.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(101, 128, 93);")
        self.label_12.setAlignment(Qt.AlignCenter)
        self.sleep_button = QPushButton(Form)
        self.sleep_button.setObjectName(u"sleep_button")
        self.sleep_button.setGeometry(QRect(640, 530, 100, 100))
        self.sleep_button.setStyleSheet(u"background-color: rgb(178, 201, 171);\n"
"border-image: url(:/icon/img/moon.svg);\n"
"border-radius : 20px;")
        self.reset_button = QPushButton(Form)
        self.reset_button.setObjectName(u"reset_button")
        self.reset_button.setGeometry(QRect(800, 530, 100, 100))
        self.reset_button.setStyleSheet(u"background-color: rgb(140, 165, 133);\n"
"image: url(:/icon/img/redo.svg);\n"
"border-radius : 20px;")
        self.exit_button = QPushButton(Form)
        self.exit_button.setObjectName(u"exit_button")
        self.exit_button.setGeometry(QRect(955, 530, 100, 100))
        self.exit_button.setStyleSheet(u"background-color: rgb(101, 128, 93);\n"
"border-image: url(:/icon/img/power-off.svg);\n"
"border-radius : 20px;")
        self.label_13 = QLabel(Form)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(640, 640, 100, 20))
        font6 = QFont()
        font6.setPointSize(11)
        font6.setBold(True)
        self.label_13.setFont(font6)
        self.label_13.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(178, 201, 171);")
        self.label_13.setAlignment(Qt.AlignCenter)
        self.label_14 = QLabel(Form)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(800, 640, 100, 20))
        self.label_14.setFont(font6)
        self.label_14.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(140, 165, 133);")
        self.label_14.setAlignment(Qt.AlignCenter)
        self.label_15 = QLabel(Form)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(955, 640, 100, 20))
        self.label_15.setFont(font6)
        self.label_15.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(101, 128, 93);")
        self.label_15.setAlignment(Qt.AlignCenter)

        self.retranslateUi(Form)
        self.back_button.clicked.connect(Form.go_mainpage)
        self.sleep_button.clicked.connect(Form.sleep_mode)
        self.reset_button.clicked.connect(Form.redo)
        self.exit_button.clicked.connect(Form.turnoff)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.back_button.setText("")
        self.logo.setText("")
        self.temp_label.setText("")
        self.humi_label.setText("")
        self.soil_label.setText("")
        self.temp_label_text.setText(QCoreApplication.translate("Form", u"<html><head/><body><p>\ud604\uc7ac</p><p>\uc628\ub3c4</p></body></html>", None))
        self.bar1.setText("")
        self.humi_label_text.setText(QCoreApplication.translate("Form", u"<html><head/><body><p>\ud604\uc7ac</p><p>\uc2b5\ub3c4</p></body></html>", None))
        self.soil_label_text.setText(QCoreApplication.translate("Form", u"<html><head/><body><p>\ud1a0\uc591</p><p>\uc218\ubd84</p></body></html>", None))
        self.bar2.setText("")
        self.bar3.setText("")
        self.label.setText("")
        self.label_2.setText("")
        self.label_3.setText("")
        self.label_4.setText(QCoreApplication.translate("Form", u"27\u00baC", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"27%", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"27%", None))
        self.recent_water_board.setText("")
        self.label_7.setText(QCoreApplication.translate("Form", u"\ucd5c\uadfc \uad00\uc218 \uc2dc\uac04", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"2022.07.08 15:03", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"2022.07.15 06:08", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"2022.07.29 08:29", None))
        self.label_11.setText(QCoreApplication.translate("Form", u"\ub69c\ubc85\ucd08", None))
        self.recent_water_board_2.setText("")
        self.label_12.setText(QCoreApplication.translate("Form", u"\ubb3c\ud1b5 \uc54c\ub9ac\ubbf8", None))
        self.sleep_button.setText("")
        self.reset_button.setText("")
        self.exit_button.setText("")
        self.label_13.setText(QCoreApplication.translate("Form", u"\ucde8\uce68 \ubaa8\ub4dc", None))
        self.label_14.setText(QCoreApplication.translate("Form", u"\ucd08\uae30\ud654", None))
        self.label_15.setText(QCoreApplication.translate("Form", u"\uc885\ub8cc", None))
    # retranslateUi

