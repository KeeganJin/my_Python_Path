import pymysql



conn = pymysql.connect(host="127.0.0.1" ,port=3306 ,user='root',
                       password='mysql' ,charset='utf8',
                       db='unicom')
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)



cursor.execute("select * from admin")
data_list = cursor.fetchall()
# list of dict
print(data_list)

for row_dict in data_list:
    # dict
    print(row_dict)

cursor.close()
conn.close()