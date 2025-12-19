import pymongo
from bson import ObjectId
try:
    client = pymongo.MongoClient("mongodb+srv://youtubepy:youtubepy@cluster0.hbqlyiw.mongodb.net/")
    client.server_info()  # Will force a connection attempt
    print("Connection successful!")
except Exception as e:
    print("Connection failed:", e)

db = client["ytmanager"]

video_collection = db["videos"]

print(video_collection)

def list_videos():
     for video in video_collection.find():
          print(f"ID: {video['_id']}, Name: {video['name']} and Time: {video['time']} and URL: {video['url']}")

def add_videos(name,time,url):
      video_collection.insert_one({"name": name , "time":time, "url":url})
      print("Video added successfully")

def update_videos(video_id,name ,time):
     video_collection.update_one( 
          {'_id': ObjectId(video_id)},
          {"$set":{"name":name, "time":time,}})
     print("Video updated successfully")
     

def delete_videos(video_id):
     video_collection.delete_one({'_id':ObjectId(video_id)}) 
     print("video deleted successfully")   


def main():
    while True:
         print("\n")
         print('*'*70)
         print('\n Youtube Manager App | Select an option')
         print("1. TO VIEW LISTED VIDEOS")
         print("2. TO ADD VIDEOS")
         print("3. TO UPDATE LISTED VIDEOS")
         print("4. TO DELETE VIDEOS FROM THE LIST")
         print("5. TO EXIT FROM THE PROGRAM")
         choice = input("Choose Given Option: ")
        
         if choice == '1':
              list_videos()
         elif choice == '2':
              name = input("Enter video name: ")
              url = input("Enter video url link: ")
              time = input("Enter video time: ")
              add_videos(name,time,url)
         elif choice == '3':
              list_videos()
              video_id = input("Enter video id: ")
              name = input("Enter video new name to update: ")
              url = input("Enter video new url to update: ")
              time = input("Enter video new time to update: ")
              update_videos(video_id,name,time)
         elif choice == '4':
              list_videos()
              video_id = input("Enter video id: ")
              delete_videos(video_id)
         elif choice == '5':
              break
         else :
              print("Invalid Input!")

if __name__ == "__main__":
    main()