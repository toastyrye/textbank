#!/bin/sh
exec <"$0" || exit; read v; read v; exec /usr/bin/osascript - "$@"; exit

on run {phoneNumber, message}
    tell application "Messages"
    send message to buddy phoneNumber of service "SMS"
    end tell
end run
