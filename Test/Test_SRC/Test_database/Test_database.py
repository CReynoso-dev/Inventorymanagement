from SRC.Database.database import Database,Customer,Product,Sales,Base
import pytest
import random
import string


def test_create_db():
    db_name = "".join(random.choices(string.ascii_letters + string.ascii_uppercase,k=8))
    db = Database(db_name = f"{db_name}",sql = "sqlite")







