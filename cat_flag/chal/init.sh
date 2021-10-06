#!/bin/bash
set +m

RED='\033[0;31m'
GREEN='\033[0;32m'
NC='\033[0m' # No Color
print () {
    printf -- "$1\n"
}

/usr/games/cowsay "Welcome to [[cat flag]]"
print "It's time to get familiar with the command-line"
print ""
print "Here are the files we have in the directory"
print "-------------------------------------------"
ls
print "-------------------------------------------"
print "To complete the challenge, type the command:"
print "${GREEN}cat flag${NC} to read the flag!"
print ""
print ""
