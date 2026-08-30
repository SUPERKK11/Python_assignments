import sqlite3
import menu
class DataBase:
    def __init__(self):
        try:
            self.conn=sqlite3.Connection("Amazon.db")
            self.curr=self.conn.cursor()
            self.curr.execute(
            """
            create table User_detail
            (
            name varchar(20),
            email varchar(20),
            age number(2),
            password varchar(30)    
            )                  
            """)
            self.conn.commit()
            self.conn.close()
        except:
            print("connection Successfully , table already created")
        else:
            print("connection successfully")
    
        
        

