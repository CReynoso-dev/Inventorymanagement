from contextlib import contextmanager
from sqlalchemy.orm import sessionmaker,Session


from SRC.Database.database import Database

class Transaction_manager():
    def __init__(self,db : Database):
        self.database = db

    @contextmanager
    def create_transaction(self):
        session = self.database.Get_connection()
        try:
            yield session
            session.commit()
        except:
            session.rollback()
            raise ValueError("rollback")

        finally:
            session.close()





