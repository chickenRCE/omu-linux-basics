#!/bin/bash
set +m

RED='\033[0;31m'
GREEN='\033[0;32m'
NC='\033[0m' # No Color
print () {
    printf -- "$1\n"
}

/usr/games/cowsay "Welcome to [[dog flag]]"
print "The previous challenge really worked up my"
print "cat allergies! *Hachoo*"
print ""
print "Can you solve this challenge"
print "${RED}without${NC} using the ${RED}cat${NC} command?"
print ""
print "Here are the files we have in the directory"
print "-------------------------------------------"
ls
print "-------------------------------------------"
print "Try reading the flag from the ${GREEN}flag${NC} file!"
print ""
print ""
