import pymysql as pymysql
import logging


def getSearchInfo(Id):
    conn = pymysql.Connect("localhost", "root", "cuiwenxuan", "shopsystem", charset="utf8")
    cur = conn.cursor();
    NumberId = int(Id)
    sql = "select * from itemInfo where itemId = '%d'" % NumberId
    # print("这就是拿到了数据库内容",sql)
    information = cur.execute(sql)

    # for i in range( information):
    #     # row = cur.fetchone()
    #     # yield row[0]
    #     print(i,str(cur.fetchone()))
    #     # list.append(cur.fetchone())
    # # print(row)
    # print(list)
    return list(cur.fetchall())

# getInfo()
