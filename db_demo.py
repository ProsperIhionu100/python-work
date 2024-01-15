""""
In this example,we use the sqlite module to connect to an aqlite database named notes.db.
The program e


where you can choose to create a new note, read all notes, update a note, delete a note or exit 





"""

import sqlite3

#connect to the database  

conn = sqlite3.connect('notes.db')
cursor = conn.cursor()

# create the notes table
cursor.execute(''' CREATE TABLE IF NOT EXISTS notes               
               (id INTEGER PRIMARY KEY  AUTOINCREMENT,
               title TEXT,
               content TEXT)
               ''')
conn.commit()

# Function to create a new note

def create_note():
    title = input("Enter the note title: ")
    content = input("enter the  note content ")
    
    
    cursor.execute("INSERT  INTO notes (title,content)VALUES(?,?)" (title,content))
    conn.commit()
    print("note created sucessfully")
    
# Function to Read notes Successfully  
def read_notes():
    cursor.execute("SELECT * FROM notes")
    notes =cursor.fetchall()
    
    if len(notes) == 0:
        print("No notes found. ")
    else:
        for note in notes:
            print(f"ID: {note[0]}")
            print(f"Title: {note[1]}")
            print(f"content: {note[2]}")
# Function to update note

def update_note():
    note_id = input("Enter id of the note to update: ")
    new_title = input("Enter the new title:")
    new_content =input("Enter the new content :")
    
    if new_title and new_content:
        cursor.execute("UPDATE notes SET title = ?, content = ?WHERE id = ?" (new_title,new_content,note_id))                       
        conn.commit()
        print("note updated successfully")
    else:                           
        print("note content provided")
    
def delete_note():
        note_id = input("Enter the id of the note to delete: ")
        
    
        cursor.execute("DELETE FROM notes WHERE id  = ?", (note_id,))                       
        conn.commit()
        print("Note deleted  successfully")
        
# Main program loop
while True:
    print("Note-takinking application ")
    print("------------------------- ")
    print("1. Create a new note ")
    print("2. Read  all notes")
    print("3. Update a note")
    print("4. Delete a note")
    print("5. Exit")

    choice = input("Enter your choice (1-5):") 
    
    if choice == "1":
        create_note()
    elif choice == "2":
        read_notes()  
    elif choice == "3":
        update_note()
    elif choice == "4":
        delete_note()
    elif choice == "5":
        break
    else:
        print("Invalid choice. Please try again.")
        
# Close the database connection 
conn.close()