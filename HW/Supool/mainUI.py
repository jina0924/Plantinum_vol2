# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainUI.ui'
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
from PySide2.QtWidgets import (QApplication, QFrame, QLabel, QPushButton,
    QSizePolicy, QWidget,QGraphicsOpacityEffect)
import myres_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1366, 768)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setStyleSheet(u"")
        self.clock = QLabel(Form)
        self.clock.setObjectName(u"clock")
        self.clock.setGeometry(QRect(533, 30, 300, 100))
        font = QFont()
        font.setFamilies([u"\ub9d1\uc740 \uace0\ub515"])
        font.setPointSize(50)
        font.setBold(True)
        self.clock.setFont(font)
        self.clock.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(70, 139, 0);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.clock.setFrameShape(QFrame.NoFrame)
        self.clock.setAlignment(Qt.AlignCenter)
        self.clock.setWordWrap(False)
        self.water = QLabel(Form)
        self.water.setObjectName(u"water")
        self.water.setGeometry(QRect(0, 0, 1366, 768))
        font1 = QFont()
        font1.setBold(True)
        font1.setUnderline(False)
        self.water.setFont(font1)
        #self.water.setStyleSheet(u"border-image: url(:/img/img/background_sand.jpg);")
        #self.water.setStyleSheet(u"background-color : srgb(40,40,30);")
        self.water.setStyleSheet(u"border-image:url(./img/icc_background_sand.png);")
        self.water.setFrameShape(QFrame.NoFrame)
        self.water.setScaledContents(False)
        self.water.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.water.setWordWrap(False)
        self.detail_button = QPushButton(Form)
        self.detail_button.setObjectName(u"detail_button")
        self.detail_button.setGeometry(QRect(0, 0, 1366, 768))
        #self.detail_button.setStyleSheet(u"color: rgba(255, 255, 255, 0);background-ccolor:srgba(255,255,255,0);")
        #self.detail_button.hide()
        opacity_effect = QGraphicsOpacityEffect(self.detail_button)
        opacity_effect.setOpacity(0)
        self.detail_button.setGraphicsEffect(opacity_effect)
        
        self.detail_button.setStyleSheet(u'backgroud:transparent')
        self.wave = QLabel(Form)
        self.wave.setObjectName(u"wave")
        self.wave.setGeometry(QRect(0, 120, 1366, 768))
        self.wave.setFont(font1)
        #self.wave.setStyleSheet(u"border-image: url(:/img/img/wave.png);")
        #self.wave.setStyleSheet(u"background-color:rgb(40,40,180);")
        self.wave.setStyleSheet(u"border-image:url(./img/icc_wave.png);")
        self.wave.setFrameShape(QFrame.NoFrame)
        self.wave.setScaledContents(False)
        self.wave.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.wave.setWordWrap(False)
        self.notice_icon = QLabel(Form)
        self.notice_icon.setObjectName(u"notice_icon")
        self.notice_icon.setGeometry(QRect(20, 20, 50, 50))
        self.notice_icon.setStyleSheet(u"border-image: url(:/icon/img/bell_white.png);")
        self.humi_icon = QLabel(Form)
        self.humi_icon.setObjectName(u"humi_icon")
        self.humi_icon.setGeometry(QRect(1080, 20, 50, 50))
        self.humi_icon.setStyleSheet(u"border-image: url(:/icon/img/water_white.png);")
        self.temp_icon = QLabel(Form)
        self.temp_icon.setObjectName(u"temp_icon")
        self.temp_icon.setGeometry(QRect(1220, 20, 50, 50))
        self.temp_icon.setStyleSheet(u"border-image: url(:/icon/img/temperature_white.png);")
        self.humi_label = QLabel(Form)
        self.humi_label.setObjectName(u"humi_label")
        self.humi_label.setGeometry(QRect(1140, 20, 85, 41))
        font2 = QFont()
        font2.setPointSize(24)
        font2.setBold(True)
        self.humi_label.setFont(font2)
        self.humi_label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.humi_label.setAlignment(Qt.AlignCenter)
        self.temp_label = QLabel(Form)
        self.temp_label.setObjectName(u"temp_label")
        self.temp_label.setGeometry(QRect(1270, 20, 85, 41))
        self.temp_label.setFont(font2)
        self.temp_label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.temp_label.setAlignment(Qt.AlignCenter)
        self.warn_label = QLabel(Form)
        self.warn_label.setObjectName(u"warn_label")
        self.warn_label.setGeometry(QRect(80, 25, 231, 41))
        font3 = QFont()
        font3.setPointSize(16)
        font3.setBold(True)
        self.warn_label.setFont(font3)
        self.warn_label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.warn_label.setAlignment(Qt.AlignCenter)
        
        self.water.raise_()
        self.wave.raise_()
        self.clock.raise_()
        self.notice_icon.raise_()
        self.humi_icon.raise_()
        self.temp_icon.raise_()
        self.humi_label.raise_()
        self.temp_label.raise_()
        self.warn_label.raise_()
        self.detail_button.raise_()

        self.retranslateUi(Form)
        self.detail_button.clicked.connect(Form.go_detailPage)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.clock.setText("")
        self.water.setText("")
        self.detail_button.setText("")
        self.wave.setText("")
        self.notice_icon.setText("")
        self.humi_icon.setText("")
        self.temp_icon.setText("")
        self.humi_label.setText(QCoreApplication.translate("Form", u"27%", None))
        self.temp_label.setText(QCoreApplication.translate("Form", u"27\u00baC", None))
        self.warn_label.setText(QCoreApplication.translate("Form", u"\ubb3c\ud1b5\uc5d0 \ubb3c\uc744 \ucc44\uc6cc\uc8fc\uc138\uc694", None))
    # retranslateUi

