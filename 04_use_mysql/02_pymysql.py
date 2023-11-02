import pymysql

# 连接 MySQL
conn = pymysql.connect(
    host="localhost",
    port=3306,
    user="root",
    password="root",
    database="db_test",
    autocommit=True
)

print(conn.get_server_info())

# 获取游标对象
cursor = conn.cursor()

# 创建数据
data = ("插班生1", 99, 9999)

# 执行参数化查询
cursor.execute("INSERT INTO test (name, age, money) VALUES (%s, %s, %s)", data)

# 执行修改 MySQL 数据时需要通过 commit 确认,或者在Connection中设置autocommit=True
# conn.commit()

conn.close()
