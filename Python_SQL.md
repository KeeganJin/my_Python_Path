# MySQL + Python

## 1.1 Python manipulate MySQL

### **1.1.2 pymysql**

similar to JDBC

```python
import pymysql


# 1. connect to MySQL
conn = pymysql.connect(host="127.0.0.1",port=3306,user='root',
                       password='pwd',charset='utf8',
                       db='unicom')
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)


# 2. send instruction
cursor.execute("insert into admin(username,password,mobile)"+
               "values('liu','hi','jun')")

conn.commit();

# 3.close connection
cursor.close()
conn.close()
```

* 占位符



## 1.2 Flask + MySQL

app.py通过request.form.get(name)获得前端内容



**Details check project "mySQLpython"**