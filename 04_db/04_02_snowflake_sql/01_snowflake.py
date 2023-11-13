"""
    1.首先，你需要安装Snowflake的Python连接器。可以使用pip安装：
        pip install snowflake-connector-python
"""

# 2.创建Snowflake连接：
# import snowflake.connector as sf
import snowflake.connector

# Snowflake账户信息
account = 'your_account'
warehouse = 'your_warehouse'
database = 'your_database'
schema = 'your_schema'
username = 'your_username'
password = 'your_password'

# 2.1创建Snowflake连接
conn = snowflake.connector.connect(
    user=username,
    password=password,
    account=account,
    warehouse=warehouse,
    database=database,
    schema=schema
)

# 2.2创建游标
cursor = conn.cursor()

# 3.传输数据
# 3.1示例数据
data_to_insert = [
    (1, 'John Doe', 'john@example.com'),
    (2, 'Jane Smith', 'jane@example.com'),
    # 添加更多数据行...
]

# 3.2执行插入语句
insert_query = "INSERT INTO your_table (column1, column2, column3) VALUES (%s, %s, %s)"
cursor.executemany(insert_query, data_to_insert)

# 3.3提交事务
conn.commit()

# 4.关闭游标和连接
cursor.close()
conn.close()
