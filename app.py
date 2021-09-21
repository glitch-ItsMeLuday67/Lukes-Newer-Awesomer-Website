from flask import Flask, session, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

app.config["SECRET_KEY"] = "encrypted_data"

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template("index.html")

@app.route("/biggest_number")
def biggest_number():
    return render_template("biggest_number.html")

@app.route("/validate_biggest")
def validate_biggest():
    user = request.form.get("user")
    user1 = request.form.get("user1")
    user2 = request.form.get("user2")
    result = ""
    if user > user1 and user > user2:
        result =  str(user) + " is the biggest number"
    elif user2 > user and user2 > user1:
        result =  str(user2) + " is the biggest number"
    elif user1 > user and user1 > user2:
        result =  str(user1) + " is the biggest number"
    elif user == user1:
        if user2 == user1:
            result =  "All numbers are same"
        if user2 < user:
            result =  str(user) + " and " + str(user1) + " are bigger."
    elif user1 == user2:
        if user < user1:
            result =  str(user1) + " and " + str(user2) + " are bigger."
    elif user == user2:
        if user1 < user2:
            result =  str(user) + " and " + str(user2) + " are bigger."
    return render_template("biggest_number.html",result = result)

@app.route("/bmi",methods=["GET","POST"])
def bmi():
    if request.method == "GET":
        return render_template("bmi.html")
    weight = request.form.get("weight",type = float)
    height = request.form.get("height", type = float)
    age = request.form.get("age", type = float)
    gender = request.form.get("gender")
    resultBMI = ""
    resultFAT = ""
    resultH2O = ""
    resultHOW = ""
    totalResult = ""
    BMI = weight / (height/100) ** 2
    resultBMI = "Your BMI is %.2f"% BMI
    fat = (1.20 * BMI) + (0.23 * age) - 16.2
    resultFAT = "Fat percentage in your body is %.2f" % fat
    if gender == "f":
        TBW = -2.097 + 0.1069 * height + 0.2466 * weight
        resultH2O = "Your total body water is %.2f"% TBW
    if gender == "m":
        TBW1 =  2.447 - 0.09156 * age + 0.1074 * height + 0.3362 * weight
        resultH2O = "Your total body water is %.2f"% TBW1
    if BMI <= 18.4:
        resultHOW = "You are underweight."
    elif BMI <= 24.9:
        resultHOW = "You are healthy."
    elif BMI <= 29.9:
        resultHOW = "You are over weight."
    elif BMI <= 34.9:
        resultHOW = "You are severely over weight."
    elif BMI <= 39.9:
        resultHOW = "You are obese."
    else:
        resultHOW = "You are severely obese."
    totalResult = resultBMI + ". " + resultFAT + ". " + resultH2O + ". " + resultHOW
    return render_template("bmi.html", totalResult = totalResult)

@app.route('/leap_year', methods=['GET', 'POST'])
def leap_year():
    if request.method == "GET":
        return render_template("leap_year.html")
    year = request.form.get("year", type = int)
    result = ""
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                 result = str(year) + " is a leap year"
            else:
                result = str(year) + " is not a leap year"     
        else: 
            result = str(year) + " is a leap year"
    else:
        result = str(year) + " is not a leap year"

    return render_template("leap_year.html", result = result) 

@app.route('/encrypt', methods=['GET', 'POST'])
def encrypt():
    if request.method == "GET":
        return render_template("encrypt_decrypt.html")
    string = request.form.get("string")
    encrypt = ""
    for i in string:
        eye = ord(i) + 5
        eye1 = chr(eye)
        encrypt += eye1

    return render_template("encrypt_decrypt.html", encrypt = encrypt)

@app.route('/decrypt', methods=['GET', 'POST'])
def decrypt():
    if request.method == "GET":
        return render_template("encrypt_decrypt.html")
    string = request.form.get("string1")
    decrypt = ""
    for i in string:
        eye = ord(i) - 5
        eye1 = chr(eye)
        decrypt += eye1

    return render_template("encrypt_decrypt.html", decrypt = decrypt)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == "GET":
        return render_template("register.html")
    
    username = request.form.get("username")
    session["username"] = username
    password = request.form.get("password")
    session["password"] = password
    confirmpass = request.form.get("cpassword")
    email = request.form.get("email")
    session["email"] = email
    message = ""

    conn = sqlite3.connect('users.db')
    cur = conn.cursor()
    usernames = cur.execute("SELECT Username FROM registration_db").fetchall()
    print(usernames)
    users = []
    for i in usernames:
        users.append(i[0])
    print(users)
    if username in users:
        error = "Username already exists."
        return render_template("register.html", error = error)

    if confirmpass != password:
        message = "Password mismatch."
        return render_template("register.html", message = message)
    
    conn = sqlite3.connect('users.db')
    cur = conn.cursor()
    cur.execute('''INSERT INTO registration_db(
        Username, Password, Email) VALUES(?,?,?)''',(username, password, email))
    print("Values Inserted")
    records1 = cur.execute("SELECT * FROM registration_db;").fetchall()
    session["records"] = records1
    print(records1)
    conn.commit()
    conn.close()

    return render_template("login.html", records = records1)
        
@app.route('/login', methods=['GET', 'POST'])
def login():

    if request.method=="GET":
        return render_template("login.html")

    user_admin = "admin"
    pass_admin = "lukeanand123$"
    username = request.form.get("username")
    password = request.form.get("password")
    message_login = ""
    db_username = session.get("username", "Incorrect username or password")
    db_password = session.get("password", "Incorrect username or password")
    role = request.form.get("flexRadioDefault")

    if role == "admin":
        if username == user_admin:
            if password == pass_admin:
                message_login = "You have logged in as an admin"
                session["admin"] = True
                session["authenticated"] = True
                return render_template("index.html", message_login = message_login)
            message_login = "Username or password is incorrect."
            return render_template("login.html", message_login = message_login)
        message_login = "Username or password is incorrect."
        return render_template("login.html", message_login = message_login)
    
    if username == db_username:
        if password == db_password:
            message_login = "Successfully Logged In"
            session["authenticated"] = True
            return render_template("index.html", message_login = message_login)
        message_login = "Incorrect username or password"
        return render_template("login.html", message_login = message_login)
    message_login = "Incorrect username or password"
    return render_template("login.html", message_login = message_login)

@app.route('/users', methods=['GET', 'POST'])
def users():
    conn = sqlite3.connect("users.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM registration_db")
    records = cur.fetchall()
    print(records)
    conn.commit()
    conn.close()
    if session.get("admin"):
        return render_template("user_table.html", records = records)
    else:
        return "You don't have the permission to access this page."

@app.route('/logout', methods=['GET', 'POST'])
def logout():
    session.clear()
    message = "You have successfully logged out"
    return render_template("index.html", message_login = message)

@app.route('/test', methods=['GET', 'POST'])
def test():
    return render_template("test.html")

if __name__ == "__main__":
    app.run(debug = True)