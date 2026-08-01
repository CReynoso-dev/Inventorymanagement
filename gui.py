import sys
from PySide6.QtCore import Qt, QSize
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel, QSizePolicy

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()


        self.setWindowTitle("INVENTORY MANAGEMENT")
        self.resize(500,500)


        main_widgit = QWidget()


        layout = QVBoxLayout(main_widgit)

        Title = QLabel("WareHouse management")



        layout.addWidget(Title)




        self.setCentralWidget(main_widgit)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
