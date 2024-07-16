# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialog_motorcontroller.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QListWidget,
    QListWidgetItem, QPlainTextEdit, QPushButton, QSizePolicy,
    QSpinBox, QTextEdit, QWidget)

class Ui_Dialog_MotorController(object):
    def setupUi(self, Dialog_MotorController):
        if not Dialog_MotorController.objectName():
            Dialog_MotorController.setObjectName(u"Dialog_MotorController")
        Dialog_MotorController.resize(488, 755)
        self.Y_POS_SET = QSpinBox(Dialog_MotorController)
        self.Y_POS_SET.setObjectName(u"Y_POS_SET")
        self.Y_POS_SET.setGeometry(QRect(210, 530, 51, 30))
        self.X_POS_SET = QSpinBox(Dialog_MotorController)
        self.X_POS_SET.setObjectName(u"X_POS_SET")
        self.X_POS_SET.setGeometry(QRect(210, 480, 51, 30))
        self.DO_IT = QPushButton(Dialog_MotorController)
        self.DO_IT.setObjectName(u"DO_IT")
        self.DO_IT.setGeometry(QRect(380, 500, 61, 32))
        self.STAGE_FRAME = QFrame(Dialog_MotorController)
        self.STAGE_FRAME.setObjectName(u"STAGE_FRAME")
        self.STAGE_FRAME.setGeometry(QRect(30, 20, 411, 271))
        self.STAGE_FRAME.setFrameShape(QFrame.StyledPanel)
        self.STAGE_FRAME.setFrameShadow(QFrame.Raised)
        self.X_POS = QPlainTextEdit(Dialog_MotorController)
        self.X_POS.setObjectName(u"X_POS")
        self.X_POS.setGeometry(QRect(120, 480, 80, 30))
        self.Y_POS = QPlainTextEdit(Dialog_MotorController)
        self.Y_POS.setObjectName(u"Y_POS")
        self.Y_POS.setGeometry(QRect(120, 530, 80, 30))
        self.NEW_MOTOR_POS_TEXT = QTextEdit(Dialog_MotorController)
        self.NEW_MOTOR_POS_TEXT.setObjectName(u"NEW_MOTOR_POS_TEXT")
        self.NEW_MOTOR_POS_TEXT.setGeometry(QRect(210, 440, 80, 30))
        self.MOVE_MOTORS_ARROW_SETTING = QSpinBox(Dialog_MotorController)
        self.MOVE_MOTORS_ARROW_SETTING.setObjectName(u"MOVE_MOTORS_ARROW_SETTING")
        self.MOVE_MOTORS_ARROW_SETTING.setGeometry(QRect(230, 360, 50, 30))
        self.DOWN = QPushButton(Dialog_MotorController)
        self.DOWN.setObjectName(u"DOWN")
        self.DOWN.setGeometry(QRect(80, 380, 70, 30))
        self.LEFT = QPushButton(Dialog_MotorController)
        self.LEFT.setObjectName(u"LEFT")
        self.LEFT.setGeometry(QRect(50, 350, 60, 30))
        self.UP = QPushButton(Dialog_MotorController)
        self.UP.setObjectName(u"UP")
        self.UP.setGeometry(QRect(80, 320, 70, 30))
        self.listWidget = QListWidget(Dialog_MotorController)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(30, 610, 221, 111))
        self.LOAD_ROUTE = QPushButton(Dialog_MotorController)
        self.LOAD_ROUTE.setObjectName(u"LOAD_ROUTE")
        self.LOAD_ROUTE.setGeometry(QRect(290, 620, 100, 32))
        self.textEdit = QTextEdit(Dialog_MotorController)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(120, 440, 80, 30))
        self.textEdit_2 = QTextEdit(Dialog_MotorController)
        self.textEdit_2.setObjectName(u"textEdit_2")
        self.textEdit_2.setGeometry(QRect(30, 440, 80, 30))
        self.textEdit_3 = QTextEdit(Dialog_MotorController)
        self.textEdit_3.setObjectName(u"textEdit_3")
        self.textEdit_3.setGeometry(QRect(30, 480, 80, 30))
        self.textEdit_4 = QTextEdit(Dialog_MotorController)
        self.textEdit_4.setObjectName(u"textEdit_4")
        self.textEdit_4.setGeometry(QRect(30, 530, 80, 30))
        self.textEdit_5 = QTextEdit(Dialog_MotorController)
        self.textEdit_5.setObjectName(u"textEdit_5")
        self.textEdit_5.setGeometry(QRect(230, 320, 80, 30))
        self.X_POS_2 = QPlainTextEdit(Dialog_MotorController)
        self.X_POS_2.setObjectName(u"X_POS_2")
        self.X_POS_2.setGeometry(QRect(270, 480, 50, 30))
        self.X_POS_3 = QPlainTextEdit(Dialog_MotorController)
        self.X_POS_3.setObjectName(u"X_POS_3")
        self.X_POS_3.setGeometry(QRect(270, 530, 50, 30))
        self.RIGHT = QPushButton(Dialog_MotorController)
        self.RIGHT.setObjectName(u"RIGHT")
        self.RIGHT.setGeometry(QRect(120, 350, 60, 30))
        self.HOME = QPushButton(Dialog_MotorController)
        self.HOME.setObjectName(u"HOME")
        self.HOME.setGeometry(QRect(370, 350, 70, 30))
        self.X_POS_4 = QPlainTextEdit(Dialog_MotorController)
        self.X_POS_4.setObjectName(u"X_POS_4")
        self.X_POS_4.setGeometry(QRect(290, 360, 50, 30))

        self.retranslateUi(Dialog_MotorController)

        QMetaObject.connectSlotsByName(Dialog_MotorController)
    # setupUi

    def retranslateUi(self, Dialog_MotorController):
        Dialog_MotorController.setWindowTitle(QCoreApplication.translate("Dialog_MotorController", u"Dialog", None))
        self.DO_IT.setText(QCoreApplication.translate("Dialog_MotorController", u"Do it!", None))
        self.X_POS.setPlainText(QCoreApplication.translate("Dialog_MotorController", u"1 um", None))
        self.Y_POS.setPlainText(QCoreApplication.translate("Dialog_MotorController", u"1 um", None))
        self.NEW_MOTOR_POS_TEXT.setHtml(QCoreApplication.translate("Dialog_MotorController", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'.AppleSystemUIFont'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Target</p></body></html>", None))
        self.DOWN.setText(QCoreApplication.translate("Dialog_MotorController", u"DOWN", None))
        self.LEFT.setText(QCoreApplication.translate("Dialog_MotorController", u"LEFT", None))
        self.UP.setText(QCoreApplication.translate("Dialog_MotorController", u"UP", None))

        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        ___qlistwidgetitem = self.listWidget.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("Dialog_MotorController", u"1 - Line", None));
        ___qlistwidgetitem1 = self.listWidget.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("Dialog_MotorController", u"2 - Square", None));
        ___qlistwidgetitem2 = self.listWidget.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("Dialog_MotorController", u"3 - Rectangle", None));
        self.listWidget.setSortingEnabled(__sortingEnabled)

        self.LOAD_ROUTE.setText(QCoreApplication.translate("Dialog_MotorController", u"Load", None))
        self.textEdit.setHtml(QCoreApplication.translate("Dialog_MotorController", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'.AppleSystemUIFont'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Current</p></body></html>", None))
        self.textEdit_2.setHtml(QCoreApplication.translate("Dialog_MotorController", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'.AppleSystemUIFont'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Motor Pos</p></body></html>", None))
        self.textEdit_3.setHtml(QCoreApplication.translate("Dialog_MotorController", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'.AppleSystemUIFont'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">X</p></body></html>", None))
        self.textEdit_4.setHtml(QCoreApplication.translate("Dialog_MotorController", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'.AppleSystemUIFont'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Y</p></body></html>", None))
        self.textEdit_5.setHtml(QCoreApplication.translate("Dialog_MotorController", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'.AppleSystemUIFont'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Distance</p></body></html>", None))
        self.X_POS_2.setPlainText(QCoreApplication.translate("Dialog_MotorController", u"um", None))
        self.X_POS_3.setPlainText(QCoreApplication.translate("Dialog_MotorController", u"um", None))
        self.RIGHT.setText(QCoreApplication.translate("Dialog_MotorController", u"RIGHT", None))
        self.HOME.setText(QCoreApplication.translate("Dialog_MotorController", u"HOME", None))
        self.X_POS_4.setPlainText(QCoreApplication.translate("Dialog_MotorController", u"um", None))
    # retranslateUi

