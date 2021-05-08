on run {targetBuddyPhone, targetMessage}
    set chars to characters of targetMessage
    activate application "Messages"
    tell application "System Events" to tell process "Messages"
        key code 45 using command down -- press Command + N to start a new window
        keystroke targetBuddyPhone -- input the phone number
        key code 36 -- press Enter to focus on the message area
        repeat with c from 1 to length of chars
            set currentChar to item c of chars
            if currentChar = "\n" then
                -- press Ctrl + Enter to type a newline.
                key code 36 using control down
            else
                -- type the next character.
               keystroke currentChar
            end if
        end repeat
        key code 36 -- press Enter to send
    end tell
end run
