from django.db import connection


# sql自定义查询
def custom_query(sql):
    cur = connection.cursor()
    cur.execute(sql)
    return cur.fetchall()
