import json

import os

from diary_main import DiaryEntry
  
def save_entries(entries, filename):
    entries_list = []
    for entry in entries:
        entries_list.append({
            "Date": entry.date,
            "Title": entry.title,
            "Content": entry.content,  
        })
    with open(filename, 'w') as file:
        json.dump(entries_list, file, indent=4)

def load_entries(filename):
    entries = []
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            try:
                entries_list = json.load(file)
                for ent in entries_list:
                    entry = DiaryEntry(ent['Title'], ent['Content'])
                    entry.date = ent['Date']
                    entries.append(entry)
            except json.JSONDecodeError:
                print("Diary data file is empty or corrupted. Starting fresh.")
    else:
        print(f"{filename} does not exist. Starting fresh.")
    return entries

def add_entries(entries):
    title = input("Enter your diary title: ").strip().capitalize()
    if not title:
        print("Title cannot be empty.")
        return
    
    content = input("Enter the contents of your diary: ").strip()
    if not content:
        print("Content cannot be empty.")
        return
    
    entry = DiaryEntry(title, content)
    entries.append(entry)
    print(f"'{title}' has been added successfully.")

def view_entries(entries):
    if not entries:
        print("No diary entries to display.")
        return
    print("\n----All Diary Entries----")
    for entry in entries:
        print(entry)

def search_entries(entries):
    keyword = input("Enter Date or Title to search for diary entry ")
    for entry in entries:
        if keyword.lower() in entry.date.lower() or keyword.lower() in entry.title.lower():
            print(entry)
            return            
    print("Invalid search key")