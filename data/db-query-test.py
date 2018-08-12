import pymysql


cnx = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='kite')

insert_query = ("INSERT INTO  `kite`. `student` (`id`, `first name`, `last name`, `age`) VALUES ('7', 'john', 'coner', '34');")


cursor = cnx.cursor()
cursor.execute(insert_query)

cnx.commit()
cursor.close()
cnx.close()