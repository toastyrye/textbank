Mac Textbank
============

A textbanking tool for mac using bash and python


Install
-------

1. Open Terminal app on mac
2. Run commands one by one

.. code-block::

        cd ~
        git clone https://github.com/toastyrye/textbank
        chmod +x install.sh
        sudo ./install.sh

3. Type your user password for your mac account

Run
---

1. Edit messagessend.py with new message body (might want to change time.sleep() as well if your computer isn't 8 years old like mine)
2. Edit contacts.csv with textbank contacts (always good to test on yourself or a small group first)
3. Run script

.. code-block::

        python messagessend.py

4. Sit back and watch the messages fly

Update
------

In case we make changes and you would like to update the app, run the following commands.

.. code-block::

        cd ~/textbank/ && chmod +x update.sh && ./update.sh

Then run the textbank bot as usual.

Fixes
-----

 - If your messages fail to send, follow these `debug steps <https://apple.stackexchange.com/questions/198223/how-do-i-send-text-messages-to-non-iphone-owners-using-the-imessage-app-on-a-mac>`__
