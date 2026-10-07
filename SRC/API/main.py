import sys

from GUI.gui import MainWindow,QApplication
from SRC.Database.database import Database
from SRC.Service import Service
from SRC.Repo.Repository import Repository

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