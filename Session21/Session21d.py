from Session21c import MongoDBHelper
from Session21a import User
from bson.objectid import ObjectId # import ObjectId, if you wish to fetch doc based on HashCode
import datetime
from tabulate import tabulate

def main():

    print("Welcome to MongoDB Test App")
    dbHelper = MongoDBHelper()

    """    
    user = User()
    user.add_user_details()
    document = vars(user)

    dbHelper.insert(document)
    """
    # To delete 
    #query = {"email": "john@example.com"}
    #dbHelper.delete(query)

    #Fetch on the basis of Unique ID -> ObjectId
    query = {"_id": ObjectId("669b94f6175bcff7f64d39ea")}
    users = dbHelper.fetch(query)
    print(users)

    # To Fetch All
    """
    users = dbHelper.fetch()
    for user in users:
        print(user)
    """

    #To Update
    #query = {"email": "ben@example.com"}
    #document_to_update = {"name": "Ben Tan", "age": 32, "creatd_on":datetime.datetime.now()}

    #dbHelper.update(document = document_to_update, query= query)

    print(tabulate(users, tablefmt='grid'))    

if __name__ == "__main__":
    main()