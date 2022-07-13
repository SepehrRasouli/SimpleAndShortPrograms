# Simple alternative timer to Microsoft's Alarms & Clock. 
# I'm making this app since I couldn't find any FOSS alternative to 'Alarms & Clock' app.
from typing import List
import os
import pickle
from config import VERBOSE,ALARM_VISUAL,NOTIFICATIONS,SOUND,DATABASE_NAME
class database:
	'''Loads and edits database.'''
	def loadDatabase(self,databaseName:str=DATABASE_NAME) -> List[int,None,List[int]] or List[int,str,None]:
		'''Loads database and returns a list of intervals.
		Args:
			DATABASE_NAME:str: database name to load.
		Returns:
			If successful :
				List[
					int: 0 for completion
					None: None because no error occured.
					List[int]: dump data.
					]
			Else:
				List[
					int: 1 for error.
					str: error explaination.
					None: No data gets returned.
					]
		'''
		if not isinstance(databaseName,int):
			if os.path.isfile(DATABASE_NAME):
				with open(DATABASE_NAME,'rb') as pf:
					data = pickle.load(pf)
				return [0,None,data]
			return [1,'Error: Database Not found. Please check DATABASE_NAME variable.',None]

		return [1,'Error: Database name should not be an integer.',None]

	def dumpDataToDatabase(self,dump:list,databaseName:str=DATABASE_NAME) -> List[int,None] or List[int,str]:
		'''Dumps data to pickle database.
		Args:
			DATABASE_NAME:str: database name to dump data to.
		Returns:
			If successful :
				List[
					int: 0 for completion
					None: None because no error occured.
					]
			Else:
				List[
					int: 1 for error.
					str: error explaination.
					]
		'''
		if not isinstance(databaseName,int):
			if os.path.isfile(DATABASE_NAME):
				with open(DATABASE_NAME,'wb') as pf:
					pickle.dump(dump,pf)
				return [0,None]
			return [1,'Error: Database Not found. Please check DATABASE_NAME variable.']
		return [1,'Error: Database name should not be an integer.']

	def createDatabase(self,override:int=False,databaseName:str=DATABASE_NAME):
		'''Creates a new database with DATABASE_NAME variable as it's name.
		Args:
			DATABASE_NAME:str: database name to create.
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

		with open(DATABASE_NAME,'wb') as pf:
			pickle.dump([],pf)

	def removeDatabase(self,databaseName:str=DATABASE_NAME):
		'''Removes DATABSE_NAME.
		Args:
			DATABASE_NAME:str: database name to remove.
		Returns:
		 str: completion message.
		'''
		if os.path.isfile(DATABASE_NAME):
			os.remove(DATABASE_NAME)
			return 'Done Removing Database.'

	def removeDatabaseEntry(self,entry_index:int,databaseName:str=DATABASE_NAME) -> list or int:
		'''Removes a database entry.
		Args:
			entry_index: int: entry index
			DATABASE_NAME : str: database name to remove entry from.
		Returns:
		list: modified database if modification was succsessful.
		int: If modification was unsuccessful. 
		'''    
		if not isinstance(entry_index,int):
			return 0
		database = self.load_database()
		if not isinstance(database,list):
			return 0
		database.pop(entry_index)
		return database
	
	def addDatabaseEntry(self,interval,databaseName:str=DATABASE_NAME) -> list or int:
		'''Adds a database entry.
		Args:
			DATABASE_NAME:str database name to load.
			interval:int: time interval.
		Returns:
			list: modified database if modification was succsessful.
			int: If modification was unsuccessful. 
		'''   
		if not isinstance(interval,int):
			return 0
		database = self.load_database()
		if not isinstance(database,list):
			return 0
		database.append(interval)
		return database

class cli:
    pass

class commandInterpreter:
    pass

class timerManager:
    pass

