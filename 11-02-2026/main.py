from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["new_db"]
collection = db["new_collection"]

try:
    users_list = [
        {
            "name": "yash",
            "age": 21,
            "skills": ["Python", "MongoDB", "FastAPI"]
        },
        {
            "name": "harsh",
            "age": 22,
            "skills": ["Java", "SQL"]
        },
        {
            "name": "ajay",
            "age": 23,
            "skills": ["JavaScript", "React", "Node.js"]
        },
        {
              "name": "jay",
              "age": 25,
              "skills": ["c", "c++", "html"]
        }
    ]

    collection.insert_many(users_list)
    print(" Inserted users with name, ages and skills.")

    print("\nPython Developers:")
    for user in collection.find({"skills": "Python"}):
        print(f"- {user['name']} (Age: {user['age']})")

    collection.update_one(
        {"name": "yash"},
        {"$push": {"skills": "Docker"}, "$set": {"age": 22}}
    )

    collection.update_one(
         {"name": "yash"},
         {
              "$set": {
                   "age": 22,
                   "skills": ["asp","react","html"]
              }
         }
    )

    print("\n Updated yash age and added 'Docker' to skills.")

    result = collection.delete_many({"age": {"$gt": 22}})
    print(f"Deleted {result.deleted_count} document(s) where age > 22.")

finally:
    client.close()
    print("\n Connection closed.")




