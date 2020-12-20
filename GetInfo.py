import pymysql as pymysql
import logging


def getInfo():
    conn = pymysql.Connect("localhost", "root", "cuiwenxuan", "shopsystem", charset="utf8")
    cur = conn.cursor();
    sql = "select * from itemInfo"
    # print("这就是拿到了数据库内容",sql)
    information = cur.execute(sql)
    print("数据分别为(编号，名称，价格，品牌):")


    # for i in range( information):
    #     # row = cur.fetchone()
    #     # yield row[0]
    #     print(i,str(cur.fetchone()))
    #     # list.append(cur.fetchone())
    # # print(row)
    # print(list)
    return list(cur.fetchall())

# getInfo()
print(getInfo())