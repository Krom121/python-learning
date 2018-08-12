import pymysql

cnx = pymysql.connect(host='localhost', port=3306, user='root', passwd='root', db='kite')

cursor = cnx.cursor()

query = ("select * from `kite`. `student`;")

cursor.execute(query)

print()

for row in cursor:
    print(row)

cursor.close()
cnx.close()