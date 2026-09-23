import sys
from PySide6.QtCore import Qt, QSize, QMetaMethod
from PySide6.QtWidgets import QApplication,QFileDialog, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel, QSizePolicy, QStackedWidget, QToolBar, QScrollArea,QLayout, QLineEdit, QFrame, QGridLayout,QHBoxLayout
from PySide6.QtGui import QAction, QActionEvent, QPixmap, QImage
from Scanning_data import scanner_reader

import database


class SetupWizardWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Ocean management")
        self.resize(500,500)
        self.book_Widget = QStackedWidget()
        self.setCentralWidget(self.book_Widget)
        self.starting_sc = self.Welcome_screen()
        self.setup_database_sc = self.Database_setup_screen()
        self.setup_database_sc2 = self.Database_setup_screen_2()
        self.book_Widget.addWidget(self.starting_sc)
        self.book_Widget.addWidget(self.setup_database_sc)
        self.book_Widget.addWidget(self.setup_database_sc2)
        self.Welcome_screen()

    def Welcome_screen(self):
        page = QWidget()
        Welcome_layout = QGridLayout(page)
        Welcome_layout.setHorizontalSpacing(0)

        pixmap = QPixmap("logo.png")
        Logo = QLabel()
        Logo.setFixedSize(100,100)
        Logo.setScaledContents(True)
        Welcome_layout.setSpacing(0)
        Welcome_layout.setContentsMargins(0,0,0,0)

        Logo.setPixmap(pixmap)
        welcome_statement = QLabel("""Welcome to Ocean Deep Endless.\n
Let’s get your inventory system set up and ready to work for you.\n This wizard will guide you through the essentials\n—your business details, inventory locations, products,\n and scanning preferences—so you can start tracking inventory quickly and confidently.
When your problems are endless, throw them in the ocean.""")

        quit = QPushButton("quit")
        quit.setSizePolicy(QSizePolicy.Policy.Fixed,QSizePolicy.Policy.Fixed)
        next = QPushButton("next")
        next.setSizePolicy(QSizePolicy.Policy.Fixed,QSizePolicy.Policy.Fixed)
        next.clicked.connect(self.Switch_Database_setup_screen)













        Welcome_layout.addWidget(welcome_statement,2,1,1,1)

        Welcome_layout.addWidget(quit,5,5)
        Welcome_layout.addWidget(next,5,6)






        return page
    def Switch_Database_setup_screen(self):
        self.book_Widget.setCurrentWidget(self.setup_database_sc)
    def Database_setup_screen(self):
        page = QWidget()
        Database_setup_layout = QVBoxLayout(page)
        h = QHBoxLayout()
        instruction = QLabel("Making Product Database and Customer_contact Database")
        #database.Creation_of_database(sys.platform)
        self.Name_of_database = f"{sys.platform}"










        next = QPushButton("next")

        next.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        back = QPushButton("back")
        back.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)


        Database_setup_layout.setSpacing(0)
        Database_setup_layout.setContentsMargins(0,0,0,0)


        Database_setup_layout.addWidget(instruction)

        next.clicked.connect(self.Switch_database_setup_screen2)


        Database_setup_layout.addStretch()
        h.addWidget(back)
        h.addWidget(next)
        Database_setup_layout.addLayout(h)







        return page
    def Switch_database_setup_screen2(self):
        self.book_Widget.setCurrentWidget(self.setup_database_sc2)
    def Inserting_UPC(self,nod,upc):

        database.Adding_product_upc(nod,upc)


        pass




    def Database_setup_screen_2(self):
        page = QWidget()
        Database_setup_layout_2 = QVBoxLayout(page)
        h = QHBoxLayout()
        horizantal = QHBoxLayout()
        instructions = QLabel("Scan one of each products UPC and input the following fields of information")
        added_products = QScrollArea()
        actual_product = QWidget()
        actual_product_l = QGridLayout(actual_product)
        added_products.setWidget(actual_product)
        added_products.setWidgetResizable(True)
        template1 = QLabel("UPC")
        template1.setContentsMargins(0,0,0,0)
        template1.setFrameShape(QFrame.Shape.Box)
        template2 = QLabel("Name")
        template2.setContentsMargins(0, 0, 0, 0)
        template2.setFrameShape(QFrame.Shape.Box)
        template3 = QLabel("Quantity")
        template3.setSizePolicy(QSizePolicy.Policy.Fixed,QSizePolicy.Policy.Fixed)
        template3.setContentsMargins(0,0,0,0)
        template3.setFrameShape(QFrame.Shape.Box)
        template4 = QLabel("Description")
        template4.setContentsMargins(0, 0, 0, 0)
        template4.setFrameShape(QFrame.Shape.Box)
        next = QPushButton("Next")
        back = QPushButton("Back")
        horizantal.addWidget(back)
        horizantal.addWidget(next)
        scanner = scanner_reader()
        database.Adding_product_upc("inventoryonhand.db", scanner.start_reader(True))

        actual_product_l.addWidget(template1,1,0)
        actual_product_l.addWidget(template2,1,1)
        actual_product_l.addWidget(template3,1,2)
        actual_product_l.addWidget(template4,1,3)
        #actual_product_l.addLayout(h)











        Database_setup_layout_2.addWidget(instructions)
        Database_setup_layout_2.addWidget(added_products)
        Database_setup_layout_2.addStretch()
        Database_setup_layout_2.addLayout(horizantal)


        return page








if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SetupWizardWindow()
    window.show()
    sys.exit(app.exec())
