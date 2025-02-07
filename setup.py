
from cx_Freeze import Executable, setup


options = {
    "build_exe": {
        "includes": ["ui_form_1p5", "Backend.LithographyController", "Backend.Electronic_Modules.Koco_Linear_Actuator.linearmotor_comms"],
        "excludes": []
    }
}


setup(
    name="Motors",
    version="1.5",
    description="GUI for controlling motor positioning and lithography light source & exposure.",
    options=options,
    executables=[Executable("motorcontrollerqt_1.5.py",
                            copyright="Copyright (C) 2025 Ciaran Barron",
                            icon="motor_icon.ico",
                            shortcut_name="LithoMotors",
                            shortcut_dir="LithoMotors",
                            )],
)



'''
Version history:
1   -   Basic setup for controlling old motors. 
1.5 -   Includes controls for litho and improved motor controls. (new motors)
'''
