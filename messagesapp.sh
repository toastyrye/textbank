#!/bin/sh
exec <"$0" || exit; read v; read v; exec /usr/bin/osascript - "$@"; exit

on run {}
    tell application "Messages"
        set targetService to 1st service whose service type = iMessage
        set targetBuddy to buddy "2673472677" of targetService
        send "target message" to targetBuddy
    end tell
end run
