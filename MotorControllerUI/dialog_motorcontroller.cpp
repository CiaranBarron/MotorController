#include "dialog_motorcontroller.h"
#include "ui_dialog_motorcontroller.h"

Dialog_MotorController::Dialog_MotorController(QWidget *parent)
    : QDialog(parent)
    , ui(new Ui::Dialog_MotorController)
{
    ui->setupUi(this);
}

Dialog_MotorController::~Dialog_MotorController()
{
    delete ui;
}
