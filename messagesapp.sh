#!/bin/sh
exec <"$0" || exit; read v; read v; exec /usr/bin/osascript - "$@"; exit

on run {phoneNumber, message}
    tell application "Messages"
    send "BIG pooooopooo" to buddy 2673472677 of service "SMS"
    end tell
end run

