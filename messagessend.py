import subprocess
import csv


with open('/Users/asaflebovic/Documents/contacts.csv') as f:
    reader = csv.reader(f)
    data = list(reader)

print(data)

count = 0
tot = len(data)

for i in data:
    try:
        count+=1
        comp = 100*count/(tot+1)
        int(i[1])
        rc = subprocess.check_call(["/Users/asaflebovic/Documents/messagesapp.sh",i[1],"Hello, {}. Thisoo is a test run. If you are receiving this message, it isn't good news. https://stackoverflow.com/users/6321606/alebovic".format(i[0])])
        print(str(comp) + "% COMPLETE (" + str(count) + "/" + str(tot+1) + ")")
    except:
        count+=1
        x = 0
