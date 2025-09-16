
import json #import json → Lets you use Python’s JSON tools to read/write data.

def load_data ():
    try:
        with open ('youtube.txt','r') as file :
         test =  json.load(file) #json.load(file) → Reads JSON from a file and turns it into Python data
         print(type (test))
         return test
    except FileNotFoundError:        
        return[]
    
def save_data_helper(videos):
    with open('youtube.txt','w') as file :
        json.dump(videos,file) #json.dump(data, file) → Saves Python data to a file in JSON format.
        
        
def list_all_videos(videos):
  print("\n")
  print("*"* 70)
  for index ,video in  enumerate(videos, start=1): #enumerate() in Python → A built-in function that lets you loop through items and get their index at the same time.(use for indexing or numbering )
     print(f"{index}.{video['name']},Duration : {video['time']}")
     print("\n")
     print("*"* 70)

def add_video (videos):
   name = input("Enter video name : ")
   time = input("Enter video time : ")
   videos.append({'name': name,'time': time })
   save_data_helper(videos)

def update_video(videos):
    list_all_videos(videos)
    index = int (input("Enter the video number to update "))
    if 1 <= index <= len(videos):
       name= input ("Enter the new video name ")
       time = input ("Enter the new video time ")
       videos[index -1]= {'name':name ,'time': time}
       save_data_helper(videos)
    else :
        print("Invalid index selected ")

def delete_video(videos):
    list_all_videos(videos)
    index= int (input("Enter the video number to be deleted "))
    if 1<= index <= len(videos):
        del videos[index -1]
        save_data_helper(videos)  #it saves the current list of videos to a file (youtube.txt) in JSON format so the data isn’t lost when the program closes.
    else:
        print("Invalid video index selected ")

def main (): #We use def main(): to organize the main logic of a program in one place. It makes the code cleaner, reusable, and easier to read
     videos =load_data()
     while True :
        print("\n Youtube manager | choose an option") 
        print("1. List all youtube videos")
        print("2. Add a youtube video")
        print("3. Update  a youtube video details ")
        print("4. delete a youtube video  ")
        print("5. Exit the app ")
        choice= input("Enter your choice :")
        print(videos)

        match choice : # its use in Python is used for pattern matching to compare a value (choice) against multiple patterns using case statements, similar to a switch statement. Introduced in Python 3.10.
            case '1':  
                list_all_videos(videos)
            case '2':
                add_video(videos)
            case '3':
                update_video(videos)
            case '4':
                delete_video(videos)
            case '5':
                break 
            case _: #case _: is the default case in Python's `match` statement; it runs when no other case matches.like if case have no 6 or more than six then its followed 
                print("invalid Choice")

if __name__ == "__main__": #__name__ is called a "dunder" name("Dunder" = Double UNDerscore)its run directly file which is present in codes not imported file 
    main()
   

            

        


         


