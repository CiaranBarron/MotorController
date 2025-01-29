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

class Ui_Dialog_MotorController(object):
    def setupUi(self, Dialog_MotorController):
        if not Dialog_MotorController.objectName():
            Dialog_MotorController.setObjectName(u"Dialog_MotorController")
        Dialog_MotorController.resize(395, 511)
        self.EXPOSE = QPushButton(Dialog_MotorController)
        self.EXPOSE.setObjectName(u"EXPOSE")
        self.EXPOSE.setGeometry(QRect(250, 280, 100, 31))
        self.MOVE_MOTORS_ARROW_SETTING = QSpinBox(Dialog_MotorController)
        self.MOVE_MOTORS_ARROW_SETTING.setObjectName(u"MOVE_MOTORS_ARROW_SETTING")
        self.MOVE_MOTORS_ARROW_SETTING.setGeometry(QRect(25, 80, 60, 30))
        self.MOVE_MOTORS_ARROW_SETTING.setMaximum(1000)
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
        self.LED_SETTINGS_BOX.setGeometry(QRect(20, 430, 200, 61))
        self.SET_LED_CURRENTS = QPushButton(Dialog_MotorController)
        self.SET_LED_CURRENTS.setObjectName(u"SET_LED_CURRENTS")
        self.SET_LED_CURRENTS.setGeometry(QRect(250, 360, 100, 30))
        self.textEdit_5 = QTextEdit(Dialog_MotorController)
        self.textEdit_5.setObjectName(u"textEdit_5")
        self.textEdit_5.setGeometry(QRect(25, 40, 100, 30))
        self.RIGHT = QPushButton(Dialog_MotorController)
        self.RIGHT.setObjectName(u"RIGHT")
        self.RIGHT.setGeometry(QRect(300, 80, 60, 30))
        self.HOME = QPushButton(Dialog_MotorController)
        self.HOME.setObjectName(u"HOME")
        self.HOME.setGeometry(QRect(250, 200, 100, 30))
        self.X_POS_4 = QPlainTextEdit(Dialog_MotorController)
        self.X_POS_4.setObjectName(u"X_POS_4")
        self.X_POS_4.setGeometry(QRect(100, 80, 70, 30))
        self.HOME_CONOR = QPushButton(Dialog_MotorController)
        self.HOME_CONOR.setObjectName(u"HOME_CONOR")
        self.HOME_CONOR.setGeometry(QRect(25, 130, 171, 32))
        self.UV_ON_CHECKBOX = QCheckBox(Dialog_MotorController)
        self.UV_ON_CHECKBOX.setObjectName(u"UV_ON_CHECKBOX")
        self.UV_ON_CHECKBOX.setGeometry(QRect(230, 430, 81, 20))
        self.EXPOSURE_TIME_SETTING = QSpinBox(Dialog_MotorController)
        self.EXPOSURE_TIME_SETTING.setObjectName(u"EXPOSURE_TIME_SETTING")
        self.EXPOSURE_TIME_SETTING.setGeometry(QRect(25, 280, 60, 30))
        self.EXPOSURE_TIME_SETTING.setMaximum(1000)
        self.EXPOSURE_TIME_SETTING.setValue(10)
        self.label = QLabel(Dialog_MotorController)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(90, 290, 49, 16))
        self.RED_CURRENT_SETTING = QSpinBox(Dialog_MotorController)
        self.RED_CURRENT_SETTING.setObjectName(u"RED_CURRENT_SETTING")
        self.RED_CURRENT_SETTING.setGeometry(QRect(80, 380, 60, 30))
        self.RED_CURRENT_SETTING.setMaximum(1000)
        self.RED_CURRENT_SETTING.setValue(10)
        self.label_2 = QLabel(Dialog_MotorController)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(150, 390, 49, 16))
        self.UV_CURRENT_SETTING = QSpinBox(Dialog_MotorController)
        self.UV_CURRENT_SETTING.setObjectName(u"UV_CURRENT_SETTING")
        self.UV_CURRENT_SETTING.setGeometry(QRect(80, 350, 60, 30))
        self.UV_CURRENT_SETTING.setMaximum(1000)
        self.UV_CURRENT_SETTING.setValue(10)
        self.label_3 = QLabel(Dialog_MotorController)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(150, 360, 49, 16))
        self.label_4 = QLabel(Dialog_MotorController)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(30, 390, 49, 16))
        self.label_5 = QLabel(Dialog_MotorController)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(30, 360, 49, 16))
        self.label_6 = QLabel(Dialog_MotorController)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(25, 260, 101, 16))
        self.PREVIOUS_EXPOSURE_TIME_ = QLabel(Dialog_MotorController)
        self.PREVIOUS_EXPOSURE_TIME_.setObjectName(u"PREVIOUS_EXPOSURE_TIME_")
        self.PREVIOUS_EXPOSURE_TIME_.setGeometry(QRect(25, 320, 161, 16))
        self.listWidget = QListWidget(Dialog_MotorController)
        QListWidgetItem(self.listWidget)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(20, 170, 200, 61))

        self.retranslateUi(Dialog_MotorController)

        QMetaObject.connectSlotsByName(Dialog_MotorController)
    # setupUi

    def retranslateUi(self, Dialog_MotorController):
        Dialog_MotorController.setWindowTitle(QCoreApplication.translate("Dialog_MotorController", u"Dialog", None))
        self.EXPOSE.setText(QCoreApplication.translate("Dialog_MotorController", u"Expose", None))
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
        self.textEdit_5.setHtml(QCoreApplication.translate("Dialog_MotorController", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'.AppleSystemUIFont'; font-size:13pt;\">Distance</span></p></body></html>", None))
        self.RIGHT.setText(QCoreApplication.translate("Dialog_MotorController", u"RIGHT", None))
#if QT_CONFIG(shortcut)
        self.RIGHT.setShortcut(QCoreApplication.translate("Dialog_MotorController", u"Right", None))
#endif // QT_CONFIG(shortcut)
        self.HOME.setText(QCoreApplication.translate("Dialog_MotorController", u"HOME", None))
        self.X_POS_4.setPlainText(QCoreApplication.translate("Dialog_MotorController", u"um\n"
"", None))
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

    # retranslateUi

