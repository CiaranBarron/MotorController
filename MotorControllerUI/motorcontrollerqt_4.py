# This Python file uses the following encoding: utf-8
# Ciaran Barron 07.11.24

import os
import sys
import time

from serial import Serial

from PySide6.QtWidgets import QApplication, QWidget, QGraphicsScene, QGraphicsEllipseItem
from PySide6.QtGui import QBrush, QColor, QPen, QPainter, QPixmap
from PySide6.QtCore import Qt

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form_4 import Ui_Dialog_MotorController

# This line allows the file to see back up one directory because
# I have the motor control script in a different folder.
# Not sure if it's legal but it works.
sys.path.insert(1, '../Backend')

# ignore this error. The path insert solves it.
from Electronic_Modules.Koco_Linear_Actuator.linearmotor_comms import LinearMotor

# x_id = 842400280  # Motor id for x
# y_id = 842400780  # Motor id for y
# s_id = "FT7AX5XQ" # Serial number for motor controller board.


class MotorControllerQt(QWidget):
    """Class for connecting the motors to the UI"""
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog_MotorController()
        self.ui.setupUi(self)

        # set values of spin boxes.
        self._move_strength = 0 # number of steps no distances.  I named it badly, but blame the oxford instruments.
        self._exposure_time = 90
        self._exposure_dose = 0
        self._litho_uv_power = 0.36  # mJ/cm2
        self._dose_per_second = 4.44

        #values in mJ/cm2
        self._3120_complete_dose = 65 * 2 # double the sheet value. mJ/cm2
        self._4340_complete_dose = 140 * 3 #triple the recommended dose on the sheet. For some reason it works well though.
        self._pattern = False

        # Bitmap exposure options
        self._bitmap_color_choice = 'Black'
        self._bitmap_square_size = 90 # um

        # Options for line and square patterns
        self._DIR1 = False
        self._DIR2 = False
        self._TRIANGLE_DIR = False
        self._DIR1_step_size = 24
        self._DIR1_no_steps = 0
        self._DIR2_step_size = 6
        self._DIR2_no_steps = 0
        self._pattern_square_size = 90 # um

        # options for triangle pattern
        self._triangle_rows = 0
        self._triangle_start_size = 0
        self._triangle_y_step_size = 0
        self._triangle_x_step_size = 0

        # for slide selection
        self._slide_choice = False

        # for bitmaps
        self._bitmap_choice = False

        # no idea what this is even for tbh. leaving it here in case it breaks something.
        self._t = 0

        # Click actions linked to functions.
        self.ui.DO_IT.clicked.connect(self.doit_method)
        self.ui.HOME.clicked.connect(self.home)
        self.ui.ABS_MOVE.clicked.connect(self._move)
        self.ui.EXPOSE.clicked.connect(self.expose)
        self.ui.UP.clicked.connect(lambda: self._move_rel_dir('up'))
        self.ui.DOWN.clicked.connect(lambda: self._move_rel_dir('down'))
        self.ui.LEFT.clicked.connect(lambda: self._move_rel_dir('left'))
        self.ui.RIGHT.clicked.connect(lambda: self._move_rel_dir('right'))

        # BITMAP FUNCTION BUTTONS
        self.ui.LOAD_BITMAP.clicked.connect(self.load_bitmap)
        self.ui.RUN_BITMAP.clicked.connect(self.run_bitmap)
        self.ui.BITMAP_SQUARE_SIZE

        # values of spin boxes & updates.
        self.ui.MOVE_MOTORS_ARROW_SETTING.setValue(self._move_strength)  # set default value in spin box.
        self.ui.MOVE_MOTORS_ARROW_SETTING.valueChanged.connect(self.update_move_strength)  # does this change it?

        self.ui.LITHO_TIMER_SECONDS.setValue(90)
        self.ui.LITHO_TIMER_SECONDS.valueChanged.connect(self.update_exposure_time)

        self.ui.LINE_PATTERN_CHECK.stateChanged.connect(self.update_line_checkboxes)
        self.ui.SQUARE_PATTERN_CHECK.stateChanged.connect(self.update_square_checkboxes)
        self.ui.TRIANGLE_PATTERN_CHECK.stateChanged.connect(self.update_triangle_checkboxes)

        self.ui.PATTERN_SQUARE_SIZE.valueChanged.connect(self.update_pattern_square_size)
        self.ui.DIR1_NO_STEPS.valueChanged.connect(self.update_DIR1_no_steps)
        self.ui.DIR2_NO_STEPS.valueChanged.connect(self.update_DIR2_no_steps)
        self.ui.TRIANGLE_ROWS.valueChanged.connect(self.update_triangle_rows)
        self.ui.TRIANGLE_START_SIZE.valueChanged.connect(self.update_triangle_start_size)

        # set up checkboxes at the start.
        self.ui.LINE_PATTERN_CHECK.setChecked(1)
        self.ui.DIR2_UP.setDisabled(True)
        self.ui.DIR2_DOWN.setDisabled(True)
        self.ui.DIR2_LEFT.setDisabled(True)
        self.ui.DIR2_RIGHT.setDisabled(True)
        self.ui.TRIANGLE_UP.setDisabled(True)
        self.ui.TRIANGLE_DOWN.setDisabled(True)

        self.ui.DIR1_UP.stateChanged.connect(self.update_DIR1_up_setting)
        self.ui.DIR1_DOWN.stateChanged.connect(self.update_DIR1_down_setting)
        self.ui.DIR1_LEFT.stateChanged.connect(self.update_DIR1_left_setting)
        self.ui.DIR1_RIGHT.stateChanged.connect(self.update_DIR1_right_setting)

        self.ui.DIR2_UP.stateChanged.connect(self.update_DIR2_up_setting)
        self.ui.DIR2_DOWN.stateChanged.connect(self.update_DIR2_down_setting)
        self.ui.DIR2_LEFT.stateChanged.connect(self.update_DIR2_left_setting)
        self.ui.DIR2_RIGHT.stateChanged.connect(self.update_DIR2_right_setting)

        self.ui.TRIANGLE_UP.stateChanged.connect(self.update_triangle_up_direction)
        self.ui.TRIANGLE_DOWN.stateChanged.connect(self.update_triangle_down_direction)

        self.ui.LITHO_POWER_CHANGE_CHECKBOX.stateChanged.connect(self.update_litho_power_checkbox)
        self.ui.LITHO_UV_POWER.valueChanged.connect(self.update_uv_power)

        self.ui.LITHO_DOSE.valueChanged.connect(self.update_exposure_dose)

        self.ui.RADIO_3120.clicked.connect(self.update_exposure_3120)
        self.ui.RADIO_4340.clicked.connect(self.update_exposure_4340)

        self.ui.LITHO_UV_POWER.setValue(self._litho_uv_power)
        self.ui.LITHO_UV_POWER.setDisabled(True)

        # temporary:
        self.ui.RADIO_4340.setDisabled(True)
        self.ui.RADIO_3120.setDisabled(True)
        self.ui.LITHO_DOSE.setDisabled(True)

        # Adding list of slides to pull from. (graphically)
        self.ui._SLIDE_LIST.itemClicked.connect(self.update_slide_choice)
        self.ui.BITMAP_LIST.itemClicked.connect(self.update_bitmap_choice)

        self.populate_bitmap_list()
        self.add_stage_slide_display()
        # self.add_laser_slide_display()

    def populate_bitmap_list(self):
        """
        List all the files in the bitmap folder as options in the list.
        """
        bitmap_list = os.listdir("../Backend/Bitmaps")
        for bitmap in bitmap_list:
            self.ui.BITMAP_LIST.addItem(bitmap)
        return None

    def update_bitmap_choice(self, item):
        """
        On selection just change the stored value of which file
        """
        self._bitmap_choice = item.text()
        print(self._bitmap_choice)
        return None

    def add_stage_slide_display(self):
        """Populate the SLIDE_DISPLAY with a QGraphicsScene."""
        # Create a QGraphicsScene
        scene = QGraphicsScene()

        pen = QPen(QColor("red"))
        pen.setWidth(2)
        pen.setStyle(Qt.SolidLine)
        # Add a rectangle to represent the slide
        slide_width, slide_height = 112, 112
        rect_ = scene.addRect(0, 0, slide_width, slide_height)
        rect_.setPen(pen)
        rect_.setBrush(QBrush(Qt.white))

        # Add a red circle to represent the laser spot
        laser_spot = QGraphicsEllipseItem(0, 0, 5, 5)
        laser_spot.setBrush(QBrush(QColor("blue")))
        laser_spot.setPos(slide_width // 2, slide_height // 2)  # Center position
        scene.addItem(laser_spot)

        # Set the scene to SLIDE_DISPLAY
        self.ui.SLIDE_DISPLAY.setScene(scene)
        self.ui.SLIDE_DISPLAY.setSceneRect(0, 0, slide_width, slide_height)
        return None

    def update_slide_choice(self, item):
        """
        change the graphic shown in the SLIDE_DISPLAY graphic.
        The graphic will always have a red rectangle the side of the stage area. And a dor for current motor position.
        This will overlay / change the slide around it.
        """
        self._slide_choice = item.text()
        print(self._slide_choice)
        return None


    def update_exposure_3120(self):
        if self.ui.RADIO_3120.isChecked():
            self._exposure_dose = self._3120_complete_dose
            self.ui.LITHO_DOSE.setValue(self._exposure_dose)
            self.update_exposure_time()
            self.ui.RADIO_4340.setChecked(False)
        return None

    def update_exposure_4340(self):
        if self.ui.RADIO_4340.isChecked():
            self._exposure_dose = self._4340_complete_dose
            self.ui.LITHO_DOSE.setValue(self._exposure_dose)
            self.update_exposure_time()
            self.ui.RADIO_3120.setChecked(False)
        return None

    def update_exposure_dose(self):
        self._exposure_dose = self.ui.LITHO_DOSE.value()
        self.ui.LITHO_TIMER_SECONDS.setValue(self._exposure_dose / self._litho_uv_power)

    def update_exposure_time(self):
        '''TODO: add the calculation of the total dose here.'''
        # update the exposure time stored in the object.
        exposure_time = self.ui.LITHO_TIMER_SECONDS.value()
        self._exposure_time = exposure_time
        self.ui.LITHO_TIMER_SECONDS.setValue(self._exposure_time)
        return None

    def update_uv_power(self):
        '''TODO: revisit the function calls at the end of this sto see if they need to be implemented here.'''
        if self.ui.LITHO_POWER_CHANGE_CHECKBOX.isChecked():
            uv_power = self.ui.LITHO_UV_POWER.value()

            self._litho_uv_power = uv_power
            self.update_exposure_time()
            self.update_exposure_dose()


    def update_litho_power_checkbox(self):
        if self.ui.LITHO_POWER_CHANGE_CHECKBOX.isChecked():
            self.ui.LITHO_UV_POWER.setEnabled(True)
        else:
            self.ui.LITHO_UV_POWER.setDisabled(True)


    def update_pattern_square_size(self):
        """
        update the local copy of the pattern square size. this is currently redundant as the function calls it directly.
        Use this to verify the changes.
        """
        self._pattern_square_size = self.ui.PATTERN_SQUARE_SIZE.value()
        return None

    def update_triangle_up_direction(self):
        if self.ui.TRIANGLE_UP.isChecked():
            self._TRIANGLE_DIR = "up"
            self.ui.TRIANGLE_DOWN.setChecked(False)
        return None


    def update_triangle_down_direction(self):
        if self.ui.TRIANGLE_DOWN.isChecked():
            self._TRIANGLE_DIR = "down"
            self.ui.TRIANGLE_UP.setChecked(False)
        return None

    def update_DIR2_up_setting(self):
        if self.ui.DIR2_UP.isChecked():
            self._DIR2 = "UP"
            self.ui._LABEL_DIR2.setText("Direction 2:   Up")
            self.ui.DIR2_DOWN.setChecked(False)
            self.ui.DIR2_LEFT.setChecked(False)
            self.ui.DIR2_RIGHT.setChecked(False)

        return None

    def update_DIR2_down_setting(self):
        if self.ui.DIR2_DOWN.isChecked():
            self._DIR2 = "DOWN"
            self.ui._LABEL_DIR2.setText("Direction 2:   Down")
            self.ui.DIR2_UP.setChecked(False)
            self.ui.DIR2_LEFT.setChecked(False)
            self.ui.DIR2_RIGHT.setChecked(False)

        return None

    def update_DIR2_left_setting(self):
        if self.ui.DIR2_LEFT.isChecked():
            self._DIR2 = "LEFT"
            self.ui._LABEL_DIR2.setText("Direction 2:   Left")
            self.ui.DIR2_DOWN.setChecked(False)
            self.ui.DIR2_UP.setChecked(False)
            self.ui.DIR2_RIGHT.setChecked(False)

        return None

    def update_DIR2_right_setting(self):
        if self.ui.DIR2_RIGHT.isChecked():
            self._DIR2 = "RIGHT"
            self.ui._LABEL_DIR2.setText("Direction 2:   Right")
            self.ui.DIR2_DOWN.setChecked(False)
            self.ui.DIR2_LEFT.setChecked(False)
            self.ui.DIR2_UP.setChecked(False)

        return None

    def update_DIR1_up_setting(self):
        if self.ui.DIR1_UP.isChecked():
            self._DIR1 = "UP"
            self.ui._LABEL_DIR1.setText("Direction 1:   Up")
            self.ui.DIR1_DOWN.setChecked(False)
            self.ui.DIR1_LEFT.setChecked(False)
            self.ui.DIR1_RIGHT.setChecked(False)

            if self.ui.SQUARE_PATTERN_CHECK.isChecked():
                if self.ui.DIR2_DOWN.isChecked():
                    self.ui.DIR2_DOWN.setChecked(False)
                if self.ui.DIR2_UP.isChecked():
                    self.ui.DIR2_UP.setChecked(False)
                self.ui.DIR2_UP.setDisabled(True)
                self.ui.DIR2_DOWN.setDisabled(True)
                self.ui.DIR2_LEFT.setEnabled(True)
                self.ui.DIR2_RIGHT.setEnabled(True)
        else:
            if self.ui.SQUARE_PATTERN_CHECK.isChecked():
                self.ui.DIR2_UP.setEnabled(True)
                self.ui.DIR2_DOWN.setEnabled(True)
                self.ui.DIR2_LEFT.setEnabled(True)
                self.ui.DIR2_RIGHT.setEnabled(True)

        return None

    def update_DIR1_down_setting(self):
        if self.ui.DIR1_DOWN.isChecked():
            self._DIR1 = "DOWN"
            self.ui._LABEL_DIR1.setText("Direction 1:   Down")
            self.ui.DIR1_UP.setChecked(False)
            self.ui.DIR1_LEFT.setChecked(False)
            self.ui.DIR1_RIGHT.setChecked(False)

            if self.ui.SQUARE_PATTERN_CHECK.isChecked():
                if self.ui.DIR2_DOWN.isChecked():
                    self.ui.DIR2_DOWN.setChecked(False)
                if self.ui.DIR2_UP.isChecked():
                    self.ui.DIR2_UP.setChecked(False)
                self.ui.DIR2_UP.setDisabled(True)
                self.ui.DIR2_DOWN.setDisabled(True)
                self.ui.DIR2_LEFT.setEnabled(True)
                self.ui.DIR2_RIGHT.setEnabled(True)
        else:
            if self.ui.SQUARE_PATTERN_CHECK.isChecked():
                self.ui.DIR2_UP.setEnabled(True)
                self.ui.DIR2_DOWN.setEnabled(True)
                self.ui.DIR2_LEFT.setEnabled(True)
                self.ui.DIR2_RIGHT.setEnabled(True)

        return None

    def update_DIR1_left_setting(self):

        if self.ui.DIR1_LEFT.isChecked():
            self._DIR1 = "LEFT"
            self.ui._LABEL_DIR1.setText("Direction 1:   Left")
            self.ui.DIR1_DOWN.setChecked(False)
            self.ui.DIR1_UP.setChecked(False)
            self.ui.DIR1_RIGHT.setChecked(False)

            if self.ui.SQUARE_PATTERN_CHECK.isChecked():
                if self.ui.DIR2_LEFT.isChecked():
                    self.ui.DIR2_LEFT.setChecked(False)
                if self.ui.DIR2_RIGHT.isChecked():
                    self.ui.DIR2_RIGHT.setChecked(False)
                self.ui.DIR2_UP.setEnabled(True)
                self.ui.DIR2_DOWN.setEnabled(True)
                self.ui.DIR2_LEFT.setDisabled(True)
                self.ui.DIR2_RIGHT.setDisabled(True)
        else:
            if self.ui.SQUARE_PATTERN_CHECK.isChecked():
                self.ui.DIR2_UP.setEnabled(True)
                self.ui.DIR2_DOWN.setEnabled(True)
                self.ui.DIR2_LEFT.setEnabled(True)
                self.ui.DIR2_RIGHT.setEnabled(True)

        return None

    def update_DIR1_right_setting(self):

        if self.ui.DIR1_RIGHT.isChecked():
            self._DIR1 = "RIGHT"
            self.ui._LABEL_DIR1.setText("Direction 1:   Right")
            self.ui.DIR1_DOWN.setChecked(False)
            self.ui.DIR1_LEFT.setChecked(False)
            self.ui.DIR1_UP.setChecked(False)

            if self.ui.SQUARE_PATTERN_CHECK.isChecked():
                if self.ui.DIR2_LEFT.isChecked():
                    self.ui.DIR2_LEFT.setChecked(False)
                if self.ui.DIR2_RIGHT.isChecked():
                    self.ui.DIR2_RIGHT.setChecked(False)
                self.ui.DIR2_UP.setEnabled(True)
                self.ui.DIR2_DOWN.setEnabled(True)
                self.ui.DIR2_LEFT.setDisabled(True)
                self.ui.DIR2_RIGHT.setDisabled(True)
        else:
            if self.ui.SQUARE_PATTERN_CHECK.isChecked():
                self.ui.DIR2_UP.setEnabled(True)
                self.ui.DIR2_DOWN.setEnabled(True)
                self.ui.DIR2_LEFT.setEnabled(True)
                self.ui.DIR2_RIGHT.setEnabled(True)

        return None

    def update_move_strength(self):
        # address this function on the arduino side. Move all checks on position there. NONE IN UI.
        ms = self.ui.MOVE_MOTORS_ARROW_SETTING.value()

        if ms > 1000:
            ms = 1000
        if ms < 0:
            ms = 0
        print(f"Motor move strength: steps - {ms}")
        self._move_strength = ms
        self.ui.MOVE_MOTORS_ARROW_SETTING.setValue(self._move_strength)

        return None


    def update_line_checkboxes(self):
        # enable the checkboxes.
        if self.ui.LINE_PATTERN_CHECK.isChecked():

            self.ui.SQUARE_PATTERN_CHECK.setChecked(False)
            self.ui.TRIANGLE_PATTERN_CHECK.setChecked(False)

            self.ui.DIR1_UP.setEnabled(True)
            self.ui.DIR1_RIGHT.setEnabled(True)
            self.ui.DIR1_LEFT.setEnabled(True)
            self.ui.DIR1_DOWN.setEnabled(True)

            self.ui.DIR2_UP.setDisabled(True)
            self.ui.DIR2_DOWN.setDisabled(True)
            self.ui.DIR2_LEFT.setDisabled(True)
            self.ui.DIR2_RIGHT.setDisabled(True)

            self.ui.TRIANGLE_DOWN.setDisabled(True)
            self.ui.TRIANGLE_UP.setDisabled(True)

            self._pattern = "line"

        return None

    def update_square_checkboxes(self):

        if self.ui.SQUARE_PATTERN_CHECK.isChecked():

            self.ui.LINE_PATTERN_CHECK.setChecked(False)
            self.ui.TRIANGLE_PATTERN_CHECK.setChecked(False)

            self.ui.DIR1_UP.setEnabled(True)
            self.ui.DIR1_RIGHT.setEnabled(True)
            self.ui.DIR1_LEFT.setEnabled(True)
            self.ui.DIR1_DOWN.setEnabled(True)

            self.ui.DIR2_UP.setEnabled(True)
            self.ui.DIR2_DOWN.setEnabled(True)
            self.ui.DIR2_LEFT.setEnabled(True)
            self.ui.DIR2_RIGHT.setEnabled(True)

            self.ui.TRIANGLE_DOWN.setDisabled(True)
            self.ui.TRIANGLE_UP.setDisabled(True)

            self._pattern = "square"

        return None

    def update_triangle_checkboxes(self):

        if self.ui.TRIANGLE_PATTERN_CHECK.isChecked():

            self.ui.LINE_PATTERN_CHECK.setChecked(False)
            self.ui.SQUARE_PATTERN_CHECK.setChecked(False)

            self.ui.DIR1_UP.setDisabled(True)
            self.ui.DIR1_RIGHT.setDisabled(True)
            self.ui.DIR1_LEFT.setDisabled(True)
            self.ui.DIR1_DOWN.setDisabled(True)

            self.ui.DIR2_UP.setDisabled(True)
            self.ui.DIR2_DOWN.setDisabled(True)
            self.ui.DIR2_LEFT.setDisabled(True)
            self.ui.DIR2_RIGHT.setDisabled(True)

            self.ui.TRIANGLE_DOWN.setEnabled(True)
            self.ui.TRIANGLE_UP.setEnabled(True)

            self._pattern = "triangle"

        return None

    def update_DIR1_step_size(self):
        step_size = self.ui.DIR1_STEP_SIZE.value()
        if step_size < 0:
            step_size = 0
        self._DIR1_step_size = step_size
        return None

    def update_DIR1_no_steps(self):
        step_size = self.ui.DIR1_NO_STEPS.value()
        if step_size < 0:
            step_size = 0
        self._DIR1_no_steps = step_size
        return None

    def update_DIR2_step_size(self):
        step_size = self.ui.DIR2_STEP_SIZE.value()
        if step_size < 0:
            step_size = 0
        self._DIR2_step_size = step_size
        return None

    def update_DIR2_no_steps(self):
        step_size = self.ui.DIR2_NO_STEPS.value()
        if step_size < 0:
            step_size = 0
        self._DIR2_no_steps = step_size
        return None

    def update_triangle_x_steps(self):
        x_steps = self.ui.TRIANGLE_X_STEPS.value()
        self._triangle_x_step_size = x_steps
        return None

    def update_triangle_y_steps(self):
        y_steps = self.ui.TRIANGLE_Y_STEPS.value()
        self._triangle_y_step_size = y_steps
        return None

    def update_triangle_rows(self):
        self._triangle_rows = self.ui.TRIANGLE_ROWS.value()
        return None

    def update_triangle_start_size(self):
        self._triangle_start_size = self.ui.TRIANGLE_START_SIZE.value()
        return None

    def expose(self):
        # add any checks here before sending message to litho arduino.
        self.litho(expose_time_seconds=self._exposure_time)
    def doit_method(self):
        """
        DO IT
        """
        # remember to add a verification this number.
        step_size = self.ui.PATTERN_SQUARE_SIZE.value()

        if self.ui.TRIANGLE_PATTERN_CHECK.isChecked():
            '''run triangle pattern - if start size > 1 go right to left. 
                  .
                 ...
                .....
            TODO: Test patterning multiple shapes and directions. 
            '''
            start_size = self._triangle_start_size
            if start_size < 1:
                step_size = 1

            rows = self._triangle_rows
            if rows < 1:
                rows = 1

            dir_modifier = 1

            if self._TRIANGLE_DIR == 'up':
                y_dir_modifier = 1
            else:
                y_dir_modifier = -1

            for i in range(rows):
                # 0 -> rows
                for j in range(start_size + 2 * i):
                    # 0 -> start_size + 2 * rows[i] => grow per row by 2.
                    row_dir = 'right'

                    self.litho(self._exposure_time)
                    time.sleep(self._exposure_time)

                    # move to the right.
                    if i % 2 == 0:
                        dir_modifier = 1
                    else:
                        dir_modifier = -1

                    with LinearMotor(serial_number=s_id) as lm:
                        lm.move_relative(x_id, dir_modifier * step_size)

                # move an extra step in the same direction and then move down one step.
                with LinearMotor(serial_number=s_id) as lm:
                    lm.move_relative(x_id, dir_modifier * step_size)

                # move up/down one step size. (row)
                with LinearMotor(serial_number=s_id) as lm:
                    lm.move_relative(y_id, y_dir_modifier * step_size)

            return None

        elif self.ui.SQUARE_PATTERN_CHECK.isChecked():
            '''TODO: test this on litho runs. Perhaps exclude certain direction combinations.'''

            rows = self._DIR1_no_steps
            cols = self._DIR2_no_steps

            row_id = x_id
            col_id = y_id

            # Handling which direction to send the motors for row and cols.
            match self._DIR1:
                case 'left':
                    row_id = x_id
                    col_id = y_id
                case 'right':
                    row_id = x_id
                    col_id = y_id
                case 'up':
                    row_id = y_id
                    col_id = x_id
                case 'down':
                    row_id = y_id
                    col_id = x_id

            if self._DIR2 == 'up' or self._DIR2 == 'down':
                if self._DIR1 == 'left':
                    row_dir_modifier = -1
                else:
                    row_dir_modifier = 1
            else:
                if self._DIR1 == 'up':
                    row_dir_modifier = 1
                else:
                    row_dir_modifier = -1


            for i in range(rows):

                for j in range(cols):

                    self.litho(self._exposure_time)
                    time.sleep(self._exposure_time)

                    # move to the right.
                    if i % 2 == 0:
                        col_dir_modifier = 1
                    else:
                        col_dir_modifier = -1

                    with LinearMotor(serial_number=s_id) as lm:
                        lm.move_relative(row_id, col_dir_modifier * step_size)

                with LinearMotor(serial_number=s_id) as lm:
                    lm.move_relative(col_id, row_dir_modifier * step_size)

            return None # leave here is important.

        elif self.ui.LINE_PATTERN_CHECK.isChecked():
            '''run line pattern'''
            m_id = x_id
            dir_modifier = 1

            match self._DIR1:
                case 'left':
                    m_id = x_id
                    dir_modifier = -1
                case 'right':
                    m_id = x_id
                    dir_modifier = 1
                case 'up':
                    m_id = y_id
                    dir_modifier = 1
                case 'down':
                    m_id = y_id
                    dir_modifier = -1

            steps = self._DIR1_no_steps

            for _ in range(steps):

                self.litho(self._exposure_time)
                time.sleep(self._exposure_time)

                with LinearMotor(serial_number=s_id) as lm:
                    lm.move_relative(m_id, dir_modifier * step_size)

            return None

        else:
            print("Error: No Pattern selected.")
        return

    def home(self):
        """
        Home the Motors. Builtin LinearMotor func
        """
        with LinearMotor(serial_number = s_id) as lm:
            lm.home_motor(x_id)
            lm.home_motor(y_id)

    def verify_positions(x, y):
        # some assertions here about the coordinates that you would be moving too. Might be redundant, check motor code.
        return None

    def _move(self):
        """
        Move the motors to a specific x,y position
        """
        # need to add some verification of the coords x and y before continuing.
        x = self.ui.MOVE_MOTORS_ABS_SETTING_X.value()
        y = self.ui.MOVE_MOTORS_ABS_SETTING_Y.value()

        with LinearMotor(serial_number=s_id) as lm:

            lm.move_absolute(x_id, x)
            lm.move_absolute(y_id, y)

            delta_pos = 74E-3 # define acceptable difference of 10 motor steps (73nm)
            new_x = lm.steps2micron(lm.get_position(x_id))
            new_y = lm.steps2micron(lm.get_position(y_id))

            assert new_x - x > delta_pos, "Error: x position deviated by more than 10 steps"
            assert new_y - y > delta_pos, "Error: y position deviated by more than 10 steps"

            print(f"Motors moved to: {new_x, new_y}")

            return None

    def _move_rel_dir(self, _dir):
        """
        Move motors in given direction, move_strength is signed micrometer value.
        """
        with LinearMotor(serial_number=s_id) as lm:
            match _dir:
                case 'left':
                    lm.move_relative(x_id, self._move_strength)
                case 'right':
                    lm.move_relative(x_id, -1 * self._move_strength)
                case 'up':
                    lm.move_relative(y_id, self._move_strength)
                case 'down':
                    lm.move_relative(y_id, -1 * self._move_strength)

    def litho(self, expose_time_seconds = 43):

        # taken directly from PCOEdgeGUI-Litho
        with Serial('COM3', baudrate=115200, timeout=0.5) as s:

            s.readline()
            _message = f"<{expose_time_seconds}>".encode()
            s.write(_message)
            msg = s.readline().decode()
            print(msg)


    def load_bitmap(self):
        # Go and grab the name of the shape and load the pre-made file of positions.
        # Maybe auto generate

        scene = QGraphicsScene()

        print(f"{self._bitmap_choice}")
        pixmap = QPixmap(f"../Backend/Bitmaps/{self._bitmap_choice}")

        if pixmap.isNull():
            print("Failed to load bitmap - check path/file size.")

        view_size = self.ui.BITMAP_DISPLAY.viewport().size()
        print(view_size)
        # resize the bitmap to the graphics view window size. The fast transformation maintain [0,255] values.
        scaled_pixmap = pixmap.scaled(view_size.width(),
                                      view_size.height(),
                                      Qt.AspectRatioMode.IgnoreAspectRatio,
                                      Qt.TransformationMode.FastTransformation)

        scene.addPixmap(scaled_pixmap)

        self.ui.BITMAP_DISPLAY.setScene(scene)

        return None

    def bitmap2coords(self):
        """
        Convert a bitmap image to a set of coordinates to run an exposure on.
        select the black of white tiles of the bitmap to expose depending on resist.
        """
        coords = []


        return Coords
    def run_bitmap(self):
        """
        Convert bitmap to coords and step through that coord list in order exposing each step.
        """
        return None

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MotorControllerQt()
    widget.show()

    sys.exit(app.exec())

