import pymysql
import datetime

# INSERT DATA VALUES

connection = pymysql.connect(host='localhost', port=3306, user='root', passwd='root', db='kite')

try:
    with connection.cursor() as cursor:
        row = ("bob", 28, "1990-02-06 23:04:56")
        cursor.execute("INSERT INTO Friends VALUES (%s, %s, %s);", row)
        connection.commit()

finally:
    connection.close()