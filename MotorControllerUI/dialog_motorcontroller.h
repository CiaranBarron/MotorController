#ifndef DIALOG_MOTORCONTROLLER_H
#define DIALOG_MOTORCONTROLLER_H

#include <QDialog>

namespace Ui {
class Dialog_MotorController;
}

class Dialog_MotorController : public QDialog
{
    Q_OBJECT

public:
    explicit Dialog_MotorController(QWidget *parent = nullptr);
    ~Dialog_MotorController();

private:
    Ui::Dialog_MotorController *ui;
};

#endif // DIALOG_MOTORCONTROLLER_H
