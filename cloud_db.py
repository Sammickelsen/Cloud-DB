import firebase_admin
from firebase_admin import credentials, firestore
from google.cloud.firestore_v1.base_query import FieldFilter, Or
import os

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {"databaseURL" : "https://cloud-db-5f51f-default-rtdb.firebaseio.com/"})

db = firestore.client()
ref = db.collection("userInfo").document()

def save_user_info():
    entry_name = input("First Name: ")
    entry_l_name = input("Last Name: ")
    entry_email = input("Email: ")
    
    # Add logic to save user information here
    user_data = {
        "f_name" : entry_name,
        "l_name" : entry_l_name,
        "email" : entry_email
    }
    ref.set(user_data)

def search_by_name(collection_name, name):
    try:
        doc_ref = db.collection(collection_name)
        query = doc_ref.where(filter=FieldFilter("f_name", "==", name))
        docs = query.stream()

        for doc in docs:
            data = doc.to_dict()
            print(f"Name: {data["l_name"]}, {data["f_name"]}")
            print(f"Email: {data["email"]}")
            print()
    except Exception as err:
        print(f"Error retrieving documents: {str(err)}")

def get_docs(collectionName):

    docs = (
        db.collection(collectionName)
        .stream()
    )
    document_list = []
    for doc in docs:
        doc_data = doc.to_dict()
        doc_data["id"] = doc.id
        doc_data['data'] = doc._data
        document_list.append(doc_data)
    
    return document_list

def update_email(doc_list, ref):
    print("Please choose which user to update: \n")
    i = 1
    for doc in doc_list:
        print(f"{i}. {doc["l_name"]}, {doc["f_name"]}")
        i += 1
    choice = int(input("> "))

    chosen_doc = doc_list[choice - 1]
    chosen_id = chosen_doc['id']
    collection_ref = db.collection(ref)
    doc_ref = collection_ref.document(chosen_id)
    new_email = input("Please type your new email: ")
    doc_ref.update({
            'email': new_email
    })

def show_all(doc_list):
    for doc in doc_list:
        print(f"{doc["l_name"]} | {doc["f_name"]} | {doc["email"]}")

def delete_user(doc_list, ref):
    print("Please choose which user to delete: \n")
    i = 1
    for doc in doc_list:
        print(f"{i}. {doc["l_name"]}, {doc["f_name"]}")
        i += 1
    choice = int(input("> "))
    chosen_doc = doc_list[choice - 1]
    chosen_id = chosen_doc['id']

    doc_ref = db.collection(ref).document(chosen_id)
    print(f"Are you sure you would like to delete {chosen_doc["f_name"]} {chosen_doc["l_name"]}'s account? (y/n)")
    passkey = input("> ")

    if passkey.lower() == "y":
        doc_ref.delete()
        print("User successfully deleted.")
    elif passkey.lower() == "n":
        print("User will not be deleted.")
    else:
        print("Invalid answer. User will not be deleted.")

def clear():
    print()
    input("Press any key to continue ")
    os.system("cls")




sentinal = True

while sentinal == True:
    
    print("""
Welcome to your test Database.  Please choose an option below:

1. Create new User
2. Search by Name
3. Delete User
4. Update Email
5. Show all Users
6. Exit
""")

    choice = input("> ")
    os.system('cls')

    if choice == "1":
        # Write Function
        save_user_info()
        clear()

    elif choice == "2":
        # Read Function
        print("Please type a name to search for.")
        name = input("> ")
        search_by_name("userInfo", name)
        clear()

    elif choice == "3":
        # Delete Function
        doc_list = get_docs("userInfo")
        delete_user(doc_list, "userInfo")
        clear()

    elif choice == "4":
        doc_list = get_docs("userInfo")
        # Update Function
        update_email(doc_list, "userInfo")
        clear()

    elif choice == "5":
        doc_list = get_docs("userInfo")
        show_all(doc_list)
        clear()

    elif choice == "6":
        sentinal = False

    else:
        print("Please input a valid option.")


