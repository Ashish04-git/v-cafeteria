from flask import Flask, render_template, url_for,request,redirect
from flaskext.mysql import MySQL
from sqlalchemy import create_engine
app = Flask(__name__)

mysql=MySQL()
app.config["MYSQL_DATABASE_USER"]='root'
app.config["MYSQL_DATABASE_PASSWORD"]=''
app.config["MYSQL_DATABASE_DB"]='my_project'
app.config["MYSQL_DATABASE_HOST"]='localhost'
app.config["MYSQL_DATABASE_PORT"]= 3306
mysql.init_app(app)
# create_engine('mysql://root:tiger@localhost/my_project')


@app.route("/home", methods=['POST'])
def login():
    if request.method=='POST':
        username=request.json["username"]
        password=request.json["password"]
        con=mysql.connect()
        cur=con.cursor()
        cur.execute("Select * from login where username=%s and password=%s", (username, password))
        record = cur.fetchone()
        con.close()
        if record is None:
            return {"msg": f"Username {username} does not exist in db"}
        return {"msg": f"Username {record[0]} exist in db"}
    

if __name__=='__main__':
    app.run(host="0.0.0.0", port="5000", debug=True)

# to run publicly
# python App.py