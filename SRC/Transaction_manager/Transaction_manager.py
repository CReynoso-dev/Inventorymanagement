from contextlib import contextmanager


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












