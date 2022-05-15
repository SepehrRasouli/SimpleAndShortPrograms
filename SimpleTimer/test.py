import timer
import os
import pickle
import random
import string
from config import DATABASE_NAME
database = timer.database()
def readPickleData(database:str) -> list:
    '''Reads & Returns pickle data.'''
    with open(database,'rb') as pf:
        data = pickle.load(pf)
    return data

def test_createDatabase():
    '''Tests createDatabse function.'''
    # Test with override set to False
    fileName = random.sample(string.ascii_letters)
    database.createDatabase(override=False,databaseName='')
    assert os.path.isfile(DATABASE_NAME)

    # Test with override set to True
    database.createDatabase(override=False)
    assert os.path.isfile(DATABASE_NAME)

    os.remove(DATABASE_NAME)

def test_removeDatabase():
    '''Tests removedatabase function.'''
    database.createDatabase()
    database.removeDatabase()
    assert not os.path.isfile(DATABASE_NAME)

def test_dumpDataToDatabase():
    '''Tests dumpDataToDatabase function.'''
    database.createDatabase()
    database.dumpDataToDatabase([15])
    data = readPickleData()
