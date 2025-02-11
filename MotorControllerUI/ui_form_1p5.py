# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialog_motorcontroller_1.5.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDialog, QLabel,
    QListWidget, QListWidgetItem, QPlainTextEdit, QPushButton,
    QSizePolicy, QSpinBox, QTextEdit, QWidget)

from PySide6.QtGui import Qt
from PySide6 import QtGui
from PySide6.QtCore import QRectF

class MySwitch(QPushButton):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setCheckable(True)
        self.setMinimumWidth(66)
        self.setMinimumHeight(22)

    def paintEvent(self, event, force_on=False, force_off=False):

        label = "ON" if self.isChecked() else "OFF"
        bg_color = Qt.green if self.isChecked() else Qt.red

        if force_on:
            label = "ON"
            bg_color=Qt.green
        if force_off:
            label="OFF"
            bg_color=Qt.red

        radius = 10
        width = 32
        center = self.rect().center()

        painter = QtGui.QPainter(self)
        painter.setRenderHint(QtGui.QPainter.Antialiasing)
        painter.translate(center)
        painter.setBrush(QtGui.QColor(0,0,0))

        pen = QtGui.QPen(Qt.black)
        pen.setWidth(2)
        painter.setPen(pen)

        painter.drawRoundedRect(QRect(-width, -radius, 2*width, 2*radius), radius, radius)
        painter.setBrush(QtGui.QBrush(bg_color))
        sw_rect = QRect(-radius, -radius, width + radius, 2*radius)

        if not (force_on or force_off):
            if not self.isChecked():
                sw_rect.moveLeft(-width)
        elif force_on:
            sw_rect.moveLeft(-width)

        painter.drawRoundedRect(sw_rect, radius, radius)
        painter.drawText(sw_rect, Qt.AlignCenter, label)


class Ui_Dialog_MotorController(object):
    def setupUi(self, Dialog_MotorController):
        if not Dialog_MotorController.objectName():
            Dialog_MotorController.setObjectName(u"Dialog_MotorController")
        Dialog_MotorController.resize(410, 641)
        self.EXPOSE = QPushButton(Dialog_MotorController)
        self.EXPOSE.setObjectName(u"EXPOSE")
        self.EXPOSE.setGeometry(QRect(250, 400, 100, 31))
        self.MOVE_MOTORS_ARROW_SETTING = QSpinBox(Dialog_MotorController)
        self.MOVE_MOTORS_ARROW_SETTING.setObjectName(u"MOVE_MOTORS_ARROW_SETTING")
        self.MOVE_MOTORS_ARROW_SETTING.setGeometry(QRect(25, 80, 131, 30))
        self.MOVE_MOTORS_ARROW_SETTING.setMaximum(24000)
        self.MOVE_MOTORS_ARROW_SETTING.setValue(10)
        self.DOWN = QPushButton(Dialog_MotorController)
        self.DOWN.setObjectName(u"DOWN")
        self.DOWN.setGeometry(QRect(245, 120, 70, 30))
        self.LEFT = QPushButton(Dialog_MotorController)
        self.LEFT.setObjectName(u"LEFT")
        self.LEFT.setGeometry(QRect(200, 80, 60, 30))
        self.UP = QPushButton(Dialog_MotorController)
        self.UP.setObjectName(u"UP")
        self.UP.setGeometry(QRect(245, 40, 70, 30))
        self.LED_SETTINGS_BOX = QListWidget(Dialog_MotorController)
        QListWidgetItem(self.LED_SETTINGS_BOX)
        QListWidgetItem(self.LED_SETTINGS_BOX)
        QListWidgetItem(self.LED_SETTINGS_BOX)
        self.LED_SETTINGS_BOX.setObjectName(u"LED_SETTINGS_BOX")
        self.LED_SETTINGS_BOX.setGeometry(QRect(20, 550, 200, 61))
        self.SET_LED_CURRENTS = QPushButton(Dialog_MotorController)
        self.SET_LED_CURRENTS.setObjectName(u"SET_LED_CURRENTS")
        self.SET_LED_CURRENTS.setGeometry(QRect(250, 480, 100, 30))
        self.RIGHT = QPushButton(Dialog_MotorController)
        self.RIGHT.setObjectName(u"RIGHT")
        self.RIGHT.setGeometry(QRect(300, 80, 60, 30))
        self.HOME = QPushButton(Dialog_MotorController)
        self.HOME.setObjectName(u"HOME")
        self.HOME.setGeometry(QRect(250, 340, 100, 30))
        self.HOME_CONOR = QPushButton(Dialog_MotorController)
        self.HOME_CONOR.setObjectName(u"HOME_CONOR")
        self.HOME_CONOR.setGeometry(QRect(20, 270, 171, 32))
        self.UV_ON_CHECKBOX = MySwitch(Dialog_MotorController)
        self.UV_ON_CHECKBOX.setObjectName(u"UV_ON_CHECKBOX")
        self.UV_ON_CHECKBOX.setGeometry(QRect(260, 580, 81, 20))
        self.EXPOSURE_TIME_SETTING = QSpinBox(Dialog_MotorController)
        self.EXPOSURE_TIME_SETTING.setObjectName(u"EXPOSURE_TIME_SETTING")
        self.EXPOSURE_TIME_SETTING.setGeometry(QRect(25, 400, 60, 30))
        self.EXPOSURE_TIME_SETTING.setMaximum(1000)
        self.EXPOSURE_TIME_SETTING.setValue(10)
        self.label = QLabel(Dialog_MotorController)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(90, 410, 49, 16))
        self.RED_CURRENT_SETTING = QSpinBox(Dialog_MotorController)
        self.RED_CURRENT_SETTING.setObjectName(u"RED_CURRENT_SETTING")
        self.RED_CURRENT_SETTING.setGeometry(QRect(80, 500, 60, 30))
        self.RED_CURRENT_SETTING.setMaximum(1000)
        self.RED_CURRENT_SETTING.setValue(10)
        self.label_2 = QLabel(Dialog_MotorController)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(150, 510, 49, 16))
        self.UV_CURRENT_SETTING = QSpinBox(Dialog_MotorController)
        self.UV_CURRENT_SETTING.setObjectName(u"UV_CURRENT_SETTING")
        self.UV_CURRENT_SETTING.setGeometry(QRect(80, 470, 60, 30))
        self.UV_CURRENT_SETTING.setMaximum(1000)
        self.UV_CURRENT_SETTING.setValue(10)
        self.label_3 = QLabel(Dialog_MotorController)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(150, 480, 49, 16))
        self.label_4 = QLabel(Dialog_MotorController)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(30, 510, 49, 16))
        self.label_5 = QLabel(Dialog_MotorController)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(30, 480, 49, 16))
        self.label_6 = QLabel(Dialog_MotorController)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(25, 380, 101, 16))
        self.PREVIOUS_EXPOSURE_TIME_ = QLabel(Dialog_MotorController)
        self.PREVIOUS_EXPOSURE_TIME_.setObjectName(u"PREVIOUS_EXPOSURE_TIME_")
        self.PREVIOUS_EXPOSURE_TIME_.setGeometry(QRect(25, 440, 161, 16))
        self.listWidget = QListWidget(Dialog_MotorController)
        QListWidgetItem(self.listWidget)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(20, 310, 200, 61))
        self.label_7 = QLabel(Dialog_MotorController)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(270, 560, 49, 16))
        self.ABS_Y = QSpinBox(Dialog_MotorController)
        self.ABS_Y.setObjectName(u"ABS_Y")
        self.ABS_Y.setGeometry(QRect(60, 220, 131, 30))
        self.ABS_Y.setMaximum(24000)
        self.ABS_Y.setValue(10)
        self.ABS_X = QSpinBox(Dialog_MotorController)
        self.ABS_X.setObjectName(u"ABS_X")
        self.ABS_X.setGeometry(QRect(60, 180, 131, 30))
        self.ABS_X.setMaximum(24000)
        self.ABS_X.setValue(10)
        self.label_8 = QLabel(Dialog_MotorController)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(30, 30, 181, 41))
        font = QFont()
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_9 = QLabel(Dialog_MotorController)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(30, 140, 181, 41))
        self.label_9.setFont(font)
        self.label_10 = QLabel(Dialog_MotorController)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(30, 180, 21, 31))
        self.label_10.setFont(font)
        self.label_11 = QLabel(Dialog_MotorController)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(30, 220, 21, 31))
        self.label_11.setFont(font)
        self.MOVE = QPushButton(Dialog_MotorController)
        self.MOVE.setObjectName(u"MOVE")
        self.MOVE.setGeometry(QRect(250, 220, 100, 30))

        self.retranslateUi(Dialog_MotorController)

        QMetaObject.connectSlotsByName(Dialog_MotorController)
    # setupUi

    def retranslateUi(self, Dialog_MotorController):
        Dialog_MotorController.setWindowTitle(QCoreApplication.translate("Dialog_MotorController", u"Dialog", None))
        self.EXPOSE.setText(QCoreApplication.translate("Dialog_MotorController", u"Expose", None))
        self.MOVE_MOTORS_ARROW_SETTING.setSuffix(QCoreApplication.translate("Dialog_MotorController", u" um", None))
        self.DOWN.setText(QCoreApplication.translate("Dialog_MotorController", u"DOWN", None))
#if QT_CONFIG(shortcut)
        self.DOWN.setShortcut(QCoreApplication.translate("Dialog_MotorController", u"Down", None))
#endif // QT_CONFIG(shortcut)
        self.LEFT.setText(QCoreApplication.translate("Dialog_MotorController", u"LEFT", None))
#if QT_CONFIG(shortcut)
        self.LEFT.setShortcut(QCoreApplication.translate("Dialog_MotorController", u"Left", None))
#endif // QT_CONFIG(shortcut)
        self.UP.setText(QCoreApplication.translate("Dialog_MotorController", u"UP", None))
#if QT_CONFIG(shortcut)
        self.UP.setShortcut(QCoreApplication.translate("Dialog_MotorController", u"Up", None))
#endif // QT_CONFIG(shortcut)

        __sortingEnabled = self.LED_SETTINGS_BOX.isSortingEnabled()
        self.LED_SETTINGS_BOX.setSortingEnabled(False)
        ___qlistwidgetitem = self.LED_SETTINGS_BOX.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("Dialog_MotorController", u"LED Settings", None));
        ___qlistwidgetitem1 = self.LED_SETTINGS_BOX.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("Dialog_MotorController", u"RED: ", None));
        ___qlistwidgetitem2 = self.LED_SETTINGS_BOX.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("Dialog_MotorController", u"UV: ", None));
        self.LED_SETTINGS_BOX.setSortingEnabled(__sortingEnabled)

        self.SET_LED_CURRENTS.setText(QCoreApplication.translate("Dialog_MotorController", u"Set LED Currents", None))
        self.RIGHT.setText(QCoreApplication.translate("Dialog_MotorController", u"RIGHT", None))
#if QT_CONFIG(shortcut)
        self.RIGHT.setShortcut(QCoreApplication.translate("Dialog_MotorController", u"Right", None))
#endif // QT_CONFIG(shortcut)
        self.HOME.setText(QCoreApplication.translate("Dialog_MotorController", u"HOME", None))
        self.HOME_CONOR.setText(QCoreApplication.translate("Dialog_MotorController", u"Home - but only for Conor", None))
        self.UV_ON_CHECKBOX.setText(QCoreApplication.translate("Dialog_MotorController", u"UV light on", None))
        self.label.setText(QCoreApplication.translate("Dialog_MotorController", u"Seconds", None))
        self.label_2.setText(QCoreApplication.translate("Dialog_MotorController", u"mA", None))
        self.label_3.setText(QCoreApplication.translate("Dialog_MotorController", u"mA", None))
        self.label_4.setText(QCoreApplication.translate("Dialog_MotorController", u"Red LED", None))
        self.label_5.setText(QCoreApplication.translate("Dialog_MotorController", u"UV LED", None))
        self.label_6.setText(QCoreApplication.translate("Dialog_MotorController", u"Exposure Time:", None))
        self.PREVIOUS_EXPOSURE_TIME_.setText(QCoreApplication.translate("Dialog_MotorController", u"Most Recent Exposure Time: ", None))

        __sortingEnabled1 = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        ___qlistwidgetitem3 = self.listWidget.item(0)
        ___qlistwidgetitem3.setText(QCoreApplication.translate("Dialog_MotorController", u"Motor Position:", None));
        self.listWidget.setSortingEnabled(__sortingEnabled1)

        self.label_7.setText(QCoreApplication.translate("Dialog_MotorController", u"UV Light", None))
        self.ABS_Y.setSuffix(QCoreApplication.translate("Dialog_MotorController", u" um", None))
        self.ABS_X.setSuffix(QCoreApplication.translate("Dialog_MotorController", u" um", None))
        self.label_8.setText(QCoreApplication.translate("Dialog_MotorController", u"Distance (Move Relative)", None))
        self.label_9.setText(QCoreApplication.translate("Dialog_MotorController", u"Position (Move Absolute)", None))
        self.label_10.setText(QCoreApplication.translate("Dialog_MotorController", u"X", None))
        self.label_11.setText(QCoreApplication.translate("Dialog_MotorController", u"Y", None))
        self.MOVE.setText(QCoreApplication.translate("Dialog_MotorController", u"MOVE", None))
    # retranslateUi

