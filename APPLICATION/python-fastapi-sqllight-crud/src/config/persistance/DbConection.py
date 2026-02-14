import sqlite3
import threading

class DbConnection:
    def __init__(self, dbName: str):
        self.dbName = dbName
        self.local = threading.local()

    def _get_connection(self) -> sqlite3.Connection:
        if not hasattr(self.local, 'connection'):
            self.local.connection = sqlite3.connect(self.dbName)
        return self.local.connection
    
    def _get_cursor(self) -> sqlite3.Cursor:
        if not hasattr(self.local, 'cursor'):
            self.local.cursor = self._get_connection().cursor()
        return self.local.cursor
       
    def getDBConnection(self)-> sqlite3.Connection:
        return self._get_connection()
    
    def getDBCursor(self) -> sqlite3.Cursor:
        return self._get_cursor()