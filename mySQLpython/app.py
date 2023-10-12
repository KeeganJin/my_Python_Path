from flask import Flask,render_template,request
import pymysql

app = Flask(__name__)

@app.route("/add/user", methods=['GET', 'POST'])
def add_user():
    if request.method == 'GET':
        return render_template("add_user.html")

    username = request.form.get('user')
    password = request.form.get('pwd')
    mobile = request.form.get('mobile')

    # 1.create connection
    conn = pymysql.connect(host="127.0.0.1",port=3306,user='root',
                           password='mysql',charset='utf8',
                           db='unicom')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

    # 2. execute SQL
    insert_sql = "insert into admin(username,password,mobile)"+\
                 "values(%s,%s,%s)"
    cursor.execute(insert_sql,[username,password,mobile])
    conn.commit()

    # 3.close
    cursor.close()
    conn.close()
    return("added successfully")

@app.route("/show/user")
def show_user():
    # 1.create connection
    conn = pymysql.connect(host="127.0.0.1",port=3306,user='root',
                           password='mysql',charset='utf8',
                           db='unicom')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

    sql = "select * from admin"
    cursor.execute(sql)
    data_list = cursor.fetchall()

    # 3.close
    cursor.close()
    conn.close()

    print(data_list)
    return render_template("show_user.html",data_list=data_list)

if __name__ == '__main__':
    app.run()