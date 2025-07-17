import json
import os
  

def save_package(packages, filename):
    package_list = []
    for package in packages:
        package_list.append({
            "Id": package.id,
            "Sender": package.sender,
            "Recipient": package.recipient,  
            "Status": package.status
        })
    with open(filename, 'w') as file:
        json.dump(package_list, file, indent=4)

def load_package(filename):
    from package_main import Package
    packages = []
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            package_list = json.load(file)
        for pkg in package_list:
            package = Package(pkg['Sender'], pkg['Recipient'])
            package.status = pkg['Status']
            package.id = pkg['Id']
            packages.append(package)
    else:
        print(f"{filename} does not exist")
    return packages
