import sqlite3

con = sqlite3.connect("youtube_manager.db")
cur = con.cursor()

cur.execute("""
    CREATE TABLE IF NOT EXISTS videos(
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            url TEXT NOT NULL,
            time TEXT NOT NULL
            )
""")

# add a program which print empty file if database is empty
#add print statement for printing in formate




def list_videos():
     cur.execute("SELECT * FROM videos")
     for row in cur.fetchall():
         # for coloumn in cur.fetchone():
          print(row)
         # print(row,f"name{name}, url{url}, time {time}")

def add_videos(name,time,url):
     cur.execute("INSERT INTO videos (name, url , time ) VALUES (?,?,?)",(name,url,time))
     con.commit()
     print("Video added successful")


def update_videos(video_id, new_name, new_time,url):
     cur.execute("UPDATE videos SET name = ? ,time = ? , url=? WHERE id = ? ",(new_name,new_time,url,video_id)) 
     con.commit()
     print("Video updated successful")

def delete_videos(id):
     cur.execute("DELETE FROM videos WHERE id = ?",(id,))
     con.commit()
     print("Video deleted successful")


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
    con.close()    




if __name__ == "__main__":
      main() 