
# 版本 psql (PostgreSQL) 10.5 ， pgadmin3  ，python 3.7

# python 连接，游标，及命令
# 连接到给定的数据库
conn = psycopg2.connect(database="table_name", user="user_name",  
             password="PASSWORD",host="127.0.0.1",port="5432")

# 建立游标，用来执行数据库操作
cursor = conn.cursor() #全部读取游标
cursor0=conn.cursor(cursor_factory=psycopg2.extras.DictCursor)#可按行读取游标

# 建立游标，用来执行数据库操作

#执行SQL命令
cursor.execute("DROP TABLE test_conn") //删除表
cursor.execute("CREATE TABLE test_conn(id int, name text)") //创建表
cursor.execute("INSERT INTO test_conn values(1,'haha')") //插入数据

#提交SQL命令
conn.commit()


#执行sql select命令
cursor.execute("select * from magicbox")
cursor0.execute("select * from information_schema.columns where table_schema='public' and table_name='magicbox'")

#获取SELECT返回的元组
rows = cursor.fetchall()
column= cursor0.fetchall()

for col in column:          #逐行取某列
    print(col['column_name'])


#查询表视图
SELECT   tablename   FROM   pg_tables  
WHERE   tablename   NOT   LIKE   'pg%'  
AND tablename NOT LIKE 'sql_%'
ORDER   BY   tablename;

#查询表结构
SELECT col_description(a.attrelid,a.attnum) as comment,pg_type.typname as typename,a.attname as name, a.attnotnull as notnull
FROM pg_class as c,pg_attribute as a inner join pg_type on pg_type.oid = a.atttypid
where c.relname = 'magicbox' and a.attrelid = c.oid and a.attnum>0

#查询表详细信息
select * from information_schema.columns
where table_schema='public' and table_name='magicbox'