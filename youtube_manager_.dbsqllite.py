import sqlite3

conn = sqlite3.connect('youtube_videos.db')

cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS videos") #If the table is already there → delete it first.(If it doesn’t exist yet → do nothing (so no error).)

conn.commit()
 
cursor.execute(''' 
CREATE TABLE IF NOT EXISTS videos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,        
    name TEXT NOT NULL,
    time TEXT NOT NULL 
)
''')
conn.commit()  
# ✅ Saves the changes permanently in the database  
# Without this → data is not stored


#Triple quotes They preserve formatting (spaces, newlines, indentation) exactly as written
def list_videos():
    cursor.execute("SELECT * FROM videos") 
# ✅ Reads (fetches) all rows from the table

    for row in cursor.fetchall():
         print(row)
def add_video(name, time):
    cursor.execute("INSERT INTO videos (name,time)VALUES(?,?)",(name,time))
    conn.commit()
    
def update_video(video_id,name,time):
    cursor.execute("UPDATE videos SET name =?,time=? WHERE id = ?",(name,time,video_id))
    conn.commit()
def delete_video(video_id):
    cursor.execute("DELETE FROM videos where id =?",(video_id,))
    conn.commit()
    
def main():
    while True :
           print("\n Youtube manager app with DB")
           print("1.List Videos")
           print("2.Add Videos")
           print("3.Update Videos")
           print("4.Delete Videos")
           print("5.exit app ")
           choice = input  ("Enter your choice :")
 
           if choice =='1':
             list_videos()
           elif choice == '2':
            name = input ("Enetr the Video name ")
            time = input ("Enetr the Video time  ")
            add_video(name,time)
           elif choice == '3':
            video_id = input ("Enter video ID to update ")
            name = input ("Enetr the Video name ")
            time = input ("Enetr the Video time  ")
            update_video(name,time,video_id)
           elif choice == '4':
               video_id = input ("Enter video ID to delete : ")
               delete_video(video_id)
           elif choice == '5':
             break 
           else :
               print("Invalid choice")
    
    conn.close()
    
    
if __name__== "__main__": 
      main() 

if __name__ == "__main__":  
    main()  
# ✅ This ensures main() only runs when file is run directly,  
# not when imported in another Python file

#cursor.execute() is used to send SQL commands (create, insert, update, delete, select) from Python to the database.
#the AUTOINCREMENT part makes SQLite automatically generate IDs:like 1,2,3

   