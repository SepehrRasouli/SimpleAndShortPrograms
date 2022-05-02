import timer
import os
from config import DATABASE_NAME
database = timer.database()
def test_createDatabase():
    # Test with override set to False
    database.createDatabase(override=False)
    assert os.path.isfile(DATABASE_NAME)

    # Test with override set to True
    database.createDatabase(override=False)
    assert os.path.isfile(DATABASE_NAME)

    os.remove(DATABASE_NAME)

def test_removeDatabase():
    database.createDatabase()
    database.removeDatabase()
    assert not os.path.isfile(DATABASE_NAME)

def test_dumpDataToDatabase():
    database.createDatabase()
    database.dumpDataToDatabase([15])

