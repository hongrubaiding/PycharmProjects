import pymysql
conn = pymysql.connect(host='localhost', user='root', passwd='zs7589090', db='quanshang')
# conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd=None, db='mysql')
cur = conn.cursor()
cur.execute("SELECT * FROM at_func")
r = cur.fetchall()
for r in cur:
   print(r)

cur.close()
conn.close()
