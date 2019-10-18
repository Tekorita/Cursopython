#Conexion a base de datos

import pymysql

conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='prueba')

cur = conn.cursor()
cur.execute("select * from persona")

print(cur.description)
print()

for row in cur:
	print(row)

cur.close()
conn.close()
