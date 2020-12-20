import pymysql as pymysql
import logging


def deleteInfo(Id):
    conn = pymysql.Connect("localhost", "root", "cuiwenxuan", "shopsystem", charset="utf8")
    cur = conn.cursor();
    NumberId = int(Id)
    sql = "delete from itemInfo where itemId = '%d'" % (NumberId)
    # print("这就是拿到了数据库内容",sql)
    print("这是删除的sql语句：",sql)
    information = cur.execute(sql)
    conn.commit()
    if(information):
        return True
    else:
        return False
