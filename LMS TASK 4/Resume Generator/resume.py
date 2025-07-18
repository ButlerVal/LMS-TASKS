import json
import os
from formatter import format_txt_resume, format_md_resume

def load_resume(filename="resume.json"):
    if not os.path.exists(filename):
        print(f"Error: {filename} not found.")
        return None
    with open(filename, "r") as f:
        return json.load(f)

def save_resume(data, format_type):
    output_filename = f"resume.{format_type}"
    if format_type == "txt":
        content = format_txt_resume(data)
    elif format_type == "md":
        content = format_md_resume(data)
    else:
        print("Invalid format type.")
        return
    with open(output_filename, "w") as f:
        f.write(content)
    print(f"Resume exported to {output_filename}")

def main():
    resume_data = load_resume()
    if not resume_data:
        return

    while True:
        print("\n=== Resume Generator ===")
        print("1. Export as .txt")
        print("2. Export as .md")
        print("3. Exit")
        choice = input("Select an option: ").strip()

        if choice == "1":
            save_resume(resume_data, "txt")
        elif choice == "2":
            save_resume(resume_data, "md")
        elif choice == "3":
            print("Goodbye! Thanks for using the Resume Generator.")
            break
        else:
            print("Invalid option. Please try again.\n")

if __name__ == "__main__":
    main()