import psycopg2 #导入psycopg2包
import psycopg2.extras
import json

# 连接到给定的数据库
conn = psycopg2.connect(database="magicbox", user="libaokun", password="magicbox",
                        host="127.0.0.1", port="5432")

# 建立游标，用来执行数据库操作
cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
cursor0 = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)


# 执行SQL命令
cursor.execute("DROP TABLE test_conn")
cursor.execute("CREATE TABLE test_conn(id int, name text)")
cursor.execute("INSERT INTO test_conn values(1,'haha')")


# 提交SQL命令
conn.commit()


# 执行sql select命令
cursor.execute("select * from magicbox")
cursor0.execute("select * from information_schema.columns where table_schema='public' and table_name='magicbox'")
# 获取SELECT返回的元组
rows = cursor.fetchall()
column = cursor0.fetchall()

L = []
for col in column:
    print(col['column_name'])
    L.append(col['column_name'])
print(L)


for row in rows:
    print(L[0],':',row['id'],'\t',L[1],':',row['passwo'],'\t',L[2],':',row['isadmin'])
print('\n')

print(rows)

# 写入本地json
with open("./test.json",'w',encoding='utf-8') as json_file:
    json.dump(rows,json_file,ensure_ascii=False)


# 关闭游标
cursor.close()

# 关闭数据库
conn.close()


