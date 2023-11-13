"""
cursor読み方：カーソル
    1.execute(query, params=None)
        （execute読み方：エクスキュート）
        ・　执行SQL查询或命令。
        ・　query是SQL查询或命令的字符串。
        ・　params是一个可选的参数，用于将参数传递给查询。
        ex:
            cursor.execute(
                "SELECT * FROM your_table WHERE column = %s",
                 (some_value,)
            )

    2.executemany(query, seq_of_params)
        ・　批量执行相同的SQL查询，但每次使用不同的参数。
        ・　query是SQL查询的字符串。
        ・　seq_of_params是一个包含参数元组的序列。
        ex:
            data_to_insert = [(1, 'John'), (2, 'Jane'), (3, 'Bob')]
            cursor.executemany(
                "INSERT INTO your_table (id, name) VALUES (%s, %s)",
                data_to_insert
            )

    3.fetchone()
        ・　从查询结果中获取一行数据作为元组。
        ・　如果没有更多的行可用，返回None。
        ex:
            row = cursor.fetchone()

    4.fetchall()
        ・从查询结果中获取所有行数据，返回一个元组列表。
        ex:
            rows = cursor.fetchall()

    5.fetchmany(size=None)
        ・　从查询结果中获取指定数量的行数据，返回一个元组列表。
        ・　size是可选的，表示要获取的行数，默认为cursor.arraysize
        ・　当不指定size参数时，fetchmany获取的行数与fetchall相同，
            即它获取查询结果中的所有行。
        ex:
            rows = cursor.fetchmany()  # 等同于 fetchall

    6.fetchwarnings()
        ・　获取最后一次执行的查询的警告信息。
        ex:
            warnings = cursor.fetchwarnings()

    7.rowcount
        ・　返回最近一次执行的查询影响的行数。
        ex:
            count = cursor.rowcount

    8.description
        ・　返回查询结果的元数据，包括列名、类型等信息。

    9.close()
        ・　关闭游标
        ex:
            cursor.close()
"""
