from datetime import datetime
import diary_tools

class DiaryEntry:
    def __init__(self, title, content):
        self.date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.title = title
        self.content = content

    def __str__(self):
        return f"Date: {self.date}, Title: {self.title}\n Content: {self.content}"    

def main():
    entries = []
    filename = "diary_data.json"
    entries = diary_tools.load_entries(filename)

    while True:
        print()
        print("----Diary Menu-----")
        print("1. Add Entry")
        print("2. View all Entries")
        print("3. Search By Date or Title")
        print("4. Save and Exit")

        choice = input("Pick a number from 1-5: ").strip()
        print()

        if choice == "1":
            diary_tools.add_entries(entries)

        elif choice == "2":
            diary_tools.view_entries(entries)

        elif choice == "3":
            diary_tools.search_entries(entries)

        elif choice == "4":
            diary_tools.save_entries(entries, filename)
            print("Entries have been saved. Goodbye, thanks for using our Personal Diary App.")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()            