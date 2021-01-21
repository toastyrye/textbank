cd ~
git clone https://github.com/toastyrye/textbank
cd textbank
python --version
easy_install pip
pip --version
pip install virtualenv
python -m virtualenv env
source env/bin/activate
pip install -r requirements.txt
python messagessend.py
