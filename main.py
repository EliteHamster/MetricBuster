# This Python file uses the following encoding: utf-8
import sys
import os
import math


from PySide2.QtWidgets import QApplication, QWidget
from PySide2.QtCore import QFile
from PySide2.QtUiTools import QUiLoader


class Calc(QWidget):
    def __init__(self):
        super(Calc, self).__init__()
        self.load_ui()

    def load_ui(self):
        loader = QUiLoader()
        path = os.path.join(os.path.dirname(__file__), "form.ui")
        ui_file = QFile(path)
        ui_file.open(QFile.ReadOnly)
        loader.load(ui_file, self)
        ui_file.close()

if __name__ == "__main__":
    app = QApplication([])
    widget = Calc()
    widget.show()
    sys.exit(app.exec_())

def changedValue(self):
    height = float(self.slider.value())
    inches = height * 3.937
    feetinches = inches // 12
    leftoverinches = inches %12
    self.TestLabel.value = "feetinches"
    print ("This is how tall you are in inches: ",inches)
    print ("This is how tall you are in ft", math.trunc(feetinches), "ft", math.trunc(leftoverinches), "Inches")
