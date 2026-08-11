import sys
from PySide6.QtCore import Qt, QSize
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel, QSizePolicy, QStackedWidget, QToolBar, QScrollArea
from PySide6.QtGui import QAction, QActionEvent
from PySide6.QtHelp import QHelpSearchEngine, QHelpEngineCore


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()


        self.setWindowTitle("INVENTORY MANAGEMENT")
        self.resize(500,500)
        self.book_widgit = QStackedWidget()
        self.setCentralWidget(self.book_widgit)

        self.starter_screen = self.Starting_screen()
        self.main_screen = self.Main_screen()
        self.customer_contact_screen = self.Customer_contact_screen()
        self.book_widgit.addWidget(self.starter_screen)
        self.book_widgit.addWidget(self.main_screen)
        self.book_widgit.addWidget(self.customer_contact_screen)

        self.Switch_Starting_screen()

    def on_button_click_sc(self):
        self.Switch_Main_screen()
    def Starting_screen(self):
        page = QWidget()
        layout = QVBoxLayout(page)

        title = QLabel("Main Menu")
        title_font = title.font()
        title_font.setPointSize(50)
        title.setFont(title_font)
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        starting_button = QPushButton("Start")
        starting_button.clicked.connect(self.on_button_click_sc)

        layout.addWidget(title)
        layout.addWidget(starting_button)
        return page
    def Main_screen(self):
        page = QWidget()
        layout = QVBoxLayout(page)
        toolbar = QToolBar("main",allowedAreas=Qt.ToolBarArea.TopToolBarArea)
        buttonAlertp = QAction("Alerts",parent=page)
        buttonStoresp = QAction("Stores",parent=page)
        buttonErrorlogp = QAction("Errors",parent=page)
        buttonStatistics = QAction("Statistics",parent=page)
        buttonUpdatep = QAction("Updates",parent=page)
        buttonInfop = QAction("Info",parent=page)
        buttonCustomerContactp = QAction("Customer Contact",parent=page)
        buttonCustomerContactp.triggered.connect(self.Switch_Customer_contact_screen)


        toolbar.addAction(buttonAlertp)
        toolbar.addAction(buttonStoresp)
        toolbar.addAction(buttonCustomerContactp)
        toolbar.addAction(buttonStatistics)
        toolbar.addAction(buttonErrorlogp)
        toolbar.addAction(buttonUpdatep)
        toolbar.addAction(buttonInfop)
        layout.addWidget(toolbar,alignment=Qt.AlignmentFlag.AlignTop)



        return page
    def Customer_contact_screen(self):
        page = QWidget()
        layout = QVBoxLayout(page)
        cc_scrollbar = QScrollArea()
        cc_toolbar = QToolBar("customer Contact",allowedAreas=Qt.ToolBarArea.TopToolBarArea)
        buttonBacktoMain = QAction("Back",parent=page)
        buttonAddCustomerInfo = QAction("Add",parent=page)
        buttonRemoveCustomerInfo = QAction("Remove",parent=page)
        buttonEditCustomerInfo = QAction("Edit",parent=page)



        cc_toolbar.addAction(buttonBacktoMain)
        cc_toolbar.addAction(buttonAddCustomerInfo)
        cc_toolbar.addAction(buttonRemoveCustomerInfo)
        cc_toolbar.addAction(buttonEditCustomerInfo)

        search_engine_config = QHelpEngineCore()
        search_engine = QHelpSearchEngine()

        layout.addWidget(cc_toolbar, alignment=Qt.AlignmentFlag.AlignTop)
        layout.addWidget(cc_scrollbar)
        #layout.addWidget(search_engine)





        return page




    def Switch_Starting_screen(self):
        self.book_widgit.setCurrentWidget(self.starter_screen)
    def Switch_Main_screen(self):
        self.book_widgit.setCurrentWidget(self.main_screen)
    def Switch_Alerts_screen(self):
        pass
    def Switch_Stores_screen(self):
        pass
    def Switch_Customer_contact_screen(self):
        self.book_widgit.setCurrentWidget(self.customer_contact_screen)
    def Switch_Statistics_screen(self):
        pass
    def Switch_Error_log(self):
        pass
    def Switch_Update_screen(self):
        pass
    def Switch_Info_screen(self):
        pass



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
