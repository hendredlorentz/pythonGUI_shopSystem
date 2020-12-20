import pymysql as pymysql
import logging


def addInfo(name , price , intro):
    conn = pymysql.Connect("localhost", "root", "cuiwenxuan", "shopsystem", charset="utf8")
    cur = conn.cursor();

    sql = "insert into iteminfo(itemId,itemName,itemPrice,itemIntro) values (0,'%s','%s','%s')" %(name,price,intro)
    # print("这就是拿到了数据库内容",sql)
    print(sql)
    information = cur.execute(sql)

    # for i in range( information):
    #     # row = cur.fetchone()
    #     # yield row[0]
    #     print(i,str(cur.fetchone()))
    #     # list.append(cur.fetchone())
    # # print(row)
    # print(list)
    print("操作的数据为：",information)
    conn.commit()
    if(information):
        return True
    else:
        return False

# getInfo()
