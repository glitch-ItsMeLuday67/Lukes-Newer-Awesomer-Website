from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html") 


@app.route("/city")
def city():
    return render_template("html.html")

@app.route("/even_odd")
def even_odd():
    return render_template("even_odd.html")

@app.route("/validate_even_odd")
def validate_even_odd():
    num = request.form.get("number")
    if num.isdigit():
        num = int(num)
        if num % 2 == 0:
            return render_template("even_odd.html", message = "It is even.")
        elif num % 2 != 0:
            return render_template("even_odd.html", message = "It is odd.")
    else:
        return render_template("even_odd.html", message = "It is not a number")

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


@app.route('/courier', methods=['GET', 'POST'])
def courier():
    if request.method == "GET":
        return render_template("courier_shop.html")
    returnsentence = ""
    parcelweight = request.form.get("parcelweight")
    if not parcelweight.isnumeric():
        return render_template("courier_shop.html",returnsentence = "Invalid Input")
    parcelweight = float(parcelweight)
    if parcelweight == 20:
        returnsentence = "You have to pay %.2f"%(parcelweight*10) + "$"
    elif parcelweight >= 10 and parcelweight < 20:
        returnsentence = "You have to pay %.2f"%(parcelweight*12) + "$"
    elif parcelweight >= 1 and parcelweight < 10:
        returnsentence = "You have to pay %.2f"%(parcelweight*14) + "$"
    elif parcelweight < 1:
        returnsentence = "You don't have to pay anything"
    else:
        returnsentence = "We don't deliver parcels more than 20kg"
    return render_template("courier_shop.html", returnsentence = returnsentence)

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
if __name__ == "__main__":
    app.run(debug=True)