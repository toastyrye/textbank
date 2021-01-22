Mac Textbank
============

A textbanking tool for mac using bash


Install
-------

1. Open Terminal app on mac

2. Run commands one by one

.. code-block::

        cd ~
        git clone https://github.com/toastyrye/textbank
        chmod +x install.sh
        sudo ./install.sh

3. Check if messages sent

Run
---

1. Edit messagessend.py with new message body.
2. Edit contacts.csv with textbank contacts (always good to test on yourself first).
3. Run script

.. code-block::

        python messagessend.py


Update
------

In case we make changes and you would like to update the app, run the following.

.. code-block::
        
        chmod +x update.sh && ./update.sh

Fixes
-----

 - `Send text messages to non-iphone through imessage <https://apple.stackexchange.com/questions/198223/how-do-i-send-text-messages-to-non-iphone-owners-using-the-imessage-app-on-a-mac>`__
