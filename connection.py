import pyodbc
import credentials

server = credentials.server
database = credentials.database
username = credentials.username
password = credentials.password

try:
    conn = pyodbc.connect(
        f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'
    )
    print("Succesful connection")

    # test
    cursor = conn.cursor()
    cursor.execute("SELECT @@version;")
    row = cursor.fetchone()
    while row:
        print(row)
        row = cursor.fetchone()

except pyodbc.Error as e:
    sqlstate = e.args[0]
    print("Error:", sqlstate)
    print("Error msg:", e)

finally:
    # Close connection
    if 'conn' in locals():
        conn.close()
        print("Closed connection")
