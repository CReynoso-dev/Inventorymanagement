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
        except:
            session.rollback()
        finally:
            session.close()
    def confirm_orm_object(self, session : Session, object):
        try:
            session.add(object)
        except:
            session.rollback()
            raise "standin for real error"
    def execute_orm_sql(self,session : Session,sql):
        try:
            session.execute(sql)
        except:
            session.rollback()
            raise "standin for real error"


    def end_transaction(self,session : Session):
        try:
            session.commit()
            session.close()
        except:
            session.rollback()
            raise "error"







