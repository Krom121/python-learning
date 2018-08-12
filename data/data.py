import pymysql

# connect to database
connection = pymysql.connect(host='localhost', port=3306, user='root', passwd='root', db='kite')

try:
   # run a query
    with connection.cursor() as cursor:
        sql = "SELECT * FROM student;"
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
finally:
   # close the connection
    connection.close()