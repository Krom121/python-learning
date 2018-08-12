import pymysql

# INSERT MANY ROWS

conection = pymysql.Connection(host='localhost', port=3306, user='root', passwd='root', db='kite')

try:
    with conection.cursor() as cursor:
        rows = [("jim", 64, "1964-01-27 10:34:12"),
                ("sue", 27, "1991-08-02 13:25:32"),
                ("tom", 37, "1982-03-05 03:22:09")]
        cursor.executemany("INSERT INTO Friends VALUES (%s, %s, %s);", rows)
        conection.commit()

finally:
    conection.close()

