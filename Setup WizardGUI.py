import sys
from PySide6.QtCore import Qt, QSize, QMetaMethod
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel, QSizePolicy, QStackedWidget, QToolBar, QScrollArea,QLayout, QLineEdit, QFrame, QGridLayout,QHBoxLayout
from PySide6.QtGui import QAction, QActionEvent, QPixmap, QImage



class SetupWizardWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Ocean management")
        self.resize(500,500)
        self.book_Widget = QStackedWidget()
        self.setCentralWidget(self.book_Widget)
        self.starting_sc = self.Welcome_screen()

        self.book_Widget.addWidget(self.starting_sc)
        self.Welcome_screen()

    def Welcome_screen(self):
        page = QWidget()
        Welcome_layout = QVBoxLayout(page)
        pixmap = QPixmap("logo.png")
        Logo = QLabel(parent=page)
        Logo.setFixedSize(100,100)
        Logo.setScaledContents(True)
        Logo.setPixmap(pixmap)
        welcome_statement = QLabel("""Welcome to Ocean Deep Endless.\n
Let’s get your inventory system set up and ready to work for you.\n This wizard will guide you through the essentials—your business details, inventory locations, products, and scanning preferences—so you can start tracking inventory quickly and confidently.
When your problems are endless, throw them in the ocean.""")











        Welcome_layout.addWidget(Logo,alignment=Qt.AlignmentFlag.AlignTop|Qt.AlignmentFlag.AlignCenter)
        Welcome_layout.addWidget(welcome_statement,alignment=Qt.AlignmentFlag.AlignTop|Qt.AlignmentFlag.AlignCenter)







        return page






if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SetupWizardWindow()
    window.show()
    sys.exit(app.exec())
