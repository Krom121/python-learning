import pymysql

connection = pymysql.connect(host='localhost', port=3306, user='root', passwd='root', db='kite')

try:
    with connection.cursor(pymysql.cursors.DictCursor) as cursor:
        sql = "SELECT * FROM Friends;"
        cursor.execute(sql)
        for row in cursor:
            print(row)
finally:
    connection.close()