#!/bin/sh
exec <"$0" || exit; read v; read v; exec /usr/bin/osascript - "$@"; exit

on run {}
    tell application "Messages"
        set targetService to 1st service whose service type = iMessage
        set targetBuddy to buddy "2158051232‬" of targetService
        send "BIG INSANE POOPOO BIG POO POO BALLS HAHAHA" to targetBuddy
    end tell
end run
