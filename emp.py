from flask import Flask,render_template,request,redirect,url_for,flash
from flask_mysqldb import MySQL

app = Flask(__name__)

app.secret_key = " flash message "

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'crud'

mysql = MySQL(app)



@app.route('/')
def Index():
    cur =mysql.connection.cursor()
    cur.execute("SELECT * FROM employee")
    data=cur.fetchall()
    return render_template('index.html',employees=data)


@app.route('/insert', methods = ['POST'])
def insert():
    if request.method=="POST":
        flash("Data insert Successful")
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO employee(name,email,phone) VALUES (%s ,%s,%s)",(name,email,phone))
        mysql.connection.commit()
        return redirect(url_for('Index'))



@app.route('/update',methods=['POST','GET'])
def update():

    if request.method == 'POST':
        id_data = request.form['id']
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        cur = mysql.connection.cursor()
        cur.execute("""
               UPDATE employee
               SET name=%s, email=%s, phone=%s
               WHERE id=%s
            """, (name, email, phone, id_data))
        flash("Data Updated Successfully")
        mysql.connection.commit()
        return redirect(url_for('Index'))




@app.route('/delete/<string:id_data>', methods = ['GET'])
def delete(id_data):
    flash("Record Has Been Deleted Successfully")
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM employee WHERE id=%s", (id_data,))
    mysql.connection.commit()
    return redirect(url_for('Index'))





if __name__ == "__main__":
    app.run(debug=True)




