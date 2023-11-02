from pymysql import Connection

# 连接mysql
conn = Connection(
    host="localhost",
    port=3306,
    user="root",
    password="root"
)

print(conn.get_server_info())

# 获取游标对象
cursor = conn.cursor()
# 使用数据库 use XXX
conn.select_db("db_test")

# 执行sql
cursor.execute(
    "SELECT * FROM test"
)

# 获取结果,得到的是一个元组tuple
results: tuple = cursor.fetchall()
print(results)
# ((1001, '桃太郎', 18, None), (1002, '阿呆', 20, None), (1003, '阿呆', 19, None), (1004, '小明', None, None))
for r in results:
    print(r)

conn.close()
