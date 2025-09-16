from pymongo import MongoClient #MongoClient → connects Python with MongoDB.
from bson import ObjectId #ObjectId → used to reference documents by their unique MongoDB _id.

client = MongoClient("mongodb+srv://tabish:yhFcdaE16pf83JxU@cluster0.elmpmti.mongodb.net/",tlsAllowInvalidCertificates=True)

#Not a good idea to include id and password in code files for privacy we use ENV

db = client["ytmanager"]
video_collection = db ["videos"]


print(video_collection)

def add_video(name,time):
    video_collection.insert_one({"name": name,"time": time})

def list_videos():
    for video in video_collection.find():
        print(f"ID : {video['_id']},Name : {video['name']} and Time : {video['time']}")

def update_video(video_id,new_name,new_time):
    video_collection.update_one({'_id':ObjectId(video_id)},{"$set":{"name" : new_name, "time": new_time}}) #Uses ObjectId(video_id) to find the correct video
       

def delete_video(video_id):
    video_collection.delete_one({"_id": ObjectId (video_id)})



def main ():
    while True:   #Keeps running until user exits.
        print("\n youtube manager App")
        print("1. list all videos")
        print("2.Add a new videos")
        print("3.update a videos")
        print("4.delete a videos")
        print("5.exit the app")
        choice = input("Enter your choice")

        if choice == "1":
            list_videos()
        elif choice == "2":
            name= input("Enter the video name : ")
            time =input("Enter the video time :")
            add_video(name,time)
        elif choice =="3": 
            video_id = input("Enter the video id to update :")
            name= input("Enter the updated video name :")
            time = input("Enter the updated video time :")
            update_video(video_id,name,time)

        elif choice=="4":
            video_id = input("Enter the video id to delete .")
            delete_video(video_id)
        
        elif choice =="5":
            break 
        else :
            print("Invalid choice")



if __name__=="__main__":
    main()

"""
MongoDB is a NoSQL database (Not Only SQL) that stores data in a flexible, document-oriented format (JSON-like documents).

Instead of storing data in tables & rows (like SQL databases), MongoDB stores data in collections & documents.

Each document is like a JSON object:

{
  "_id": "64b7f23a9e",
  "name": "My Video",
  "time": "10 min"



🔹 Why we use MongoDB?

Flexibility – No need for fixed schema (you can add new fields anytime).

Scalability – Handles large amounts of unstructured data (big data, social media apps, etc.).

JSON-like storage – Easy to use with modern web apps (since frontend also works with JSON).

Fast Development – Good for projects where requirements keep changing.
}"""