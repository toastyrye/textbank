# -*- coding: utf-8 -*-

import subprocess
import csv
import time

filename="contacts.csv"
message_body = "This is Alex w/ Sunrise San Diego. This Friday (1/22), we are hosting a Green New Decade livestream (bit.ly/SDGNDecade) about our city government, where they have historically failed, and how we want to see them do better! As far as accessibiliy, we will have an ASL interpreter, captions, and a break in the middle. Will you join us at 6-8PM Pacific?"

with open(filename, 'r') as f:
    reader = csv.reader(f)
    data = list(reader)

print(data)
print("Message body: " + message_body)
rawinput("Proceed? (enter to continue, ctrl-c to stop)")

for i in data:
    if i[0] == "Name":
        continue

    time.sleep(1)
    
    try:
        phone_number = i[1]
        contact_name = i[0]
        message = "Hi " + contact_name +"! " + message_body
        subprocess.run(["osascript", "sendMessage.applescript", phone_number, message])
        print("Texted " + contact_name + " at number " + phone_number)
    except:
        print("Failed to text " + contact_name + " at number " + phone_number)

