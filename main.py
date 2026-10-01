import sys

from gui import MainWindow,QApplication
from database import Database
from Service import Service
from Repository import Repository

def main():
    app = QApplication(sys.argv)
    db = Database("superb.db")
    repo = Repository(db)
    serv = Service(repo)


    window = MainWindow(serv)
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()