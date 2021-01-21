import subprocess
import csv
import time

filename="contacts.csv"

with open(filename, 'r') as f:
    reader = csv.reader(f)
    data = list(reader)

print(data)

input("Proceed? (ctrl-c if not)")

for i in data:
    if i[0] == "Name":
        continue

    time.sleep(1)
    
    try:
        phone_number = i[1]
        contact_name = i[0]
        message = f"Hi {contact_name}!"
        # subprocess.run(["osascript", "sendMessage.applescript", phone_number, message])
        print(f"Texted {contact_name} at number {phone_number}")
    except:
        print(f"Failed to text {contact_name} at number {phone_number}")

