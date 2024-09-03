# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialog_motorcontroller.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
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
from PySide6.QtWidgets import (QApplication, QDialog, QListWidget, QListWidgetItem,
    QPlainTextEdit, QPushButton, QSizePolicy, QSpinBox,
    QTextEdit, QWidget)

class Ui_Dialog_MotorController(object):
    def setupUi(self, Dialog_MotorController):
        if not Dialog_MotorController.objectName():
            Dialog_MotorController.setObjectName(u"Dialog_MotorController")
        Dialog_MotorController.resize(395, 340)
        self.DO_IT = QPushButton(Dialog_MotorController)
        self.DO_IT.setObjectName(u"DO_IT")
        self.DO_IT.setGeometry(QRect(250, 280, 100, 31))
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
        self.listWidget = QListWidget(Dialog_MotorController)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(25, 200, 200, 110))
        self.LOAD_ROUTE = QPushButton(Dialog_MotorController)
        self.LOAD_ROUTE.setObjectName(u"LOAD_ROUTE")
        self.LOAD_ROUTE.setGeometry(QRect(250, 240, 100, 30))
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
        self.HOME_CONOR.setGeometry(QRect(25, 160, 171, 32))

        self.retranslateUi(Dialog_MotorController)

        QMetaObject.connectSlotsByName(Dialog_MotorController)
    # setupUi

    def retranslateUi(self, Dialog_MotorController):
        Dialog_MotorController.setWindowTitle(QCoreApplication.translate("Dialog_MotorController", u"Dialog", None))
        self.DO_IT.setText(QCoreApplication.translate("Dialog_MotorController", u"Do it!", None))
#if QT_CONFIG(shortcut)
        self.DO_IT.setShortcut(QCoreApplication.translate("Dialog_MotorController", u"Up", None))
#endif // QT_CONFIG(shortcut)
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

        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        ___qlistwidgetitem = self.listWidget.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("Dialog_MotorController", u"IGNORE THESE", None));
        ___qlistwidgetitem1 = self.listWidget.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("Dialog_MotorController", u"1 - line", None));
        ___qlistwidgetitem2 = self.listWidget.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("Dialog_MotorController", u"2 - square", None));
        self.listWidget.setSortingEnabled(__sortingEnabled)

        self.LOAD_ROUTE.setText(QCoreApplication.translate("Dialog_MotorController", u"Load", None))
        self.textEdit_5.setHtml(QCoreApplication.translate("Dialog_MotorController", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'.AppleSystemUIFont'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Distance</p></body></html>", None))
        self.RIGHT.setText(QCoreApplication.translate("Dialog_MotorController", u"RIGHT", None))
#if QT_CONFIG(shortcut)
        self.RIGHT.setShortcut(QCoreApplication.translate("Dialog_MotorController", u"Right", None))
#endif // QT_CONFIG(shortcut)
        self.HOME.setText(QCoreApplication.translate("Dialog_MotorController", u"HOME", None))
        self.X_POS_4.setPlainText(QCoreApplication.translate("Dialog_MotorController", u"steps\n"
"", None))
        self.HOME_CONOR.setText(QCoreApplication.translate("Dialog_MotorController", u"Home - but only for Conor", None))
    # retranslateUi

