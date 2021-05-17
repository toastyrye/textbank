#!/usr/bin/env bash

cd
mkdir -p textbank
cd textbank
curl -O https://raw.githubusercontent.com/toastyrye/textbank/master/messagessend.py
curl -O https://raw.githubusercontent.com/toastyrye/textbank/master/sendMessage.applescript
curl -O https://raw.githubusercontent.com/toastyrye/textbank/master/body.txt
curl -O https://raw.githubusercontent.com/toastyrye/textbank/master/contacts.csv

if ! command -v textbank &> /dev/null; then
    cat <<EOF >> ~/.bash_profile
textbank() {(
    cd ~/textbank && python messagessend.py
)}
EOF
fi
