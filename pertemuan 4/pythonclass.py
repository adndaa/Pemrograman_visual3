from PyQt5.QtWidgets import  QMainWindow, QWidgets, QApplication, QPushButton, QLabel

class MyWindow(MainWindow):
    def __inir__(self):
        super().__init__()
        self.label = QLabel(self)
        self.label.setText("Label1")
        self.label.move(200, 0)
        self.button = QPushButton(self)
        self.button.setText("Button1")

app = QApplication([])
window = MyWindow()
window.show()
app.exec_()