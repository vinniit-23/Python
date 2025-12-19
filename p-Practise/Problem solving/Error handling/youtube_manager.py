import json

def load_data():
   try:
    with open("youtube.txt",'r') as file:
      return json.load(file)
   except FileNotFoundError:
      print("somenthing went wrong!, can't load the method")
      return []

def save_to_file(videos):
   with open("youtube.txt",'w') as file:
        json.dump(videos,file)


def list_all_videos(videos):
     for index,video in enumerate(videos, start=1):
        print(f"{index}.video name: {video['name']} , video url: {video['url']} , Duration: {video['time']}")


def add_videos(videos):
     name =input("Add name of the video : ")
     url = input("Add url of the video : ")
     time = input("Add time of the video : ")
     videos.append({'name':name,'url':url, 'time':time})
     save_to_file(videos)

def update_videos(videos):
   list_all_videos(videos)
   index = int(input("enter the video number which you want to update "))
   if 1<= index <= len(videos):
      name = input("Enter new name of video : ")
      url = input("Enter new url of the video : ")
      time = input("Enter newtime of the video : ")
      videos[index-1] = {'name':name , 'url':url , 'time':time}
      save_to_file(videos)
   else:
      print("somenthing went wrong on!, can't update the videos")

def delete_videos(videos):
   list_all_videos(videos)
   index = int(input("enter the video number which you want to update: "))
   if 1<= index <= len(videos):
      del videos[index-1]
      save_to_file(videos)
   else:
      print("somenthing went wrong on!, can't delete the video")     

def main():
   videos = load_data()
   while True:
     print('\n')
     print('*'*70)
     print("\n ***** Youtube Manager App | Choose an option *****")
     print("1. To view List of added videos ")
     print("2. To Add videos in List ")
     print("3. To update videos List")
     print("4. To Delete videos from the List ")
     print("5. To exit from the app")
     choice = input("Enter your choice : ")

     match choice :
        case '1':
           list_all_videos(videos)
        case '2':
           add_videos(videos)
        case '3':
           update_videos(videos)
        case '4':
           delete_videos(videos)
        case '5':
           break
        case _:
           print("Invalid choice/input")
         
   
         
   


if __name__  == "__main__":
       main()




"""In this program we used normal text file as data base in which we are saving our data with help 
of json in python.

   - the data which are saving is in form of list of dictionary which means we created a list in which
       we are storing data in in form as dictionary 

    - it looks like it 
       [{"name": "name", "url":"url", "time":"time" }]

    what does above structure means?

     ans :- the brackets [] symbolise list and braces {} symbolise dictionary
          dictionary work on key values basis means the first name is key and second name is value 
          which changes with real value when we run the program its is only for representitative purpose 
          we are using enumerator for changing index for user which will start form 1
          will we know that list index start with 0 tht's why we are using enumerator 
         

      Summary:
             we made text file in which we are storing data as json format for which we are using json 
             in pythonn.

        """