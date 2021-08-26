import psycopg2
from Configuration import Configuration
from psycopg2.extras import RealDictCursor
from flask import jsonify
import simplejson as json


class DB:
    def __init__(self):
        self.config = Configuration()
        
    def start_connection(self):
        #establishing the connection
        conn = psycopg2.connect(
            database = self.config.database, 
            user = self.config.user, 
            password = self.config.password, 
            host = self.config.host, 
            port= self.config.port
        )

        conn.autocommit = True
        cursor = conn.cursor(cursor_factory=RealDictCursor)
        return conn, cursor

    def create_table(self, name):
        conn, cursor = self.start_connection()
        #Preparing query to create a database
        command = """
                    CREATE TABLE %s (
                        id SERIAL PRIMARY KEY,
                        title VARCHAR(255) NOT NULL,
                        text VARCHAR(255) NOT NULL)
                  """%name
        try:
            #Creating a database
            cursor.execute(command)
            cursor.close()
            print("..........Table created successfully........")
            conn.commit()
            #Closing the connection
            conn.close()
        except:
            raise 

    def insert_note(self, table_name ,title, text):
        try:
            conn, cursor = self.start_connection()
            cursor.execute("""INSERT INTO notes (title, text) VALUES (%s,%s)""",(title ,text))
            cursor.close()
            conn.commit()
            #Closing the connection
            conn.close()
            return {'title':title, 'text':text}, 201
        except:
            return 400
    def get_all_notes(self):
        try:
            conn, cursor = self.start_connection()
            cursor.execute("""SELECT * FROM notes """)
            notes = cursor.fetchall()
            cursor.close()
            conn.commit()
            #Closing the connection
            conn.close()
            return json.dumps(notes)
        except:
            return 400


