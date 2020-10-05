
import subprocess
import csv
import requests

bashfile = requests.get('https://raw.githubusercontent.com/alebovic/textbank/master/messagesapp.sh').text

'''with open(raw_input('Drop CSV file! '), 'r') as f:
    reader = csv.reader(f)
    data = list(reader)'''

data = [[2673472677, "Asaf"]]

print(data)

count = 0
tot = len(data)

for i in data:
    try:
        count+=1
        comp = 100*count/(tot+1)
        int(i[1])
        rc = subprocess.check_call([bashfile,i[1],"Hello, {name}! You have been bulk texted.".format(i[0])])
        print(str(comp) + "% COMPLETE (" + str(count) + "/" + str(tot+1) + ")")
    except:
        count+=1
        x = 0
