from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/show/info")
def index():
    return render_template("index.html")

@app.route("/register",methods=['GET','POST'])
def register():
    if request.method == 'GET':
        return render_template("register.html")
    else:
        usr = request.form.get("usr")
        pwd = request.form.get("pwd")
        print(usr, pwd)
        return "successful registration"

# //methods default to GET

@app.route("/temp")
def temp():
    return render_template("temp.html")

@app.route("/menu")
def menu():
    return render_template("menu.html")
@app.route("/table")
def table():
    return render_template("table.html")


if __name__ == "__main__":
    # host = "", port = ""
    app.run()