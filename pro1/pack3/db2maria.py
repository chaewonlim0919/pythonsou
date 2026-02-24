# 원격 데이터베이스 연동 프로그래밍
# MariaDB: driver file 설치 후 사용
# pip install mysqlclient
import MySQLdb

conn = MySQLdb.connect(
    host='127.0.0.1',
    user='root',
    password='123',
    database='test',
    port=3306)
print(conn)
conn.close()
