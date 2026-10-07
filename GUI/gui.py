import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel, QStackedWidget, QToolBar, QScrollArea,QLayout, QLineEdit, \
    QGridLayout
from PySide6.QtGui import QAction

from SRC.Database.database import Database
from SRC.Service import Service
from SRC.Repo.Repository import Repository




class MainWindow(QMainWindow):
    def __init__(self,serv):
        self.services = serv
        super().__init__()


        self.setWindowTitle("INVENTORY MANAGEMENT")
        self.resize(500,500)
        self.book_widgit = QStackedWidget()
        self.setCentralWidget(self.book_widgit)

        self.starter_screen = self.Starting_screen()
        self.main_screen = self.Main_screen()
        self.customer_contact_screen = self.Customer_contact_screen()
        self.add_customer_contact_info = self.Add_cc_screen()
        self.delete_customer_info = self.Delete_cc_screen()
        self.district = self.Stores_screen()
        self.book_widgit.addWidget(self.district)
        self.book_widgit.addWidget(self.starter_screen)
        self.book_widgit.addWidget(self.main_screen)
        self.book_widgit.addWidget(self.customer_contact_screen)
        self.book_widgit.addWidget(self.add_customer_contact_info)
        self.book_widgit.addWidget(self.delete_customer_info)

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
        buttonStoresp.triggered.connect(self.Switch_Stores_screen)


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

        buttonBacktoMain.triggered.connect(self.Switch_Main_screen)
        buttonAddCustomerInfo.triggered.connect(self.Switch_add_customer_info)
        buttonRemoveCustomerInfo.triggered.connect(self.Switch_delete_customer_info)
        #buttonAddCustomerInfo.triggered.connect()


        self.search_bar_cc = QLineEdit(parent=page)



        self.scrollbar_widget_cc = QWidget()
        self.scrollbar_layout_cc = QGridLayout(self.scrollbar_widget_cc)
        self.scrollbar_layout_cc.setSizeConstraint(QLayout.SizeConstraint.SetMinAndMaxSize)
        self.cc_scrollbar = QScrollArea()
        self.scrollbar_layout_cc.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.cc_scrollbar.setWidgetResizable(True)


        self.scrollbar_layout_cc.setSpacing(0)
        self.scrollbar_layout_cc.setContentsMargins(0,0,0,0)


        self.cc_scrollbar.setWidget(self.scrollbar_widget_cc)
        #self.cc_scrollbar.setLayout(self.scrollbar_layout_cc)
        self.search_bar_cc.returnPressed.connect(self.update_display_cc)
        self.search_bar_cc.textEdited.connect(self.erase_display_cc)








        self.layout_cc.addWidget(self.cc_toolbar, alignment=Qt.AlignmentFlag.AlignTop)

        self.layout_cc.addWidget(self.search_bar_cc,alignment=Qt.AlignmentFlag.AlignTop)
        #layout.addWidget(datatest)
        self.layout_cc.addWidget(self.cc_scrollbar)






        return page

    def Add_cc_screen(self):
        page = QWidget()
        layout_add_cc_screen = QVBoxLayout(page)

        add_cc_screen_toolbar = QToolBar("Add customer info",allowedAreas=Qt.ToolBarArea.TopToolBarArea)



        BackButton = QAction("Back",parent=page)

        add_cc_screen_toolbar.addAction(BackButton)
        BackButton.triggered.connect(self.Switch_Customer_contact_screen)
        self.add_new_cc = QLineEdit(parent=page)
        self.add_new_cc.returnPressed.connect(self.add_new_cc_function)
        new_cc_format = QLabel("write new customer info in this format: customer_name,customer_number,customer_email")



        layout_add_cc_screen.addWidget(add_cc_screen_toolbar,alignment= Qt.AlignmentFlag.AlignTop)
        layout_add_cc_screen.addWidget(new_cc_format)
        layout_add_cc_screen.addWidget(self.add_new_cc,alignment= Qt.AlignmentFlag.AlignTop)
        layout_add_cc_screen.addStretch(0)
        #layout_add_cc_screen.addWidget(hey)



        return page
    def add_new_cc_function(self):
        text = self.add_new_cc.text()
        print(text.split(","))

        database.add_customer_data("inventoryonhand.db",text)

    def Delete_cc_screen(self):
        page = QWidget()
        Delete_cc_screen_layout = QVBoxLayout(page)
        Delete_cc_toolbar = QToolBar("delete screen toolbar",allowedAreas=Qt.ToolBarArea.TopToolBarArea)
        backbutton = QAction("Back",parent=page)
        refreshbutton = QAction("Refresh",parent=page)
        Delete_cc_toolbar.addAction(backbutton)
        Delete_cc_toolbar.addAction(refreshbutton)
        backbutton.triggered.connect(self.Switch_Customer_contact_screen)

        Delete_cc_scrollarea_widget = QWidget()
        self.Delete_cc_scrollarea_layout = QGridLayout(Delete_cc_scrollarea_widget)
        Delete_cc_scrollarea = QScrollArea()
        self.Delete_cc_scrollarea_layout.setSizeConstraint(QLayout.SizeConstraint.SetMinAndMaxSize)
        Delete_cc_scrollarea.setWidgetResizable(True)
        self.Delete_cc_scrollarea_layout.setSpacing(0)
        self.Delete_cc_scrollarea_layout.setContentsMargins(0,0,0,0)
        Delete_cc_scrollarea.setWidget(Delete_cc_scrollarea_widget)




        Delete_cc_screen_layout.addWidget(Delete_cc_toolbar, alignment=Qt.AlignmentFlag.AlignTop)
        Delete_cc_screen_layout.addWidget(Delete_cc_scrollarea)





        return page



    def erase_display_cc(self):
        for i in reversed(range(self.scrollbar_layout_cc.count())):
            self.scrollbar_layout_cc.itemAt(i).widget().setParent(None)
    def update_display_cc(self):
        search_input = self.search_bar_cc
        text = search_input.text()
        search_output = self.services.Lookup_customer(text)
        print(search_output)
        rowcounter = -1
        columncounter = 0
        for result in search_output:
            rowcounter+=1
            columncounter = 0
            for data in result:
                columncounter+=1
                column = QLabel(f"{data}")
                column.setStyleSheet("""boarder: 2px solid black;
                                     """)
                self.scrollbar_layout_cc.addWidget(column,rowcounter,columncounter)











        return
    #you ended with being able to add the stuff on you need to figure out how to remove it set the borders and make it scrollable its not scrolling















    def Switch_Starting_screen(self):
        self.book_widgit.setCurrentWidget(self.starter_screen)
    def Switch_Main_screen(self):
        self.book_widgit.setCurrentWidget(self.main_screen)
    def Switch_add_customer_info(self):
        self.book_widgit.setCurrentWidget(self.add_customer_contact_info)
    def Switch_delete_customer_info(self):
        self.book_widgit.setCurrentWidget(self.delete_customer_info)


    def Switch_Alerts_screen(self):
        pass
    def Switch_Stores_screen(self):
        self.book_widgit.setCurrentWidget(self.district)

        pass
    def Stores_screen(self):
        page = QWidget()
        stores_layout = QVBoxLayout(page)




        return page
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
    db = Database("superb.db")
    repo = Repository(db)
    serv = Service(repo)
    window = MainWindow(serv)
    window.show()
    sys.exit(app.exec())
