"""
Web Application Development with Flask
SAS Model
"""

from flask import *
import datetime
import hashlib
from database import MongoDBHelper
from bson.objectid import ObjectId

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

@web_app.route("/update-patient/<id>")
def update_patient(id):
    print("Patient to be updated: ", id)

    # Save Patient ID in Session, which needs to be updated
    session["id"] = id
    
    # Fetch Document from patient collection, where ID Matches
    query = {"_id": ObjectId(id)}
    db_helper.collection = db_helper.db["patients"]

    #result is a list
    result = db_helper.fetch(query=query)

    # As we will get list of documents, 0th index will be our document
    # with patient id matching we have passed
    patient_doc = result[0]
    return render_template("update.html", name= session['name'], email=session['email'], patient = patient_doc )

@web_app.route("/update-patient-in-db", methods= ["POST"])
def update_patient_in_db():
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
    query = {"_id": ObjectId(session["id"])}
    # To save Patient Data in MongoDB
    result = db_helper.update(patient_data, query)
   
    return render_template("success.html", message = "Patient Updated Successfully." , name= session['name'], email=session['email'] )

@web_app.route("/delete-patient/<id>")
def delete_patient(id):
    print("Patient to be deleted: ", id)
    query = {"_id": ObjectId(id)}
    db_helper.collection = db_helper.db["patients"]
    db_helper.delete(query)
    return render_template("success.html", message = "Patient Deleted Successfully." , name= session['name'], email=session['email'] )

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

@web_app.route("/add-consultation/<id>")
def add_consultation(id):
    
    query = {"_id": ObjectId(id)}
    db_helper.collection = db_helper.db["patients"]

    #result is a list
    result = db_helper.fetch(query=query)

    # As we will get list of documents, 0th index will be our document
    # with patient id matching we have passed
    patient_doc = result[0]
    session["patient_name"] = patient_doc["name"]
    # Store the Patient Id in Session temporarily
    session["patient_id"] = id
    return render_template("add-consultation.html", name= session['name'], email = session['email'], patient_name=session["patient_name"])

@web_app.route("/add-consultation-in-db", methods= ["POST"])
def add_consultation_in_db():

    # Create Dictionary with data from HTML form
    consultation_data = {
        "complaints": request.form["complaints"],
        "bp": request.form["bp"],
        "temperature": request.form["temperature"],
        "sugar": request.form["sugar"],
        "medicines": request.form["medicines"],
        "remarks": request.form["remarks"],
        "follow_up": request.form["follow_up"],
        "doctor_email": session["email"],
        "doctor_name": session["name"],
        "patient_id" : session["patient_id"],
        "patient_name" : session["patient_name"],
        "created_on": datetime.datetime.now()
    }
    
    db_helper.collection = db_helper.db["consultations"]
    # To save Consultation Data in MongoDB
    result = db_helper.insert(consultation_data)
   
    return render_template("success.html", message = "Consultation added Successfully." , name= session['name'], email=session['email']  )

@web_app.route("/fetch-consultations")
def fetch_consultations_from_db():
      
    if len(session["email"]) == 0:
        return redirect("/")
    
    # Create Dictionary with data from HTML form
    user_data = {
        "doctor_email": session["email"]
    }
    db_helper.collection = db_helper.db["consultations"]
    
    # To fetch Data from MongoDB
    result = db_helper.fetch(query = user_data)
    # result here is list of document(dictionaries) fetched from MongoDB

    if len(result)>0:
        print(result)
        return render_template("consultations.html", consultations= result, name=session["name"], email=session["email"])
    else:
        return render_template("error.html", message ="Consultations Not Found" , name= session['name'], email=session['email'])

@web_app.route("/fetch-consultations-of-patient/<id>")
def fetch_consultations_of_patient_from_db(id):
      
    if len(session["email"]) == 0:
        return redirect("/")
    
    # Create Dictionary with data from HTML form
    user_data = {
        "doctor_email": session["email"],
        "patient_id": id
    }
    db_helper.collection = db_helper.db["consultations"]
    
    # To fetch Data from MongoDB
    result = db_helper.fetch(query = user_data)
    # result here is list of document(dictionaries) fetched from MongoDB

    if len(result)>0:
        print(result)
        return render_template("consultations.html", consultations= result, name=session["name"], email=session["email"])
    else:
        return render_template("error.html", message ="Consultations Not Found" , name= session['name'], email=session['email'])

@web_app.route("/delete-consultation/<id>")
def delete_consultation(id):
    print("Consultation to be deleted: ", id)
    query = {"patient_id": id}
    db_helper.collection = db_helper.db["consultations"]
    db_helper.delete(query)
    return render_template("success.html", message = "Consultation Deleted Successfully." , name= session['name'], email=session['email'] )

@web_app.route("/update-consultation/<c_id>")
def update_consultation(c_id):
    print("Consultation to be updated: ", c_id)
    
    # Fetch Document from patient collection, where ID Matches
    query = {"consultation_id" : c_id}
    db_helper.collection = db_helper.db["consultations"]

    #result is a list
    result = db_helper.fetch(query=query)

    # As we will get list of documents, 0th index will be our document
    # with patient id matching we have passed
    patient_doc = result[0]
    session["consultationt_id"] = c_id
    return render_template("update.html", name= session['name'], email=session['email'], patient = patient_doc )

@web_app.route("/update-consultation-in-db", methods= ["POST"])
def update_consultation_in_db():
    # Create Dictionary with data from HTML form
    consultation_data = {
        "complaints": request.form["complaints"],
        "bp": request.form["bp"],
        "temperature": request.form["temperature"],
        "sugar": request.form["sugar"],
        "medicines": request.form["medicines"],
        "remarks": request.form["remarks"],
        "followup": request.form["followup"],
        "patient_name": request.form["patient_name"],
        "created_on": datetime.datetime.now()
    }
    
    db_helper.collection = db_helper.db["patients"]
    query = {session["consultation_id"] : c_id}
    # To save Patient Data in MongoDB
    result = db_helper.update(consultation_data, query)
   
    return render_template("success.html", message = "Consultation Updated Successfully." , name= session['name'], email=session['email'] )

@web_app.route("/search-patient")
def search_patient():
    return render_template("search.html", name=session["name"], email= session["email"])

@web_app.route("/search-patient-from-db", methods= ["POST"])
def search_patient_from_db():
    patient_data = {
        "email" : request.form["email"],
        "doctor_email" : session["email"]
    }

    db_helper.collection = db_helper.db["patients"]
    
    # To fetch Data from MongoDB
    result = db_helper.fetch(query = patient_data)
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