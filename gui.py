import sys
from PySide6.QtCore import Qt, QSize, QMetaMethod
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel, QSizePolicy, QStackedWidget, QToolBar, QScrollArea,QLayout, QLineEdit, QFrame, QGridLayout,QHBoxLayout
from PySide6.QtGui import QAction, QActionEvent

import database
from database import Search_function_cc



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
        self.layout_cc = QVBoxLayout(page)
        datatest = QLabel("fuckyou\nh\nhey\nhey\nhey")


        self.cc_toolbar = QToolBar("customer Contact",allowedAreas=Qt.ToolBarArea.TopToolBarArea)
        buttonBacktoMain = QAction("Back",parent=page)
        buttonAddCustomerInfo = QAction("Add",parent=page)
        buttonRemoveCustomerInfo = QAction("Remove",parent=page)
        buttonEditCustomerInfo = QAction("Edit",parent=page)




        self.cc_toolbar.addAction(buttonBacktoMain)
        self.cc_toolbar.addAction(buttonAddCustomerInfo)
        self.cc_toolbar.addAction(buttonRemoveCustomerInfo)
        self.cc_toolbar.addAction(buttonEditCustomerInfo)


        self.search_bar_cc = QLineEdit(parent=page)



        self.scrollbar_widget_cc = QWidget()
        self.scrollbar_layout_cc = QGridLayout(self.scrollbar_widget_cc)
        self.cc_scrollbar = QScrollArea()
        self.scrollbar_layout_cc.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.cc_scrollbar.setWidgetResizable(True)


        self.scrollbar_layout_cc.setSpacing(0)
        self.scrollbar_layout_cc.setContentsMargins(0,0,0,0)


        self.cc_scrollbar.setWidget(self.scrollbar_widget_cc)
        self.cc_scrollbar.setLayout(self.scrollbar_layout_cc)
        self.search_bar_cc.returnPressed.connect(self.update_display_cc)





        self.layout_cc.addWidget(self.cc_toolbar, alignment=Qt.AlignmentFlag.AlignTop)

        self.layout_cc.addWidget(self.search_bar_cc,alignment=Qt.AlignmentFlag.AlignTop)
        #layout.addWidget(datatest)
        self.layout_cc.addWidget(self.cc_scrollbar)





        return page
    def update_display_cc(self):
        search_input = self.search_bar_cc.text()
        search_output = database.Search_function_cc("inventoryonhand.db",search_input)
        for i in range(len(search_output)):
            beep = search_output[i]
            print(beep,"outer")
            for z in range(len(search_output[0])):
                print(beep[z],"inner")



                self.scrollbar_layout_cc.addWidget(QLabel(f"{beep[z]}"))




        return print(search_output)
    #you ended with being able to add the stuff on you need to figure out how to remove it set the borders and make it scrollable its not scrolling















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
