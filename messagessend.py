# -*- coding: utf-8 -*-

import csv
import time
import traceback
from subprocess import check_output

contacts="contacts.csv"
body = "body.txt"

with open(contacts, 'r') as f:
    reader = csv.reader(f)
    data = list(reader)

with open(body, 'r') as f:
    message_body = f.read()


print(data)
print("Message body: " + message_body)
raw_input("Proceed? (enter to continue, ctrl-c to stop)")

for i in data:
    if i[0] == "Name":
        continue

    try:
        phone_number = i[1]
        contact_name = i[0]
        message = message_body.format(name=contact_name)
        out = check_output(["osascript", "sendMessage.applescript", phone_number, message])
        print("Texted " + contact_name + " at number " + phone_number)
    except:
        print("Failed to text " + contact_name + " at number " + phone_number)
        traceback.print_exc()
    time.sleep(10)
