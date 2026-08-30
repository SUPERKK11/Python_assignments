import sqlite3
class user_registration:
    def __init__(self,name,email,age,password):
        try:
                    self.conn=sqlite3.Connection("Amazon.db")
                    self.curr=self.conn.cursor()
                    self.curr.execute(
                    """
                    Insert Into User_detail values (?,?,?,?);             
                    """,
                    (name,email,age,password))
                    self.conn.commit()
                    self.conn.close()
        except:
                    print("Registration failed")
        else:
                    print("Registraion successfully")