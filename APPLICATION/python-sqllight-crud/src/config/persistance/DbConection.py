import sqlite3

class DbConnection:
    def __init__(self, dbName: str):
        self.dbName = dbName
        self.connection = None
        self.cursor = None
        self.connect()

    def connect(self):
       self.connection = sqlite3.connect(self.dbName)
       self.cursor = self.connection.cursor()
       
    def getDBConnection(self)-> sqlite3.Connection:
        con: sqlite3.Connection = self.connection
        if not con:
            try:
                self.connection.execute("SELECT 1")
            except sqlite3.ProgrammingError:
                self.connect()
        return self.connection
    
    def getDBCursor(self) -> sqlite3.Cursor:
        cur: sqlite3.Cursor = self.cursor
        if not cur:
            try:
                self.connection.execute("SELECT 1")
            except sqlite3.ProgrammingError:
                self.connect()
        return self.cursor
