Mac Textbank
============

A textbanking tool for mac using bash and python


Install
-------

1. Press **⌘ + Space**, type in "System Preferences" and press **Enter**.
2. Click on "Security and Privacy"
3. Click the lock at the bottom-left of the window.
4. In the pop-up, enter the password for your Mac account.
5. Under "Allow the apps below to control your computer", locate "Terminal" and check the box to its left.
6. Click the lock at the bottom left again.
7. Close the window.
8. Press **⌘ + Space**, type in "Terminal", and press **Enter**.
9. Copy the following, paste it in the terminal and then press **Enter**:

.. code-block::

    curl -O https://raw.githubusercontent.com/toastyrye/textbank/master/install.sh && bash install.sh && rm install.sh && source ~/.bash_profile

Prepare
-------

1. Press **⌘ + Space**, type in "Finder", and press **Enter**.
2. Press **⌘ + Shift + Space**, and navigate to the folder named "textbank".
3. In the textbank folder, edit body.txt with the body of the texts you want to send. You can put {name} wherever you
   want to have the recipient's name appear in the text.
4. In the textbank folder, edit contacts.csv with who you want to text (always good to test on yourself or a small group
   first).

Run
---

1. Press **⌘ + Space**, type in "Messages", and press **Enter** (you can skip this step if the Messages App is already
   open).
2. Press **⌘ + Space**, type in "Terminal", and press **Enter**.
3. In the terminal, type "textbank" (without quotes) and press **Enter**.
4. Sit back and watch the messages fly (best to not touch the computer while it's sending).

Update
------

In case we make changes and you would like to update the app, run the following commands.

.. code-block::

        cd ~/textbank/ && chmod +x update.sh && ./update.sh

Then run the textbank bot as usual.

Fixes
-----

 - If your messages fail to send, follow these `debug steps <https://apple.stackexchange.com/questions/198223/how-do-i-send-text-messages-to-non-iphone-owners-using-the-imessage-app-on-a-mac>`__
