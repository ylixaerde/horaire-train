import sqlite3

class App:
    def __init__(self):
        self.db_name = "data.sqlite"
        self.sql_init_script = "horaire-train.sql"

    def fn_init_db(self):
        sqliteConnection = None
        try:            
            with sqlite3.connect(self.db_name, timeout=10) as sqliteConnection:
                print(f"Connected to the database {self.db_name}")
                cursor = sqliteConnection.cursor()
                try:
                    with open(self.sql_init_script, "r") as sqlite_file:
                        try:
                            sql_script = sqlite_file.read()
                        except Exception as error:
                            print(f"Error while reading the SQL script: {error}")
                            return
                except Exception as error:
                    print(f"Error while opening the SQL file: {error}")
                    return
                
                try:
                    cursor.executescript(sql_script)
                    print("SQLite script executed successfully")
                except sqlite3.Error as error:
                    print(f"Error while executing SQLite script: {error}")
                finally:
                    cursor.close()
        except sqlite3.Error as error:
            print(f"Error while connecting to SQLite: {error}")
        except Exception as error:
            print(f"{error}")
        finally:
            if sqliteConnection:
                sqliteConnection.close()
                print("The SQLite connection is closed")


app = App()
app.fn_init_db()