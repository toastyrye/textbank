#!/bin/sh
exec <"$0" || exit; read v; read v; exec /usr/bin/osascript - "$@"; exit

MESSAGE="Hi! This is Alex with Sunrise San Diego. This Friday (1/22) we're hosting a Green New Decade livestream (bit.ly/SDGNDecade) about our city government, where they've historically failed, and how we want to see them do better! As far as accessibility we will have an ASL interpreter, captions, and a break in the middle. Will you join us at 6-8PM Pacific?"

on run {}
    tell application "Messages"
        set targetService to 1st service whose service type = iMessage
        set targetBuddy to buddy "+13017583707" of targetService
        send $MESSAGE to targetBuddy
    end tell
end run
