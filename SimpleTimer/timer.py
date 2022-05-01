# Simple alternative timer to Microsoft's Alarms & Clock. 
# I'm making this app since I couldn't find any FOSS alternative to 'Alarms & Clock' app.
from typing import List
import os
import pickle
from config import VERBOSE,ALARM_VISUAL,NOTIFICATIONS,SOUND,DATABASE_NAME
verbose_print = print if VERBOSE else lambda *a,**k:None
class database:
	'''Loads and edits database.'''
	def loadDatabase(self) -> List[int]:
		'''Loads database and returns a list of intervals.
		Returns:
		List[int]: loaded database.
		str: error.
		'''
		if os.path.isfile(DATABASE_NAME):
			with open(DATABASE_NAME,'rb') as pf:
				data = pickle.load(pf)
			return data
		verbose_print('Error: Database Not found. Please check DATABASE_NAME variable.')

	def createDatabase(self,override:int=False):
		'''Creates a new database with DATABASE_NAME variable as it's name.
		Args:
			override: True to remake existing database. Default is False
		'''
		if os.path.isfile(DATABASE_NAME):
			if not override:
				verbose_print('Error: database already exists, set override to True to remake existing database.')
			else:
				os.remove(DATABASE_NAME)
				with open(DATABASE_NAME,'wb') as pf:
					pickle.dump([],pf)
				verbose_print('Done Overriding and creating database.')

		with open(DATABASE_NAME,'wb') as pf:
			pickle.dump([],pf)
			verbose_print('Done Creating Database.')


	def removeDatabaseEntry(self,entry_index:int) -> list or int:
		'''Removes a database entry.
		Args:
			entry_index: int
		Returns:
		list: modified database if modification was succsessful.
		int: If modification was unsuccessful. 
		'''    
		if not isinstance(entry_index,int):
			verbose_print('entry index is not integer.')
			return 0
		database = self.load_database()
		if not isinstance(database,list):
			verbose_print('database is not of type list')
			return 0
		database.pop(entry_index)
		return database
	
	def addDatabaseEntry(self,interval) -> list or int:
		'''Adds a database entry.
		Args:
			data: int
		Returns:
		list: modified database if modification was succsessful.
		int: If modification was unsuccessful. 
		'''   
		if not isinstance(interval,int):
			verbose_print('interval is not integer.')
			return 0
		database = self.load_database()
		if not isinstance(database,list):
			verbose_print('database is not of type list')
			return 0
		database.append(interval)
		return database


class cli:
    pass

class commandInterpreter:
    pass

class timerManager:
    pass

