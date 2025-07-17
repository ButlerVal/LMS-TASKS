import uuid
from package_utils import save_package, load_package

class Package:
    def __init__(self, sender, recipient):
        self.id = str(uuid.uuid4())
        self.sender = sender
        self.recipient = recipient
        self.status = "In Transit"

    def __str__(self):
        return f"Id: {self.id}, Sender: {self.sender}, Recipient: {self.recipient}, Status: {self.status}"

def add_package(packages):
    sender = input("Enter the name of the sender: ").title().strip()
    recipient = input("Enter the name of the recipient: ").title().strip()
    details = Package(sender, recipient)
    packages.append(details)
    print(f"Package registered with ID: {details.id}")

def view_package(packages):
    if not packages:
        print("No Packages")
    else:
        print("All Packages:")
        for package in packages:
            print(package)

def mark_package(packages):
    package_id = input("Enter the package ID: ").strip()
    for package in packages:
        if package.id == package_id:
            package.status = "Delivered"
            print(f"Package {package_id} from {package.sender} has been marked as delivered.")
            return
    print("Package ID is not valid.")

def main():
    packages = []

    while True:
        print()
        print("----Package Menu-----")
        print("1. Register a package")
        print("2. View all packages")
        print("3. Mark package as delivered")
        print("4. Save to or Load from file")
        print("5. Save and Exit")

        choice = input("Pick a number from 1-5: ").strip()
        print()

        if choice == "1":
            add_package(packages)
        elif choice == "2":
            view_package(packages)
        elif choice == "3":
            mark_package(packages)
        elif choice == "4":
            print("Do you want to Save to or Load from file (S/L)?")
            ans = input("Enter S to save or L to load: ").upper().strip()
            if ans == "S":
                save_package(packages, 'package_data.json')
                print("Packages have been saved to file successfully.")
            elif ans == "L":
                packages = load_package('package_data.json')
                print("Packages have been loaded from file successfully.")
            else:
                print("Invalid input. Please enter S or L.")
        elif choice == "5":
            save_package(packages, 'package_data.json')
            print("Packages have been saved. Goodbye, thanks for using our package management system.")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()