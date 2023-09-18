from pymongo import MongoClient

try:
  conn = MongoClient("mongodb://localhost:27017")
  print("Connected to MongoDB Successfully...")
except:
  print("Connection failed")

db_name = input("Enter database name: ")

db = conn[db_name]

coll_name = input("Enter collection name: ")

collection = db[coll_name]

while True:
  print("1. Insert\n2. Update\n3. Delete\n4. Display\n5. Exit")
  
  ch = int(input("Enter your choice: "))
  
  if ch == 1:
    name = input("Enter the name: ")
    age = input("Enter age: ")
    phone = input("Enter contact number: ")
    address = input("Enter address: ")
    
    record = {'name': name, 'age': age, 'phone': phone, 'address': address}
    
    query = collection.insert_one(record)
    print("Inserted Successfully")
    
  elif ch == 2:
    key = input("Enter the key: ")
    value = input("Enter the value: ")
    update_query = {key: value}
    new_key = input("Enter the key to be updated: ")
    new_value = input("Enter the value to be updated: ")
    new_field = {"$set" : {new_key : new_value}}
    update_result = collection.update_one(update_query, new_field)
    print("Updated Successfully")
  
  elif ch == 3:
    key = input("Enter the key: ")
    value = input("Enter the value: ")
    delete_query = {key: value}
    delete_result = collection.delete_one(delete_query)
    print("Record Deleted Successfully")
    
  elif ch == 4:
    data = collection.find()
    for i in data:
      print(i)
  
  elif ch == 5:
    print("Exiting....")
    exit()
    
  else:
    print("Invalid choice")