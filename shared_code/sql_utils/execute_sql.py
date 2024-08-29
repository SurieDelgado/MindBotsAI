from openai import OpenAI
import pyodbc
import os

class SQLExecutor(): 
    def __init__(self):
        
        print("",pyodbc.drivers())

        self.cursor = self.conexion().cursor()

    def execute_query(self, query):
        self.cursor.execute(query)
        results = []
        field_map = {}
        for index, row in enumerate(self.cursor.description):
            field_map[index] = row[0]

        for row in enumerate(self.cursor.fetchall()):
            new_row = {}

            for index, field in enumerate(row[1]):
                new_row[field_map[index]] = field
            results.append(new_row)

        return results

    def conexion(self):
        """ Connect to the SQL database server """
        conn = None
        try:
            print('Connecting to the SQL database...')
            server=os.environ['sql_url']
            user=os.envion['sql_user']
            password=os.envion['sql_pass']
            database=os.envion['sql_db']
            driver = '{ODBC Driver 18 for SQL Server}'
            print(f'DRIVER={driver};SERVER={server};DATABASE={database};UID={user};PWD={password};')
            conn = pyodbc.connect(
                f'DRIVER={driver};SERVER={server};DATABASE={database};UID={user};PWD={password};'
            )
            return conn

        except (Exception, pyodbc.DatabaseError) as error:
            print(error)
            return None