"""
SQL综合案例，读取文件，写入MySQL数据库中
"""
from typing import List
from file_define import FileReader, TextFileReader, JsonFileReader
from data_define import Record
from pymysql import Connect

text_file_reader = TextFileReader("2011年1月销售数据.txt")
json_file_reader = JsonFileReader("2011年2月销售数据JSON.txt")

jan_data: List[Record] = text_file_reader.read_data()
feb_data: List[Record] = json_file_reader.read_data()
# 将两个月份的数据合并为一个list来存储
all_data: List[Record] = jan_data + feb_data

# 构建MySQL链接对象
conn = Connect(
    host="localhost",
    port=3306,
    user="root",
    password="123456",
    autocommit=True
)
# 获得游标对象
cursor = conn.cursor()
# 选择数据库
conn.select_db("py_sql")
# 组织SQL语句
for record in all_data:
    sql = f"insert into orders(order_date, order_id, money, province) " \
          f"values('{record.date}', '{record.order_id}', {record.money}, '{record.province}')"
    # 执行SQL语句
    cursor.execute(sql)
# 关闭MySQL链接对象
conn.close()
