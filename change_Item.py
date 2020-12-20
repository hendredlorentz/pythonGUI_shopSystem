import pymysql as pymysql
import logging


def changeInfo(Id,Name,Price,Intro):
    conn = pymysql.Connect("localhost", "root", "cuiwenxuan", "shopsystem", charset="utf8")
    cur = conn.cursor();
    NumberId = int(Id)
    sql = "update itemInfo set itemName='%s',itemPrice='%s',itemIntro='%s' where itemId = '%d'" % (Name,Price,Intro,NumberId)
    # print("这就是拿到了数据库内容",sql)
    print("这是更新的sql语句：",sql)
    information = cur.execute(sql)
    conn.commit()
    if(information):
        return True
    else:
        return False
