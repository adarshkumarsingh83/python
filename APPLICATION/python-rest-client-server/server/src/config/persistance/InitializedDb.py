import sqlite3
from src.config.persistance.DbConection import DbConnection

class InitializedDb:
    def __init__(self, dbConnection: DbConnection, dbScriptPath: str):
        self.dbConnection = dbConnection
        self.dbScriptPath = dbScriptPath
        self.initializeDb()

    def initializeDb(self):
        print("Initializing database...")
        connection: sqlite3.Connection = self.dbConnection.getDBConnection()
        cursor: sqlite3.Cursor = self.dbConnection.getDBCursor()
        try:
            with open(self.dbScriptPath, 'r') as file:
                sqlScript = file.read()
                # execute the SQL script to initialize the database
                cursor.executescript(sqlScript)
                # commit changes to the database
                connection.commit()
                print("Database initialized successfully.")
        except Exception as e:
            print(f"Error initializing database: {e}")
            #close the connection in case of error
            connection.close()