import pymysql
import datetime

connection = pymysql.connect(host='localhost', port=3306, user='root', passwd='root', db='kite')

    # show tables
try:
    with connection.cursor() as cursor:
        cursor.execute("SHOW TABLES")
        for (table_name) in cursor:
            print(table_name)
finally:
    connection.close()

    # Create tables

#try:
    #with connection.cursor() as cursor:
       # cursor.execute("""CREATE TABLE IF NOT EXISTS Friends(name char(20), age int, DOB datetime);""")
#finally:
    #connection.close()
