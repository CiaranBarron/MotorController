# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialog_motorcontroller_3.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDialog, QFrame,
    QLabel, QPushButton, QRadioButton, QSizePolicy,
    QSpinBox, QTextEdit, QWidget)

class Ui_Dialog_MotorController(object):
    def setupUi(self, Dialog_MotorController):
        if not Dialog_MotorController.objectName():
            Dialog_MotorController.setObjectName(u"Dialog_MotorController")
        Dialog_MotorController.resize(440, 674)
        self.EXPOSE = QPushButton(Dialog_MotorController)
        self.EXPOSE.setObjectName(u"EXPOSE")
        self.EXPOSE.setGeometry(QRect(320, 310, 81, 31))
        self.MOVE_MOTORS_ARROW_SETTING = QSpinBox(Dialog_MotorController)
        self.MOVE_MOTORS_ARROW_SETTING.setObjectName(u"MOVE_MOTORS_ARROW_SETTING")
        self.MOVE_MOTORS_ARROW_SETTING.setGeometry(QRect(20, 50, 60, 30))
        self.MOVE_MOTORS_ARROW_SETTING.setMaximum(1000)
        self.MOVE_MOTORS_ARROW_SETTING.setValue(10)
        self.DOWN = QPushButton(Dialog_MotorController)
        self.DOWN.setObjectName(u"DOWN")
        self.DOWN.setGeometry(QRect(245, 100, 70, 30))
        self.LEFT = QPushButton(Dialog_MotorController)
        self.LEFT.setObjectName(u"LEFT")
        self.LEFT.setGeometry(QRect(200, 60, 60, 30))
        self.UP = QPushButton(Dialog_MotorController)
        self.UP.setObjectName(u"UP")
        self.UP.setGeometry(QRect(245, 20, 70, 30))
        self.DO_IT = QPushButton(Dialog_MotorController)
        self.DO_IT.setObjectName(u"DO_IT")
        self.DO_IT.setGeometry(QRect(320, 620, 81, 30))
        self.RIGHT = QPushButton(Dialog_MotorController)
        self.RIGHT.setObjectName(u"RIGHT")
        self.RIGHT.setGeometry(QRect(300, 60, 60, 30))
        self.HOME = QPushButton(Dialog_MotorController)
        self.HOME.setObjectName(u"HOME")
        self.HOME.setGeometry(QRect(320, 150, 81, 30))
        self.HOME_CONOR = QPushButton(Dialog_MotorController)
        self.HOME_CONOR.setObjectName(u"HOME_CONOR")
        self.HOME_CONOR.setGeometry(QRect(20, 100, 171, 32))
        self.LINE_PATTERN_CHECK = QCheckBox(Dialog_MotorController)
        self.LINE_PATTERN_CHECK.setObjectName(u"LINE_PATTERN_CHECK")
        self.LINE_PATTERN_CHECK.setGeometry(QRect(20, 370, 61, 20))
        self.SQUARE_PATTERN_CHECK = QCheckBox(Dialog_MotorController)
        self.SQUARE_PATTERN_CHECK.setObjectName(u"SQUARE_PATTERN_CHECK")
        self.SQUARE_PATTERN_CHECK.setGeometry(QRect(20, 460, 61, 20))
        self.textEdit = QTextEdit(Dialog_MotorController)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(20, 150, 201, 41))
        self.LITHO_TIMER_SECONDS = QSpinBox(Dialog_MotorController)
        self.LITHO_TIMER_SECONDS.setObjectName(u"LITHO_TIMER_SECONDS")
        self.LITHO_TIMER_SECONDS.setGeometry(QRect(180, 320, 42, 22))
        self.LITHO_TIMER_SECONDS.setMaximum(1000)
        self._LABEL_MOVE_STEPS = QLabel(Dialog_MotorController)
        self._LABEL_MOVE_STEPS.setObjectName(u"_LABEL_MOVE_STEPS")
        self._LABEL_MOVE_STEPS.setGeometry(QRect(20, 15, 121, 31))
        font = QFont()
        font.setPointSize(12)
        self._LABEL_MOVE_STEPS.setFont(font)
        self._LABEL_EXPOSURE_DOSE = QLabel(Dialog_MotorController)
        self._LABEL_EXPOSURE_DOSE.setObjectName(u"_LABEL_EXPOSURE_DOSE")
        self._LABEL_EXPOSURE_DOSE.setGeometry(QRect(20, 300, 111, 16))
        self._LABEL_DIR1_STEP_SIZE = QLabel(Dialog_MotorController)
        self._LABEL_DIR1_STEP_SIZE.setObjectName(u"_LABEL_DIR1_STEP_SIZE")
        self._LABEL_DIR1_STEP_SIZE.setGeometry(QRect(190, 390, 51, 16))
        self.DIR1_STEP_SIZE = QSpinBox(Dialog_MotorController)
        self.DIR1_STEP_SIZE.setObjectName(u"DIR1_STEP_SIZE")
        self.DIR1_STEP_SIZE.setGeometry(QRect(250, 390, 42, 22))
        self._LABEL_DIR1_NO_STEPS = QLabel(Dialog_MotorController)
        self._LABEL_DIR1_NO_STEPS.setObjectName(u"_LABEL_DIR1_NO_STEPS")
        self._LABEL_DIR1_NO_STEPS.setGeometry(QRect(190, 410, 49, 16))
        self.DIR1_NO_STEPS = QSpinBox(Dialog_MotorController)
        self.DIR1_NO_STEPS.setObjectName(u"DIR1_NO_STEPS")
        self.DIR1_NO_STEPS.setGeometry(QRect(250, 410, 42, 22))
        self._LABEL_DIR1 = QLabel(Dialog_MotorController)
        self._LABEL_DIR1.setObjectName(u"_LABEL_DIR1")
        self._LABEL_DIR1.setGeometry(QRect(100, 370, 151, 16))
        self.DIR1_LEFT = QCheckBox(Dialog_MotorController)
        self.DIR1_LEFT.setObjectName(u"DIR1_LEFT")
        self.DIR1_LEFT.setGeometry(QRect(100, 390, 31, 20))
        self.DIR1_UP = QCheckBox(Dialog_MotorController)
        self.DIR1_UP.setObjectName(u"DIR1_UP")
        self.DIR1_UP.setGeometry(QRect(140, 390, 31, 20))
        self.DIR1_RIGHT = QCheckBox(Dialog_MotorController)
        self.DIR1_RIGHT.setObjectName(u"DIR1_RIGHT")
        self.DIR1_RIGHT.setGeometry(QRect(100, 410, 31, 20))
        self.DIR1_DOWN = QCheckBox(Dialog_MotorController)
        self.DIR1_DOWN.setObjectName(u"DIR1_DOWN")
        self.DIR1_DOWN.setGeometry(QRect(140, 410, 31, 20))
        self.line = QFrame(Dialog_MotorController)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(20, 440, 271, 16))
        self.line.setFrameShadow(QFrame.Plain)
        self.line.setFrameShape(QFrame.HLine)
        self.DIR2_NO_STEPS = QSpinBox(Dialog_MotorController)
        self.DIR2_NO_STEPS.setObjectName(u"DIR2_NO_STEPS")
        self.DIR2_NO_STEPS.setGeometry(QRect(250, 500, 42, 22))
        self._LABEL_DIR2 = QLabel(Dialog_MotorController)
        self._LABEL_DIR2.setObjectName(u"_LABEL_DIR2")
        self._LABEL_DIR2.setGeometry(QRect(100, 460, 151, 16))
        self.DIR2_LEFT = QCheckBox(Dialog_MotorController)
        self.DIR2_LEFT.setObjectName(u"DIR2_LEFT")
        self.DIR2_LEFT.setGeometry(QRect(100, 480, 31, 20))
        self.DIR2_UP = QCheckBox(Dialog_MotorController)
        self.DIR2_UP.setObjectName(u"DIR2_UP")
        self.DIR2_UP.setGeometry(QRect(140, 480, 31, 20))
        self.DIR2_DOWN = QCheckBox(Dialog_MotorController)
        self.DIR2_DOWN.setObjectName(u"DIR2_DOWN")
        self.DIR2_DOWN.setGeometry(QRect(140, 500, 31, 20))
        self.DIR2_RIGHT = QCheckBox(Dialog_MotorController)
        self.DIR2_RIGHT.setObjectName(u"DIR2_RIGHT")
        self.DIR2_RIGHT.setGeometry(QRect(100, 500, 31, 20))
        self.DIR2_STEP_SIZE = QSpinBox(Dialog_MotorController)
        self.DIR2_STEP_SIZE.setObjectName(u"DIR2_STEP_SIZE")
        self.DIR2_STEP_SIZE.setGeometry(QRect(250, 480, 42, 22))
        self._LABEL_DIR2_STEP_SIZE = QLabel(Dialog_MotorController)
        self._LABEL_DIR2_STEP_SIZE.setObjectName(u"_LABEL_DIR2_STEP_SIZE")
        self._LABEL_DIR2_STEP_SIZE.setGeometry(QRect(190, 480, 51, 16))
        self._LABEL_DIR2_NO_STEPS = QLabel(Dialog_MotorController)
        self._LABEL_DIR2_NO_STEPS.setObjectName(u"_LABEL_DIR2_NO_STEPS")
        self._LABEL_DIR2_NO_STEPS.setGeometry(QRect(190, 500, 49, 16))
        self.line_2 = QFrame(Dialog_MotorController)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(20, 530, 271, 16))
        self.line_2.setFrameShadow(QFrame.Plain)
        self.line_2.setFrameShape(QFrame.HLine)
        self.TRIANGLE_PATTERN_CHECK = QCheckBox(Dialog_MotorController)
        self.TRIANGLE_PATTERN_CHECK.setObjectName(u"TRIANGLE_PATTERN_CHECK")
        self.TRIANGLE_PATTERN_CHECK.setGeometry(QRect(20, 550, 76, 20))
        self.TRIANGLE_START_SIZE = QSpinBox(Dialog_MotorController)
        self.TRIANGLE_START_SIZE.setObjectName(u"TRIANGLE_START_SIZE")
        self.TRIANGLE_START_SIZE.setGeometry(QRect(250, 570, 42, 22))
        self.TRIANGLE_START_SIZE.setMaximum(50)
        self.label = QLabel(Dialog_MotorController)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(190, 570, 49, 16))
        self.label_2 = QLabel(Dialog_MotorController)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(190, 590, 41, 16))
        self.TRIANGLE_ROWS = QSpinBox(Dialog_MotorController)
        self.TRIANGLE_ROWS.setObjectName(u"TRIANGLE_ROWS")
        self.TRIANGLE_ROWS.setGeometry(QRect(250, 590, 42, 22))
        self.TRIANGLE_ROWS.setMaximum(50)
        self.label_3 = QLabel(Dialog_MotorController)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(100, 550, 71, 16))
        self.TRIANGLE_UP = QCheckBox(Dialog_MotorController)
        self.TRIANGLE_UP.setObjectName(u"TRIANGLE_UP")
        self.TRIANGLE_UP.setGeometry(QRect(100, 570, 61, 20))
        self.TRIANGLE_DOWN = QCheckBox(Dialog_MotorController)
        self.TRIANGLE_DOWN.setObjectName(u"TRIANGLE_DOWN")
        self.TRIANGLE_DOWN.setGeometry(QRect(100, 590, 61, 20))
        self.label_4 = QLabel(Dialog_MotorController)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(190, 610, 61, 16))
        self.label_5 = QLabel(Dialog_MotorController)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(190, 630, 61, 16))
        self.TRIANGLE_Y_STEPS = QSpinBox(Dialog_MotorController)
        self.TRIANGLE_Y_STEPS.setObjectName(u"TRIANGLE_Y_STEPS")
        self.TRIANGLE_Y_STEPS.setGeometry(QRect(250, 610, 42, 22))
        self.TRIANGLE_Y_STEPS.setMaximum(200)
        self.TRIANGLE_X_STEPS = QSpinBox(Dialog_MotorController)
        self.TRIANGLE_X_STEPS.setObjectName(u"TRIANGLE_X_STEPS")
        self.TRIANGLE_X_STEPS.setGeometry(QRect(250, 630, 42, 22))
        self.TRIANGLE_X_STEPS.setMaximum(200)
        self.RADIO_3120 = QRadioButton(Dialog_MotorController)
        self.RADIO_3120.setObjectName(u"RADIO_3120")
        self.RADIO_3120.setGeometry(QRect(20, 220, 89, 20))
        self.RADIO_4340 = QRadioButton(Dialog_MotorController)
        self.RADIO_4340.setObjectName(u"RADIO_4340")
        self.RADIO_4340.setGeometry(QRect(110, 220, 89, 20))
        self.label_6 = QLabel(Dialog_MotorController)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(20, 200, 261, 16))
        self._LABEL_EXPOSE_SEC = QLabel(Dialog_MotorController)
        self._LABEL_EXPOSE_SEC.setObjectName(u"_LABEL_EXPOSE_SEC")
        self._LABEL_EXPOSE_SEC.setGeometry(QRect(20, 320, 81, 16))
        self.LITHO_DOSE = QSpinBox(Dialog_MotorController)
        self.LITHO_DOSE.setObjectName(u"LITHO_DOSE")
        self.LITHO_DOSE.setGeometry(QRect(180, 300, 42, 22))
        self._LABEL_UV_POWER = QLabel(Dialog_MotorController)
        self._LABEL_UV_POWER.setObjectName(u"_LABEL_UV_POWER")
        self._LABEL_UV_POWER.setGeometry(QRect(20, 280, 161, 16))
        self.LITHO_UV_POWER = QSpinBox(Dialog_MotorController)
        self.LITHO_UV_POWER.setObjectName(u"LITHO_UV_POWER")
        self.LITHO_UV_POWER.setGeometry(QRect(180, 280, 42, 22))
        self.LITHO_POWER_CHANGE_CHECKBOX = QCheckBox(Dialog_MotorController)
        self.LITHO_POWER_CHANGE_CHECKBOX.setObjectName(u"LITHO_POWER_CHANGE_CHECKBOX")
        self.LITHO_POWER_CHANGE_CHECKBOX.setGeometry(QRect(20, 250, 271, 20))

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
        self.DO_IT.setText(QCoreApplication.translate("Dialog_MotorController", u"Do it!", None))
        self.RIGHT.setText(QCoreApplication.translate("Dialog_MotorController", u"RIGHT", None))
#if QT_CONFIG(shortcut)
        self.RIGHT.setShortcut(QCoreApplication.translate("Dialog_MotorController", u"Right", None))
#endif // QT_CONFIG(shortcut)
        self.HOME.setText(QCoreApplication.translate("Dialog_MotorController", u"HOME", None))
        self.HOME_CONOR.setText(QCoreApplication.translate("Dialog_MotorController", u"Home? only Conor can know", None))
        self.LINE_PATTERN_CHECK.setText(QCoreApplication.translate("Dialog_MotorController", u"Line", None))
        self.SQUARE_PATTERN_CHECK.setText(QCoreApplication.translate("Dialog_MotorController", u"Square", None))
        self.textEdit.setHtml(QCoreApplication.translate("Dialog_MotorController", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Pattern Litho</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">motor controlled so use at own peril.</span></p></body></html>", None))
        self._LABEL_MOVE_STEPS.setText(QCoreApplication.translate("Dialog_MotorController", u"Move (steps)", None))
        self._LABEL_EXPOSURE_DOSE.setText(QCoreApplication.translate("Dialog_MotorController", u"Expsoure (mW/cm2)", None))
        self._LABEL_DIR1_STEP_SIZE.setText(QCoreApplication.translate("Dialog_MotorController", u"Step Size:", None))
        self._LABEL_DIR1_NO_STEPS.setText(QCoreApplication.translate("Dialog_MotorController", u"No. Steps:", None))
        self._LABEL_DIR1.setText(QCoreApplication.translate("Dialog_MotorController", u"Direction 1", None))
        self.DIR1_LEFT.setText(QCoreApplication.translate("Dialog_MotorController", u"L", None))
        self.DIR1_UP.setText(QCoreApplication.translate("Dialog_MotorController", u"U", None))
        self.DIR1_RIGHT.setText(QCoreApplication.translate("Dialog_MotorController", u"R", None))
        self.DIR1_DOWN.setText(QCoreApplication.translate("Dialog_MotorController", u"D", None))
        self._LABEL_DIR2.setText(QCoreApplication.translate("Dialog_MotorController", u"Direction 2", None))
        self.DIR2_LEFT.setText(QCoreApplication.translate("Dialog_MotorController", u"L", None))
        self.DIR2_UP.setText(QCoreApplication.translate("Dialog_MotorController", u"U", None))
        self.DIR2_DOWN.setText(QCoreApplication.translate("Dialog_MotorController", u"D", None))
        self.DIR2_RIGHT.setText(QCoreApplication.translate("Dialog_MotorController", u"R", None))
        self._LABEL_DIR2_STEP_SIZE.setText(QCoreApplication.translate("Dialog_MotorController", u"Step Size:", None))
        self._LABEL_DIR2_NO_STEPS.setText(QCoreApplication.translate("Dialog_MotorController", u"No. Steps:", None))
        self.TRIANGLE_PATTERN_CHECK.setText(QCoreApplication.translate("Dialog_MotorController", u"Triangle", None))
        self.label.setText(QCoreApplication.translate("Dialog_MotorController", u"Start size", None))
        self.label_2.setText(QCoreApplication.translate("Dialog_MotorController", u"Rows", None))
        self.label_3.setText(QCoreApplication.translate("Dialog_MotorController", u"Direction", None))
        self.TRIANGLE_UP.setText(QCoreApplication.translate("Dialog_MotorController", u"Up ", None))
        self.TRIANGLE_DOWN.setText(QCoreApplication.translate("Dialog_MotorController", u"Down", None))
        self.label_4.setText(QCoreApplication.translate("Dialog_MotorController", u"Y Step size", None))
        self.label_5.setText(QCoreApplication.translate("Dialog_MotorController", u"X Step size", None))
        self.RADIO_3120.setText(QCoreApplication.translate("Dialog_MotorController", u"3120 (rec)", None))
        self.RADIO_4340.setText(QCoreApplication.translate("Dialog_MotorController", u"4340 (rec)", None))
        self.label_6.setText(QCoreApplication.translate("Dialog_MotorController", u"Resist (default exposure times for given power)", None))
        self._LABEL_EXPOSE_SEC.setText(QCoreApplication.translate("Dialog_MotorController", u"Exposure (s)", None))
        self._LABEL_UV_POWER.setText(QCoreApplication.translate("Dialog_MotorController", u"UV Power (uW) / 90um sq", None))
        self.LITHO_POWER_CHANGE_CHECKBOX.setText(QCoreApplication.translate("Dialog_MotorController", u"Change UV Power (requires attiny re-program)", None))
    # retranslateUi

