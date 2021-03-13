import sqlite3

class query_executor:
    def __init__(self, dbname: str):
        self.connection = sqlite3.connect(dbname)
        self.cursor = self.connection.cursor()
    
    def execute_query(self, query:str):
        result = None

        try:
            result = self.cursor.execute(query)
            self.connection.commit()
        except Exception as ex:
            print(ex)
        
        return result

    def __del__(self):
        self.cursor.close()
        self.connection.close()