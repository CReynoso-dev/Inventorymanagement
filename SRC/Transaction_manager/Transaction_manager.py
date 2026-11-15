from contextlib import contextmanager
from sqlalchemy.orm import sessionmaker,Session


from SRC.Database.database import Database

class Transaction_manager():
    def __init__(self,db : Database):
        self.database = db

    @contextmanager
    def start_transaction(self):
        session = self.database.Get_connection()
        try:
            yield session
            session.commit()
        except Exception:
            session.rollback()
            raise

        finally:
            session.close()




    def end_transaction(self,session : Session):
        try:
            session.commit()
            session.close()
        except:
            session.rollback()
            raise "error"







