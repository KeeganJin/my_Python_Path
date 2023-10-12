import pymysql

while True:
    usr = input("username:")
    if usr.upper() == 'Q':
        break
    pwd = input("password:")
    mobile = input("mobile:")


    # 1. connect to MySQL
    conn = pymysql.connect(host="127.0.0.1",port=3306,user='root',
                           password='mysql',charset='utf8',
                           db='unicom')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)


    # 2. send instruction
    # cursor.execute("insert into admin(username,password,mobile)"+
    #                "values('liu','hi','jun')")
    insert_sql = "insert into admin(username,password,mobile)"+\
                 "values(%s,%s,%s)"
    cursor.execute(insert_sql,[usr,pwd,mobile])
    conn.commit();



    # 3.close connection
    cursor.close()
    conn.close()

