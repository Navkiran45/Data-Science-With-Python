"""
Web Application Development with Flask
"""

from flask import *
import datetime
import hashlib
from database import MongoDBHelper

web_app = Flask("Doctor's App")
db_helper = MongoDBHelper()

@web_app.route("/") #Decorator
def index():
    # EITHER you can return plain text
    #message = "Welcome to Doctor's App. Its {}".format(datetime.datetime.now())
    
    # OR you can return HTML
    message = """
    <html>
    <head>
        <title> Doctor's App </title>
        <body>
        <center>
            <h3> Welcome to Doctor's App </h3>
        </center>
        </body>
    </head>
    </html>
    """
    #return message

    # render_template is used to return web pages (html pages)
    return render_template("index.html")
@web_app.route("/register")
def register():
    return render_template("register.html")

@web_app.route("/home")
def home():
    if session["email"] != "":
        return render_template("home.html", name = session['name'], email= session['email'])
    else:
        return redirect("/")

@web_app.route("/success")
def success():
    return render_template("success.html", name = session['name'], email= session['email'])

@web_app.route("/error")
def error():
    return render_template("error.html", name = session['name'], email= session['email'])

@web_app.route("/logout")
def logout():
    # Reset the Data
    session["email"] == ""
    session["name"] == ""
    return redirect("/")

@web_app.route("/add-user", methods= ["POST"])
def add_user_in_db():
    # Create Dictionary with data from HTML form
    user_data = {
        "name": request.form["name"],
        "email": request.form["email"],
        "password": hashlib.sha256(request.form["password"].encode('utf-8')).hexdigest(),
        "created_on": datetime.datetime.now()
    }
    db_helper.collection = db_helper.db["users"]
    # To save Data in MongoDB
    result = db_helper.insert(user_data)
    #message = "User Id is {}".format(result.inserted_id)
    #return message

    # Write the data in the Session Object
    # This data can be used anywhere in the project
    session['user_id'] = str(result.inserted_id)
    session['name'] = user_data["name"]
    session['email'] = user_data["email"]

    return render_template("home.html", email= session['email'])

@web_app.route("/fetch-user", methods= ["POST"])
def fetch_user_from_db():
   
    
    # Create Dictionary with data from HTML form
    user_data = {
        "email": request.form["email"],
        "password": hashlib.sha256(request.form["password"].encode('utf-8')).hexdigest()
    }
    db_helper.collection = db_helper.db["users"]
    # To fetch Data from MongoDB
    result = db_helper.fetch(query = user_data)

    print("Result is: ",result)

    if len(result)>0:
        user_data = result[0]
        session['name'] = user_data["name"]
        session['email'] = user_data["email"]

        return render_template("home.html", name= session['name'], email=session['email'])
    else:
        return render_template("error.html", message ="User Not Found. Please Try Again", name= session['name'], email=session['email'])
   
@web_app.route("/add-patient", methods= ["POST"])
def add_patient_in_db():
    # Create Dictionary with data from HTML form
    patient_data = {
        "name": request.form["name"],
        "email": request.form["email"],
        "phone": request.form["phone"],
        "gender": request.form["gender"],
        "age": int(request.form["age"]),
        "address": request.form["address"],
        "doctor_email": session["email"],
        "doctor_name": session["name"],
        "created_on": datetime.datetime.now()
    }
    
    db_helper.collection = db_helper.db["patients"]
    # To save Patient Data in MongoDB
    result = db_helper.insert(patient_data)
   
    return render_template("success.html", message = "Patient added Successfully." , name= session['name'], email=session['email'] )

@web_app.route("/fetch-patients")
def fetch_patients_from_db():
      
    if len(session["email"]) == 0:
        return redirect("/")
    
    # Create Dictionary with data from HTML form
    user_data = {
        "doctor_email": session["email"]
    }
    db_helper.collection = db_helper.db["patients"]
    
    # To fetch Data from MongoDB
    result = db_helper.fetch(query = user_data)
    # result here is list of document(dictionaries) fetched from MongoDB

    if len(result)>0:
        print(result)
        return render_template("patients.html", patients= result, name=session["name"], email=["email"])
    else:
        return render_template("error.html", message ="Patients Not Found" , name= session['name'], email=session['email'])

def main():
    # To use Session Tracking, create a secret key
    web_app.secret_key = "doctors-key-v1"
    # App will run Infinitely, until user quits
    web_app.run()
    #web_app.run(port = 5001) #optionally you can give port number

if __name__ == "__main__":
    main()